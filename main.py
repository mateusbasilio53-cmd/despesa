import sqlite3

conexao = sqlite3.connect('financas.db')
cursor = conexao.cursor()

print('Rastreador de despesas pessoal')

while True:
    print('-------------------------------')
    print('Menu:')
    print('1. Adicionar despesa')
    print('2. Ver despesas')
    print('3. Sair')
    print('-------------------------------')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        descricao = input('Digite a descrição da despesa: ')
        categoria = input('Digite a categoria da sua despesa: ')
        valor = float(input('Digite o valor da despesa: '))
        data = input('Digite a data da despesa (DD/MM/AAAA): ')
        cursor.execute('''
            INSERT INTO despesas (descricao, categoria, valor, data)
            VALUES (?, ?, ?, ?)
        ''', (descricao, categoria, valor, data))
        conexao.commit()
        print(f'Despesa "{descricao}" da categoria {categoria} de R${valor:.2f} na data {data} adicionada com sucesso!')

    elif opcao == '2':
        print('Exibindo todas as despesas...')
        cursor.execute('SELECT * FROM despesas')
        despesas = cursor.fetchall()
        for despesa in despesas:
            print(f'ID: {despesa[0]}, Descrição: {despesa[1]}, Categoria: {despesa[2]}, Valor: R${despesa[3]:.2f}, Data: {despesa[4]}')

    elif opcao == '3':
        print('Saindo...')
        break

    else:
        print('Opção inválida. Tente novamente.')