
cars = [("Palio", "Fiat", 15),
        ("Golf", "Volkswagen", 20),
        ("Prism", "Chevrolet", 13),
        ("Supra", "Toyota", 40),
        ("Civic", "Honda", 25)]

to_dollars = lambda data: (data[0], data[1], data[2]*0.21)
cars_dollars = list(map(to_dollars, cars))

power = lambda powers: powers[2]
cars.sort(key= power, reverse= True)

for i in cars:
    print(i)
print("")
print("------------LISTA EM DÓLAR----------------------")


for i in cars_dollars:
    print(i)

price_low = lambda data: data[2] <= 20

cheap_cars = list(filter(price_low, cars))

print()
print("------------LISTA BARATINHOS------------------")

for i in cheap_cars:
    print(i)