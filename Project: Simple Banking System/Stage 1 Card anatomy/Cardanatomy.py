import random
count = 0
user_info = {}
while True:
    print("1. Create an account\n2. Log into account\n0. Exit")
    choice = int(input())
    print("")
    if choice == 1:
        #Issuer Identification Number (IIN)
        random.seed(count)
        iin = random.randint(400000, 400000)
        #customer account number (can)
        random.seed(count)
        can = random.randint(0000000000, 9999999999)
        random.seed(count)
        pin = random.randint(0000, 9999)
        #card number (cn)
        cn = str(iin) + str(can)
        user_info[cn] = {}
        user_info[cn]['pin'] = pin
        user_info[cn]['balance'] = 0
        print("Your card has been created\nYour card number:")
        print(cn)
        print("Your card PIN:")
        print(pin)
        print("")
        count += 1
    elif choice == 2:
        print("Enter your card number:")
        check_cn = str(input())
        print("Enter your PIN:")
        check_pin = int(input())
        print("")
        try:
            if (user_info[check_cn]['pin'] == check_pin):
                print("You have successfully logged in!")
                print("")
                while True:
                    print("1. Balance\n2. Log out\n0. Exit""")
                    print("")
                    choice1 = int(input())
                    if choice1 == 1:
                        print("Balance: {}".format(user_info[check_cn]['balance']))
                        print("")
                    elif choice1 == 2:
                        print("You have successfully logged out!")
                        print("")
                        break
                    else:
                        print("Bye!")
                        exit()
        except KeyError:
            print("Wrong card number or PIN!")
            print("")
        else:
            print("Wrong card number or PIN!")
            print("")
    else:
        print("Bye!")
        exit()
