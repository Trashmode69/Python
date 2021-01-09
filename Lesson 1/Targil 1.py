num = int(input("Enter a number with 4 digits"))

# This is Alafim
print("Alafim=" + str(num // 1000))

# Tihs is Meot
print("Meot=" + str((num // 100) % 10))

# This si Asarot
print("Asarot=" + str((num % 100) // 10))

# This is Ahadot
print("Ahadot=" + str(num % 10))
