import ex1

a = []
b = []
x = 0

while x != 4:
    x = int(input("1 para adicionar um produto e seu preço \n2 para remover um produto e seu preço \n3 para mostrar os "
                  "produtos e preços \n4 para encerrar \nESCOLHA: "))

    if x == 1:
        prod = input("Digite seu produto: ")
        preç = float(input("Digite o preço: "))
        ex1.sign_value(a, prod)
        ex1.sign_value(b, preç)
    elif x == 2:
        elem = int(input("Digite a posição do produto que deseja remover na lista: "))
        ex1.delete_el(a, (elem - 1))
        ex1.delete_el(b, (elem - 1))
    elif x == 3:
        ex1.show_list(a, b)
        print("\n")
    elif x == 4:
        exit()
    else:
        print("VALOR INVÁLIDO \n")