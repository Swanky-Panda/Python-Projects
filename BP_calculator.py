from colorama import Fore

# INPUT
print(Fore.LIGHTWHITE_EX + "_________________________________________")
print("\n" * 0)
print("Please enter your SYS and DIA:")
print("\n" * 0)
sys = float(input("SYS: ".upper()))
dia = float(input("DIA: ".upper()))
print("\n" * 0)
print("_________________________________________" + Fore.RESET)

# _____________________________________________________________________________________________________________________

# OUTPUTS
print("\n" * 1)
if sys < 90 and dia < 60:
    print(Fore.LIGHTWHITE_EX + "You Have: ".upper() + Fore.CYAN + "Low Blood Pressure" + Fore.RESET)
elif 90 <= sys <= 119 and 60 <= dia <= 79:
    print(Fore.LIGHTWHITE_EX + "You Have: ".upper() + Fore.GREEN + "Normal Blood Pressure" + Fore.RESET)
elif 120 <= sys <= 129 and dia < 80:
    print(Fore.LIGHTWHITE_EX + "You Have: ".upper() + Fore.YELLOW + "Elevated Blood Pressure" + Fore.RESET)
elif 130 <= sys <= 139 or 80 <= dia <= 89:
    print(Fore.LIGHTWHITE_EX + "You Have: ".upper() + Fore.LIGHTYELLOW_EX + "Hypertension - Stage 1 Blood Pressure" + Fore.RESET)
elif 140 <= sys <= 180 or 90 <= dia <= 120:
    print(Fore.LIGHTWHITE_EX + "You Have: ".upper() + Fore.LIGHTRED_EX + "Hypertension - Stage 2 Blood Pressure" + Fore.RESET)
elif sys > 180 or dia > 120:
    print(Fore.LIGHTWHITE_EX + "You Have: ".upper() + Fore.RED + "Hypertension - Stage 3 Blood Pressure" + Fore.RESET)
else:
    print(Fore.WHITE + "BMI isn't within auto indexing parameters".upper() + Fore.RESET)

print("\n" * 1)
print(Fore.LIGHTWHITE_EX + "BP index (SYS|DIA):".upper())
print(Fore.WHITE + "Under 90 and Under 60 - Low")
print("90-119 and 60-79 - Normal")
print("120-129 and Under 80 - Elevated")
print("130-139 or 80-89 - Hypertension (Stage 1)")
print("140-180 or 90-120 - Hypertension (Stage 2)")
print("Over 180 or Over 120 - Hypertension (Stage 3)" + Fore.RESET)
print("\n" * 0)
print("_________________________________________" + Fore.RESET)

# _____________________________________________________________________________________________________________________
