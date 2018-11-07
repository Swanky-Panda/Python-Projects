from colorama import Fore

# INPUT
print(Fore.WHITE + "_________________________________________")
print('\n' * 0)
print("Please enter your height and weight:")
print('\n' * 0)
height = float(input("Height(in): ".upper()))
weight = float(input("Weight(lb): ".upper()))
print('\n' * 0)
print("_________________________________________" + Fore.RESET)

# CALCULATIONS
bmi = (weight * 0.45) / (height * 0.025) ** 2
bmi = float("%.2f" % bmi)

# OUTPUTS
print('\n' * 1)
if bmi < 18:
    desired = ((((0.025 * height) ** 2) * 18.5) / 0.45) - weight
    desired = str("%.2f" % desired) + " Pounds"
    print(Fore.WHITE + "You Are: ".upper() + Fore.YELLOW + "Underweight" + Fore.RESET)
    print('\n' * 1)
    print(Fore.WHITE + "You Need to Gain: ".upper() + Fore.BLUE + desired + Fore.RESET)
elif 18.5 <= bmi <= 24.9:
    print(Fore.WHITE + "You Are: ".upper() + Fore.GREEN + "Normal" + Fore.RESET)
    print('\n' * 1)
    print(Fore.WHITE + "You Need to Lose: ".upper() + Fore.BLUE + "0 Pounds" + Fore.RESET)
elif 25 <= bmi <= 29.9:
    desired = weight - ((((0.025 * height) ** 2) * 24.9) / 0.45)
    desired = str("%.2f" % desired) + " Pounds"
    print(Fore.WHITE + "You Are: ".upper() + Fore.LIGHTRED_EX + "Overweight" + Fore.RESET)
    print('\n' * 1)
    print(Fore.WHITE + "You Need to Lose: ".upper() + Fore.BLUE + desired + Fore.RESET)
elif bmi > 30:
    desired = weight - ((((0.025 * height) ** 2) * 24.9) / 0.45)
    desired = str("%.2f" % desired) + " Pounds"
    print(Fore.WHITE + "You Are: ".upper() + Fore.RED + "Obese" + Fore.RESET)
    print('\n' * 1)
    print(Fore.WHITE + "You Need to Lose: ".upper() + Fore.BLUE + desired + Fore.RESET)
else:
    print(Fore.WHITE + "BMI isn't within auto indexing parameters".upper() + Fore.RESET)
print('\n' * 1)
print(Fore.WHITE + "BMI: ".upper() + Fore.WHITE + str(bmi) + Fore.RESET)
print('\n' * 1)
print(Fore.WHITE + "BMI index:".upper())
print(Fore.WHITE + "Under 18 - Underweight")
print("18.5 to 24.9 - Normal")
print("25 to 29.9 - Overweight")
print("Over 30 - Obese" + Fore.RESET)
print('\n' * 0)
print("_________________________________________" + Fore.RESET)