import os

print("1  ,shutdown system fori")
print("2 , shutdown system be sorat zamndar")
print("3,restar system fori")
print("4 , restar system be sorat zamndar")
print("5,exit")
print(end="zaman ro vared konid : ")

choice = int(input())

if choice == 1:
    os.system("shutdown /s /t 0 ")
elif choice == 2:
    print(end=" zamanet ro vared kon :")
    sec = int(input())
    str_1 = "shutdown /s /t "
    str_2 = str(sec)
    str = str_1 + str_2
    os.system(str)
elif choice == 3:
    os.system("shutdown /r /t 0")
elif choice == 4:
    print(end=" zamanet ro vkonid : ")
    sec = int(input())
    str1 = "shutdown /r /t"
    str2 = str(sec)
    str = str1 + str2
    os.system(str)
elif choice == 5:
    exit()
else:
    print("wrong !!!!!!!!!!!!")
