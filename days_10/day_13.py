import random


def select_random_element(ele_dict):
    name, n = random.choice(list(ele_dict.items()))
    abbreviation, num = n
    return name, abbreviation, num


def play_game(ele):
    p = 0
    name, abb, num = ele
    in_abb = input(f"Enter the correct abbreviation for {name}: ").title()
    in_num = int(input(f"Enter the correct atomic number for {name}: "))
    if abb == in_abb:
        print("Correct Abbreviation")
        p += 1
    else:
        print("Incorrect Abbreviation")
    if num == in_num:
        print("Correct Atomic Number")
        p += 1
    else:
        print("Incorrect Atomic Number")
    return p


elements = {"Aluminum": ["Al", 13], "Argon": ["Ar", 18], "Barium": ["Ba", 56], "Beryllium": ["Be", 4],
            "Boron": ["B", 5], "Bromine": ["Br", 35], "Cadmium": ["Cd", 48], "Calcium": ["Ca", 20],
            "Carbon": ["C", 6], "Chlorine": ["Cl", 17], "Chromium": ["Cr", 24], "Copper": ["Cu", 29],
            "Fluorine": ["F", 9], "Gold": ["Au", 79], "Helium": ["He", 2], "Hydrogen": ["H", 1],
            "Iodine": ["I", 53], "Iron": ["Fe", 26], "Lead": ["Pb", 82], "Lithium": ["Li", 3],
            "Magnesium": ["Mg", 12], "Manganese": ["Mn", 25], "Mercury": ["Hg", 80], "Neon": ["Ne", 10],
            "Nickel": ["Ni", 28], "Nitrogen": ["N", 7], "Oxygen": ["O", 8], "Phosphorus": ["P", 15],
            "Platinum": ["Pt", 78], "Potassium": ["K", 19], "Silicon": ["Si", 14], "Silver": ["Ag", 47],
            "Sodium": ["Na", 11], "Strontium": ["Sr", 38], "Sulfur": ["S", 16], "Tin": ["Sn", 50],
            "Uranium": ["U", 92], "Xenon": ["Xe", 54], "Zinc": ["Zn", 30]}

score = 0
correct = True

while correct:
    random_element = select_random_element(elements)
    points = play_game(random_element)
    if points == 0:
        correct = False
        print(f"Game over! Final Score: {score}")
    else:
        score = score + points
        print(f"Score: {score}")
