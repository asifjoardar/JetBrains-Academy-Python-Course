import math
import random
import sqlite3
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS card (id INTEGER, number TEXT, pin TEXT, balance INTEGER);')
conn.commit()

def menu():
    print("1. Create an account\n2. Log into account\n0. Exit")

def menu1():
    print("1. Balance")
    print("2. Add income")
    print("3. Do transfer")
    print("4. Close account")
    print("5. Log out")
    print("0. Exit")

while True:
    menu()
    choice = int(input())
    print("")
    if choice == 1:
        #Issuer Identification Number (IIN)
        iin = 400000
        #customer account number (can)
        can = random.randint(000000000, 999999999)
        pin = random.randint(0000, 9999)
        #card number (cn)
        cn = str(iin) + str(can)
        #Luhn Algorithm in action
        genarate = []
        sum = 0
        for i in cn:
            genarate.append(int(i))
        for i in range(0,len(genarate)):
            if (i%2==0):
                genarate[i] *= 2
            if genarate[i]>9:
                genarate[i] -= 9
            sum += genarate[i]
        sum = 10*(math.ceil(sum/10)) - sum
        checksum = str(sum)
        cn += checksum
        print("Your card has been created\nYour card number:")
        print(cn)
        print("Your card PIN:")
        print(pin)
        print("")
        cur.execute(f'INSERT INTO card (id, number, pin, balance) VALUES ({400000}, {cn}, {pin}, {0})')
        conn.commit()
    elif choice == 2:
        print("Enter your card number:")
        check_cn = str(input())
        print("Enter your PIN:")
        check_pin = int(input())
        print("")
        cur.execute(f'SELECT * FROM card WHERE number = "%s" and pin = "%s"' % (check_cn, check_pin))
        conn.commit()
        if cur.fetchone() is not None:
            print("You have successfully logged in!")
            print("")
            while True:
                menu1()
                choice1 = int(input())
                cur.execute(f'SELECT balance FROM card WHERE number = {check_cn}')
                conn.commit()
                balance_print = cur.fetchone()[0]
                if choice1 == 1:
                    print('Balance: {}'.format(balance_print))
                    print("")
                elif choice1 == 2:
                    print('Enter income:')
                    money = int(input())
                    cur.execute(f'UPDATE card SET balance = balance + {money} WHERE number = {check_cn}')
                    conn.commit()
                    print('Income was added!\n')
                elif choice1 == 3:
                    print('Transfer')
                    print('Enter card number:')
                    trans_card = input()
                    #luhan in action
                    genarate = []
                    sum = 0
                    for i in trans_card:
                        genarate.append(int(i))
                    for i in range(0, len(genarate)-1):
                        if (i % 2 == 0):
                            genarate[i] *= 2
                        if genarate[i] > 9:
                            genarate[i] -= 9
                        sum += genarate[i]
                    sum = sum + genarate[len(genarate)-1]
                    checksum = (sum%10 == 0)
                    cur.execute(f'SELECT * FROM card WHERE number = "%s"' % (trans_card))
                    conn.commit()
                    d = cur.fetchone()
                    if trans_card == check_cn:
                        print("You can't transfer money to the same account!\n")
                    elif not checksum:
                        print('Probably you made mistake in the card number. Please try again!\n')
                    elif d is None:
                        print('Such a card does not exist.\n')
                    elif d is not None:
                        print('Enter how much money you want to transfer:')
                        trans_amount = int(input())
                        #cur.execute(f'SELECT balance FROM card WHERE number = {check_cn}')
                        #conn.commit()
                        #have = cur.fetchone()[0]
                        if balance_print < trans_amount:
                            print('Not enough money!')
                        else:
                            cur.execute(f'UPDATE card SET balance = balance + {trans_amount} WHERE number = {trans_card}')
                            conn.commit()
                            cur.execute(f'UPDATE card SET balance = balance - {trans_amount} WHERE number = {check_cn}')
                            conn.commit()
                            print('Success!')
                elif choice1 == 4:
                    cur.execute(f'DELETE FROM card WHERE number = {check_cn};')
                    conn.commit()
                    print('The account has been closed!\n')
                    break
                elif choice1 == 5:
                    print("You have successfully logged out!")
                    print("")
                    break
                else:
                    print("Bye!")
                    exit()
        else:
            print("Wrong card number or PIN!\n")
    else:
        print("Bye!")
        exit()
