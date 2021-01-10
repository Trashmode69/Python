print("Now we will calculate your marketing:\n\nprice:\n------\nTomato= 3 NIS\nCucumber= 2 NIS\nCola= 5 NIS\nChiken= 20 NIS\n ")
Tomatos=int(input("Enter how many Tomatos? "))
Cucumbers=int(input("Enter how many Cucumbers? "))
Colas=int(input("Enter how many Colas? "))
Chickens=int(input("Enter how many Chikens? "))
print("---------------------------")

print("Sammary of your order:\n\nTomatos: " + str(Tomatos) + "\nCucumbers: " + str(Cucumbers) + "\nColas: " + str(Colas) + "\nChickens: " + str(Chickens))
Summary=(Tomatos*3)+(Cucumbers*2)+(Colas*5)+(Chickens*20)
print("\nYou have to pay: " + str(Summary) + " NIS without tax")
print("\nYou have to pay: " + str("%.2f" % (Summary*1.17)) + " NIS with tax")

print("------------------------------------")