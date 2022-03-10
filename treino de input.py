name = None

while not name:
    print()
    name = input("Qual o seu nome?")
print()
print("Olá " + name)
print()



idade = int(input("Quantos anos você tem?"))

if idade >= 18:
        print()
        print("Entendo... você é maior de idade!")
        print()
elif idade < 0:
        print()
        print("Você ainda nem nasceu")
        print()
else:
        print()
        print("Você é menor de idade")
        print()


altura = float(input("Qual a sua altura em metros?"))

print()
print("Você tem " + str(altura) + " de altura")

