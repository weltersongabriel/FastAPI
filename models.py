from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

# cria a conexao do seu banco
db = create_engine("sqlite:///banco.db")

# criar as classes do banco
Base = declarative_base()

# criar as classes/tabela do banco

class Usuario(Base):
    __tablename__ = "usuarios"

    id =  Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String)
    ativo = Column ("ativo", Boolean)
    admin = Column ("admin", Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

# PEDIDOS
class Pedido(Base):
    __tablename__= "pedidos"

#    STATUS_PEDIDOS = (
#       ("PENDENTE", "PENDENTE"),
#        ("CANCELADO", "CANCELADO"),
#        ("FINALIZADO", "FINALIZADO")
#    )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String) # pendente cancelado finalizado
    usuario = Column("usuario", ForeignKey("usuarios.id"))
    preco = Column("preco", Float)


    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.usuario = usuario
        self.preco = preco
        self.status = status


# Itens Pedidos
class ItemPedido(Base):
    __tablename__ = "itens_pedido"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", String)
    preco_unitario = Column("preco_unitatio", Float)
    pedido = Column("pedido", ForeignKey("pedidos.id"))

    def __int__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido



# executar a criação dos metadados do seu banco
