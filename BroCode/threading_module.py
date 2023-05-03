import time
import threading

def watch_video():
    time.sleep(3)
    print("O vídeo terminou!   ")

def clean_house():
    time.sleep(5)
    print("Você terminou a limpeza!   ")

def water_plants():
    time.sleep(3)
    print("Você terminou de regar as plantas!   ")

def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logado por: ", count, "segundos.")

t = threading.Thread(target= timer, daemon=True)
t.start()

x = threading.Thread(target = watch_video, args=() )
x.start()

y = threading.Thread(target= clean_house, args=())
y.start()

z = threading.Thread(target= water_plants(), args=())
z.start()
