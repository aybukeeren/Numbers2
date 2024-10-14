'''
0. exit
1. append
2. calculate total
enter choice : '''

from Numbers import Numbers
print("0. exit\n"+"1. append\n"+"2. calculate total")
choice = int(input("Enter choice :"))

while choice != 0:
    if choice == 1:
        number = int(input("Enter your number =>"))
        select1 = Numbers(number)
        print(select1.__str__())
    elif choice == 2:
        print(Numbers.total_list())
    else:
        print("Wrong entered !!")
    choice = int(input("Enter choice :"))
    