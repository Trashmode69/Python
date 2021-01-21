choice=input("Menu:\n-----\n1.Insert Number and ** it by 3\n2.Insert 4 IPs to a list and print it\n3.insert 4 Entries to DNS_Dictionary and print it\n4.Chek if a string is Polindrom\n")
if(choice=="1"):
    print("The new number is: " + str((int(input("Enter a number: ")))**3))
elif(choice == "2"):
    list_ip=[]
    list_ip.append(input("Enter new IP: "))
    list_ip.append(input("Enter new IP: "))
    list_ip.append(input("Enter new IP: "))
    list_ip.append(input("Enter new IP: "))
    print("The new list:\n-------------" + str(list_ip))
elif(choice =="3"):
    dns_dict={}
    dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
    dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
    dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
    dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
    print("The new dns_dict:\n----------------" + str(dns_dict))
elif(choice == "4"):
    word=input("Enter a word: ")
    if(word==word[::-1]):
        print("This is Polindrom")
    else:
        print("This isn't Polindrom")
else:
    print("Enter 1-4 only!!!")