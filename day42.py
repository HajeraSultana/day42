title = "MokeBeast"
print(f"{title: ^60}")
print()


beast = {"Beast Name" : None, "Type": None, "Special Move" : None, "HP": None, "MP": None}

for name, value in beast.items():
    beast[name] = input(f"{name}: \t").strip().title()

if beast["Type"] == "Earth":
        print("\033[32m", end="")
elif beast["Type"] == "Air":
        print("\033[37m", end="")
elif beast["Type"] == "Fire":
        print("\033[31m", end="")
elif beast["Type"] == "Water":
        print("\033[34m", end="")
else:
        print("\033[33m", end="")


for name, value in beast.items():
    print()
    print (f"{name:<15} : {value}")

    
