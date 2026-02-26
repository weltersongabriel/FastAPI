from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base

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

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String) # pendente cancelado finalizado
    usuario = Column("usuario", ForeignKey("usuarios.id"))
    preco = Column("preco", Float)


    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.usuario = usuario
        self.preco = preco
        self.status = status



# PAROU NO MINUTO 30 DA AULA 3



# executar a criação dos metadados do seu banco