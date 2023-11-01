from controller import PessoaController

while True:
    print('1 para Cadastrar\n2 para Logar\n3 para Sair')
    try:
        op = int(input())
        if op == 1:
            nome=input('\ndigite nome ')
            email=input('\ndigite email ')
            senha=input('\ndigite senha ')
            result = PessoaController.cadastrar(nome=nome, email=email, senha=senha)
            print(result)
            if result == 2:
                print('tamanho do nome inválido')
            elif result == 3:
                print('tamanho do email inválido')
            elif result == 4:
                print('tamanho da senha inválido')
            elif result == 5:
                print('email já cadastrado')
            elif result == 6:
                print('erro interno do sistema')
            elif result == 1:
                print("OK")
            input()
        elif op == 2:
            email=input('\ndigite email ')
            senha=input('\ndigite senha ')
            result = PessoaController.login(email=email, senha=senha)
            print(result)
            input()
        elif op == 3:
            break
    except:
        print('digite somente opções válidas')
        input()

    print("Finalizado com Sucesso")