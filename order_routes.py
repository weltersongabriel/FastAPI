from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import pegar_sessao, verificar_token
from schemas import PedidoSchema, ItemPedidoSchema, ItemPedido
from models import Pedido, Usuario

order_router = APIRouter(prefix="/pedidos", tags=["pedidos"], dependencies=[Depends(verificar_token)])

@order_router.get("/")
async def pedidos():
    return {"mensagem": "vc acessou a rota dos pedidos"}


@order_router.post("/pedido")
async def criar_pedido(pedido_schema: PedidoSchema, session: Session = Depends(pegar_sessao)):
    novo_pedido = Pedido(usuario=pedido_schema.usuario)
    session.add(novo_pedido)
    session.commit()
    return {"mensagem": f"Pedido criado com sucesso: {novo_pedido.id}"}


@order_router.post("/pedido/cancelar/{id_pedido}")
async def cancelar_pedido(id_pedido: int, session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    # usuario.admin = True
    # usuario.id = pedido.usuario
    pedido = session.query(Pedido).filter(Pedido.id == id_pedido).first()

    if not pedido:
        raise HTTPException(status_code=400, detail="Pedido não encontrado")
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=401, detail="Voce não tem autoriação para faxer essa modificação")
    
    pedido.status = "CANCELADO"
    session.commit()
    return {
        "mensagem": f"Pedido número: {id_pedido} cancelado com sucesso",
        "pedido": pedido
    }


@ order_router.get("/listar")
async def listar_pedidos(session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    if not usuario.admin:
        raise HTTPException(status_code=401, detail="Voce não tem autoriação para faxer essa operação")
    else:
        pedido = session.query(Pedido).all()
        return {
            "pedidos": pedidos
        }
    
@order_router.post("/pedido/adicionar-item/{id_pedido}")
async def adicionar_item_pedido(id_pedido: int, 
                                item_pedido_schema: ItemPedidoSchema, 
                                session: Session = Depends(pegar_sessao), 
                                 usuario: Usuario = Depends(verificar_token)):
    pedido = session.quer(Pedido).filter(Pedido.id==id_pedido).first()
    if not pedido:
        raise HTTPException(status_code=400, detail="Pedido não existente")
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=401, detail="Voce nã tem autorização para fazer essa operação")
    
    item_pedido = ItemPedido(item_pedido_schema.quantidade, item_pedido_schema.sabor,
                             item_pedido_schema.tamanho, item_pedido_schema.preco_unitario,
                             item_pedido_schema.id.pedido)
    
    pedido.calcular_preco()
    session.add(item_pedido)
    session.commit()
    return {
        "mensagem": "Item criado com sucesso",
        "item_id": item_pedido.id,
        "preco_pedido": pedido.preco
    }