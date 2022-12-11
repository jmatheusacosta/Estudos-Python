#AULA PRÁTICA

print("------------QUESTÃO 1------------")

price1 = float(input("Digite o preço antigo: "))

print(f'O preço com o desconto de 10% é: R$ {price1*0.9 :.2f}')

print("------------QUESTÃO 2------------")

fix_sal = float(input("Digite o salário fixo:  "))
sales = float(input("Digite o valor arrecadado em vendas:  "))

print(f'O salário final é R$ {fix_sal + (sales*0.05) :.2f}')

print("------------QUESTÃO 3------------")

past_w = float(input("Digite seu peso a 3 meses atrás:  "))
today_w = float(input("Digite seu peso hoje em dia:  "))

print(f"Sua mudança de peso foi de: {((today_w*100)/past_w)-100 :.2f}%")

print("------------QUESTÃO 4------------")

bigger_s = int(input("Digite o tamanho do lado maior do trapézio:  "))
smaller_s = int(input("Digite o tamanho do lado menor do trapézio:  "))
height_t = int(input("Digite a altura do trapézio:  "))

print("A área do trapézio é: ", ((bigger_s+smaller_s)*height_t)/2)
