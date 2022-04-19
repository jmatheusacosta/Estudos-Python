
def maiusculo(text):
    return text.upper()
    
def minusculo(text):
    return text.lower()
    
def texto(func):
    text = func("Olá")
    print(text)
    
texto(maiusculo)


age_check = lambda age: True if int(age) >= 18 else False

print(age_check(int(age := input("Digite sua idade"))))

if int(age) >= 18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade")
    