from dao import PessoaDao

class PessoaController():
    @classmethod
    def verifica_dados(cls, nome, email, senha):
        if 3 > len(nome) or len(nome) > 50:
            return 2
        if len(email) > 200:
            return 3
        if 6 > len(senha) or len(senha) > 100:
            return 4
        return 1

    @classmethod
    def cadastrar(cls, nome, email, senha):
        try:
            usuario = PessoaDao.getUser(email)
            if len(usuario) > 0:
                return 5
            dados_verificados = cls.verifica_dados(nome=nome, email=email, senha=senha)
            if dados_verificados != 1:
                return dados_verificados
            PessoaDao.cadastrar(nome=nome, email=email, senha=senha)
            return 1
        except:
            return 6

    @classmethod
    def login(cls, email, senha):
        logado = PessoaDao.login(email=email, senha=senha)
        if len(logado) == 1:
            return {'logado':True, 'id': logado[0].id}
        else:
            return False

# result = PessoaController.cadastrar(nome='tiago',email='tetigo@gmail.com',senha='123456')
# print(result)

if __name__ == '__main__':
    # print(PessoaController.cadastrar('tiago', 'tetigo@gmail.com', '123456'))
    print(PessoaController.login('tetigo@gmail.com', '123456'))