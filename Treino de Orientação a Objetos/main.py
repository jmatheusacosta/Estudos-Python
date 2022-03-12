from animal import Animal

elephant = Animal("Elefante","Grande","Mamíferos","Terrestre")
salmon = Animal("Salmão","Pequeno","Peixe","Aquático")

salmon.paws_number = 0

elephant.breathe()

print("\nO "+ elephant.name+ " é "+ elephant.size+ ", da família de "+ elephant.type+ ", seu habitat é o "+ elephant.habitat)

print("\nO "+ salmon.name+ " é "+ salmon.size+ ", da família de "+ salmon.type+ ", seu habitat é o "+ salmon.habitat)