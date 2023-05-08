import sqlite3  

bancoContatos = sqlite3.connect("bancoContatos.db ")  
#bancoContatos.execute("CREATE TABLE contatos(nome text, numero integer)")
cursor = bancoContatos.cursor()

def inserir(nome, numero):
    cursor.execute(f"INSERT INTO contatos VALUES('{nome}', {numero})")
    bancoContatos.commit()
    
def visualizar():
    cursor.execute(f"SELECT * FROM contatos")
    #print(cursor.fetchall())
    for visualiza in cursor.fetchall():
        print(f'- {visualiza}')
    bancoContatos.commit()
    
def deletar(numero):
    cursor.execute(f"DELETE FROM contatos WHERE numero = {numero}")
    bancoContatos.commit()
    
def atualizar(numeroAgora, numeroAntes):
    #Alterar
    cursor.execute(f"UPDATE contatos SET numero = {numeroAgora} WHERE numero = {numeroAntes}")
    bancoContatos.commit()
    
print('-'*10,'REGISTRO CONTATOS','-'*10)
while True:
    print('\n---- MENU INICIAL -----')
    print('1 - Cadastrar\n2 - Alterar\n3 - Deletar\n4 - Visualizar registros')
    op = int(input('Opção desejada: '))
    if op == 1:
        print('\n---> Cadastro')
        nome = input('Nome: ')
        numero = int(input('Número: '))
        inserir(nome, numero)
    if op == 2:
        print('\n---> Alterar')
        numeroAntes = int(input('Qual número gostaria de alterar: '))
        numeroAgora = int(input('Qual será o número atual: '))
        atualizar(numeroAgora, numeroAntes)
    if op == 3:
        print('\n---> Excluir')
        numero = int(input('Qual número gostaria de apagar: '))
        deletar(numero)
    if op == 4:
        print('\n---> Visualizar todos')
        visualizar()
    if op > 5 or op < 1:
        print("\nPoxa, que pena, até a próxima")
        break

bancoContatos.close()