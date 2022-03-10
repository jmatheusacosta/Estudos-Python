def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("----------------------------------------------------")
        print(key)
        print()
        for i in options[question_num-1]:
            print(i)
        print()
        guess = input("Escolha entre A,B,C ou D: ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num +=1
    display_score(correct_guesses, guesses)

# --------------------------

def check_answer(answer, guess):

    if answer == guess:
        print("CORRETO!")
        return 1
    else:
        print("ERRADO!")
        return 0


# --------------------------

def display_score(correct_guesses, guesses):
    print("----------------------------------------------------")
    print("RESULTADOS")
    print("----------------------------------------------------")

    print("Respostas Certas:", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("  Suas Respostas:", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()
    print()
    score = int(correct_guesses/len(questions)*100)
    print("Sua pontuação é: ", str(score), "%")

# --------------------------

def play_again():
    response = input("Você quer jogar novamente(SIM ou NÃO)")
    response = response.upper()

    if response == "SIM":
        return True
    else:
        return False

questions = {
    "Quem é o principal fundador da Microsoft?": "C",
    "Em que ano estamos?": "A",
    "A terra é plana?": "B",
    "Esse quiz foi feito em qual linguagem de programação?": "D"
}

options = [["A.Jeff Bezos","B.Elon Musk","C.Bill Gates","D.Steve Jobs"],["A.2022","B.2012","C.2004","D.2020"],
           ["A.Sim","B.Não","C.As vezes","D.Talvez"],["A.C","B.Java","C.Ruby","D.Python"]]

new_game()

while play_again():
    new_game()
print()
print("Tchau!")