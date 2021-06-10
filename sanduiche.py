lista_dos_produtos = []  # Lista de produtos novos
                         # que é colocado após feito o login
                         # e selecionar a opção correspondente


def telaInicio():  # Visual da tela de inicio
    print('###################################')
    print('#                                 #')
    print('#                                 #')
    print('#         TELA PRINCIPAL          #')
    print('#                                 #')
    print('#                    por: Carlos  #')
    print('###################################')


def telaPrincipal():  # Tela principal, após o login feito ela aparece
    print("""          ´´´´´´´´´     PAINEL PRINCIPAL     ´´´´´´´
           ´´´´´´$$                      $$´´´´´´
           ´´´´´´$$       Criado por     $$´´´´´´
           ´´´´´´´$$s      @Carlos     s$$´´´´´´´
           ´´´´´´´´$$$$              $$$$´´´´´´´´
           ´´´´´´´´´³$$$$´¶¶¶¶¶¶¶¶´$$$$³´´´´´´´´´
           ´´´´´´´´´´³$$$$´¶¶¶¶¶¶´$$$$³´´´´´´´´´´
           ´´´´´´´´´¶´$$$$$´¶¶¶¶´$$$$$´¶´´´´´´´´´
           ´´´´´´´´¶¶¶´$$$´¶¶¶¶¶¶´$$$´¶¶´´´´´´´´´
           ´´´´´´´´¶¶¶¶¶´´¶¶¶¶¶¶¶¶´´¶¶¶¶´´´´´´´´´
           ´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´
           ´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´
           ´´´´´´´´´´¶¶´´´´¶¶¶¶´´´´´¶¶´´´´´´´´´´´
           ´´´´´´´´´´¶¶´´´´¶¶¶¶´´´´´¶¶´´´´´´´´´´´                    
           ´´´´´´´´´´¶¶¶¶¶¶¶¶´¶¶¶¶¶¶¶¶´´´´´´´´´´´
           ´´´´´´´´´´´¶¶¶¶¶¶´´´¶¶¶¶¶¶¶´´´´´´´´´´´
           ´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´
           ´´´´´´´´´´´´´´¶´¶´¶´¶´¶´´´´´´´´´´´´´´´
           ´´´´´´¶´´´´´´´¶´´´´´´´¶´´´´´´´¶´´´´´´´
           ´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´
           ´´´´´¶¶´´´´´´´´¶´´´´´¶´´´´´´´´¶¶´´´´´´
           ´´´´´¶¶´´´´´´´¶¶´´´´´¶¶´´´´´´´¶¶´´´´´´
           ´´´´´¶¶´¶¶´¶¶´¶´´´´´´´¶´¶¶´¶¶´¶¶´´´´´´
           ´´´¶´¶¶´¶¶´¶¶´¶´´´´´´´¶´¶¶´¶¶´¶¶´¶´´´´
           ´´¶¶´¶¶´¶¶´¶¶´¶´´´´´´´¶´¶¶´¶¶´¶¶´¶¶´´´
           ´´´¶¶¶¶´¶¶´¶¶´´´´´´´´´´´¶¶´¶¶´¶¶¶¶´´´´
           ´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´´´´¶¶´¶¶´¶¶¶´´´´""")


telaInicio()

while True:  # Loop principal
    print('\n1 - Fazer login')
    print('2 - Sair')
    inicio = int(input('\nDigite uma opção(1 ou 2): '))

    # Caso opção (1, 2 ou 3) faça algo
    if inicio == 1:
        print('\n-=- Tela de Login =-=')
        while True:  # Loop para 'login', Verificação ##PRINCIPAL##
            User = str(input('USUÁRIO: ')).strip()
            Passw = input('SENHA: ').strip()

            if User == 'admin' and Passw == 'admin123':
                print('LOGIN EFETUADO COM SUCESSO\n')
                break
            else:
                print('\nUsuário ou Senha incorretos')

        telaPrincipal()
        print(f'                  Seja-bem vindo {User}')
        print('OPÇÕES:')
        print('[I] - Cadastrar novo produto')

        while True:  # Loop para cadastro de novo produto ou sair da conta
            novamente = str(input('\nCadastrar um novo produto?[S/N] ')).strip().title()
            # COLOCAR FINALIZAÇÃO DO FOR ##PRINCIPAL##
            p = 2

            if novamente == 'S':
                nomeProduto = str(input('\nNome do produto: ')).strip().title()
                lista_dos_produtos.append(nomeProduto)
                precoProduto = float(input('Preço do produto: R$'))
                lista_dos_produtos.append(precoProduto)
                estoqueProduto = int(input('Estoque de quanto(s)? '))
                lista_dos_produtos.append(estoqueProduto)
                print('Produto cadastrado com sucesso!\n')
                print('-=-=-=-=-=-=- Lista dos produtos -=-=-=-=-=-=-=-=')
                print('Nome do Produto  |  Preço  |    Estoque(Quantid.)')

                for v in range(0, len(lista_dos_produtos)):  # LOOP QUE MOSTRA NA TELA OS INTENS CADASTRADOS
                    print('', end=' ')
                    print(f'    {lista_dos_produtos[v]}     ', end=' ')
                    if v == p:
                        print('\n')
                        p+=3

            elif novamente == 'N':
                inicio = str(input('\nDeseja sair mesmo?(S/N) ')).strip().title()
                if inicio in 'Ss':
                    print('\nVolte sempre!')
                    break
            else:
                print('\nERRO. Tente novamente')
        break

    elif inicio == 2:
        print('\nVolte sempre!')
        break

    else:
        print('\nInválido. Opções são apenas 1 e 2')
