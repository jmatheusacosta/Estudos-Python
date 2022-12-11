from tkinter import *
import time

window = Tk()
window.geometry("1024x768")
window.title("JAO CODIGOS")

icon = PhotoImage(file='imagens/cinas.png')
window.iconphoto(True, icon)
window.config(background="black")

x = BooleanVar()



def display():
    if (x.get()==1):
        print("VOCÊ APERTOU")
    else:
        print("VOCê TIROU")

photo = PhotoImage(file='imagens/cinas.png')



ordem_photo = PhotoImage(file='imagens/ordem.png')


label = Label(window, text="QUAL É ESSE RITUAL?",
              font=('Arial', 40,'bold'),
              fg='white',
              bg='black',

              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom',
              )
label.pack()

labelright = Label(window,
                   text="RESPOSTA CERTA!",
                   font=('Arial', 15, 'bold'),
                   fg='white',
                   bg='black'
                   )

labelwrong = Label(window,
                   text="RESPOSTA ERRADA...",
                   font=('Arial', 15, 'bold'),
                   fg='white',
                   bg='black'
                   )

entry = Entry(window,
              font=("Arial", 30))
entry.pack(side=LEFT)

check_button = Checkbutton(window,
                           text="eu concordo com isso",
                           variable=x,
                           onvalue=True,
                           offvalue=False,
                           command=display,
                           font=('Arial', 20),
                           image=ordem_photo,
                           compound='left',
                           fg='#630BD6',
                           bg='black',
                           activeforeground='#630BD6',
                           activebackground='black')
check_button.pack(side=BOTTOM)

def click():
    resposta = entry.get()
    if resposta == "cinerária":
        print("RESPOSTA CERTA!")

        labelright.pack(side=RIGHT)

    else:
        print("RESPOSTA ERRADA...")

        labelwrong.pack(side=RIGHT)


button = Button(window,
                text="submit",
                command=click,
                font=("Arial", 10),
                )
button.pack(side=RIGHT)


window.mainloop()