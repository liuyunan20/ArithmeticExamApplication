# read animals.txt
with open("animals.txt", "r") as file:
    animals = file.readlines()
    file.close()

# animals = ["rabbit\n", "cat\n", "turtle"]
new_animals = []
for x in range(len(animals) - 1):
    new_animal = animals[x].rstrip("\n")

    new_animals.append(new_animal)
new_animals.append(animals[-1])
new_string = " ".join(new_animals)
with open("animals_new.txt", "w", encoding='utf-8') as new_file:
    new_file.write(new_string)
    new_file.close()

# and write animals_new.txt
