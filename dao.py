from model import Pessoa
from config import get_session
import hashlib

class PessoaDao:
    @classmethod
    def cadastrar(cls, nome, email, senha):
        session = get_session()
        senha=hashlib.sha256(senha.encode()).hexdigest()
        p1=Pessoa(nome=nome,email=email, senha=senha)
        session.add(p1)
        session.commit()
    
    @classmethod
    def getUser(cls, email):
        session = get_session()
        user = session.query(Pessoa).filter(Pessoa.email == email).all()
        return user

    @classmethod
    def login(cls,email, senha):
        session =  get_session()
        senha = hashlib.sha256(senha.encode()).hexdigest()
        logado = session.query(Pessoa).filter(Pessoa.email==email).filter(Pessoa.senha == senha).all()
        return logado
    
