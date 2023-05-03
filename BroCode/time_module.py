import time

print(time.ctime(0)) # converte tempo em segundos desde a epoch( quando seu pc acha que o tempo "começou")
print()

print(time.time()) # retorna segundos passados desde a epoch
print()

print(time.ctime(time.time())) # para mostrar a data e hora de agora
print()

time_object = time.localtime() # pega a data e hora local mas não está em um formato legível
print(time_object)

print()

local_time = time.strftime("%d %B %Y %H:%M:%S", time_object) #transformando o localtime em algo legível
print(local_time)

