details_list = ["David Gerasim", 27, "David@gmail.com", "123456789"]
print("Full name: " + details_list[0] + "\nAge: " + str(details_list[1]) + "\nMail: " + details_list[2] + "\nPhone: " +
      details_list[3])
ip_list = ["1.1.1.1", "2.2.2.2"]
print(ip_list)

# פקודה זו מוסיפה אל הרשימה את המבוקש
ip_list.append("3.3.3.3")
ip_list.append("4.4.4.4")
ip_list.append("5.5.5.5")
print(ip_list)

# פקודה זו מוציאה את המבוקש מן הרשימה
ip_list.pop(2)
print("ip list length is: " + str(len(ip_list)) + "\nand the ip list: " + str(ip_list))
