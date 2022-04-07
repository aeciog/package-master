# Este programa é escrito em Classes e Objetos

import pickle  # implementa protocolos binários para serializar e desserializar uma estrutura de objeto Python.
import os
import pathlib


class Conta:
    accNo = 0
    nome = ''
    deposito = 0
    tipo = ''

    def criarConta(self):
        self.accNo = int(input('Digite o número da conta: '))
        self.nome = input('Digite o nome do títular: ')
        self.tipo = input('Digite o tipo de conta [C/P]: ')
        self.deposito = int(input('Insira o valor (>=500 para salvar e >= 1000 para corrente: '))
        print("\n\n\nConta Criada")

    def mostrarConta(self):
        print('Número da conta: ', self.accNo)
        print('Titular: ', self.nome)
        print('Tipo de Conta: ', self.tipo)
        print('Balanço: ', self.deposito)

    def modificarConta(self):
        print('Número da conta: ', self.accNo)
        self.name = input('Altere o nome: ')
        self.tipo = input('Altere o tipo da conta: ')
        self.deposito = int(input('Altere o valor: '))

    def depositoMontante(self, montante):
        self.deposito += montante

    def retirarMontante(self, montante):
        self.deposito -= montante

    def getContaNo(self):
        return self.accNo

    def getContaTitularNome(self):
        return self.name

    def getDeposito(self):
        return self.deposito


def intro():
    print("\t\t\t\t*********************************")
    print("\t\t\t\tSISTEMA DE GERENCIAMENTO BANCÁRIO")
    print("\t\t\t\t*********************************")

    input('Precione para continuar...')


def escrevaConta():
    conta = Conta()
    conta.criarConta()
    gravarArquivosContas(conta)


def mostrarTudo():
    file = pathlib.Path("contas.data")
    if file.exists():
        infile = open('contas.data', 'rb')
        mylist = pickle.load(infile)
        for item in mylist:
            print(item.accNo, " - ", item.nome, " - ", item.tipo, " - ", item.deposito)
        infile.close()
    else:
        print("Não há registros a serem exibidos")


def displaySp(num):
    file = pathlib.Path("contas.data")
    if file.exists():
        infile = open('contas.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist:
            if item.accNo == num:
                print("Seu balanço na conta é = ", item.deposito)
                found = True

        else:
            print("Nenhum registro para pesquisar")
        if not found:
            print("Nenhum registro existente com este número")


def depositarSacar(num1, num2):
    file = pathlib.Path("contas.data")
    if file.exists():
        infile = open('contas.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('contas.data')
        for item in mylist:
            if item.accNo == num1:
                if num2 == 1:
                    depositar = int(input("Insira o valor a depositar"))
                    item.deposito += depositar
                    print("Sua conta está atualizada")
                elif num2 == 2:
                    depositar = int(input("Insira o valor a ser retirado"))
                    if depositar <= item.deposito:
                        item.deposito -= depositar
                    else:
                        print("Você não pode sacar grandes quantias")
    else:
        print("Nenhum registro para pesquisar")
    outfile = open('novasContas.data', 'wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('novasContas.data', 'contas.data')


def deletarConta(num):
    file = pathlib.Path("contas.data")
    if file.exists():
        infile = open('contas.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        newList = []
        for item in oldlist:
            if item.accNo != num:
                newList.append(item)
        os.remove('contas.data')
        outfile = open('novasContas.data', 'wb')
        pickle.dump(newList, outfile)
        outfile.close()
        os.rename('novasContas.data', 'contas.data')


def modificarConta(num):
    file = pathlib.Path("contas.data")
    if file.exists():
        infile = open('contas.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('contas.data')
        for item in oldlist:
            if item.accNo == num:
                item.nome = input("Digite o nome do titular da conta: ")
                item.tipo = input("Digite o tipo de conta: ")
                item.deposito = int(input("Insira o valor: "))

        outfile = open('novasContas.data', 'wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('novasContas.data', 'contas.data')


def gravarArquivosContas(Conta):
    file = pathlib.Path("contas.data")
    if file.exists():
        infile = open('contas.data', 'rb')
        oldlist = pickle.load(infile)
        oldlist.append(Conta)
        infile.close()
        os.remove('contas.data')
    else:
        oldlist = [Conta]
    outfile = open('novasContas', 'wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('novasContas', 'contas.data')

#start do programa
ch = ''
num = 0
intro()

while ch != 8:
    # system("cls");
    print("\tMENU PRINCIPAL")
    print("\t1. NOVA CONTA")
    print("\t2. VALOR DO DEPÓSITO")
    print("\t3. RETIRAR MONTANTE")
    print("\t4. CONSULTA DE SALDO")
    print("\t5. LISTA DE TODOS OS TITULARES DE CONTA")
    print("\t6. FECHAR UMA CONTA")
    print("\t7. MODIFICAR UMA CONTA")
    print("\t8. SAIR")
    print("\tSelecione sua opção (1-8): ")
    ch = input()
    # system("cls");

    if ch == '1':
        escrevaConta()
    elif ch == '2':
        num = int(input("\tDigite o número da conta: "))
        depositarSacar(num, 1)
    elif ch == '3':
        num = int(input("\tDigite o número da conta: "))
        depositarSacar(num, 2)
    elif ch == '4':
        num = int(input("\tDigite o número da conta: "))
        displaySp(num)
    elif ch == '5':
        mostrarTudo()
    elif ch == '6':
        num = int(input("\tDigite o número da conta: "))
        deletarConta(num)
    elif ch == '7':
        num = int(input("\tDigite o número da conta: "))
        modificarConta(num)
    elif ch == '8':
        print("\tObrigado por usar o sistema de gestão bancária")
        break
    else:
        print("Escolha inválida")

    ch = input("Tecle ENTER para menu")