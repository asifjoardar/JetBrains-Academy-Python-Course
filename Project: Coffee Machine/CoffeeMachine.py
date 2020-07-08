class Coffeemachine:
    #constractor
    def __init__(self, waterase, milkase, beansase, cupase, moneyase):
        self.waterase = waterase
        self.milkase = milkase
        self.beansase = beansase
        self.cupase = cupase
        self.moneyase = moneyase

    #check remaining
    def rem(self):
        print("The coffee machine has:")
        print(self.waterase, " of water")
        print(self.milkase, " of milk")
        print(self.beansase, " of coffee beans")
        print(self.cupase, " of disposable cups")
        if (self.moneyase > 0):
            print("$", self.moneyase, " of money")
        else:
            print(self.moneyase, " of money")
    #take money
    def take(self):
        print("I gave you $", self.moneyase)
        self.moneyase = 0
    #fill the machine
    def fill(self):
        print("Write how many ml of water do you want to add:")
        num = int(input())
        self.waterase += num
        print("Write how many ml of milk do you want to add:")
        num = int(input())
        self.milkase += num
        print("Write how many grams of coffee beans do you want to add:")
        num = int(input())
        self.beansase += num
        print("Write how many disposable cups of coffee do you want to add:")
        num = int(input())
        self.cupase += num
    #buy something
    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        dec = str(input())
        if (dec == "back"):
            pass
        elif (dec == "3"):
            if (self.waterase >= 200 and self.milkase >= 100 and self.beansase >= 12 and self.cupase >= 1):
                print("I have enough resources, making you a coffee!")
                self.waterase -= 200
                self.milkase -= 100
                self.beansase -= 12
                self.moneyase += 6
                self.cupase -= 1
            else:
                print("Sorry, not enough water!")
        elif (dec == "2"):
            if (self.waterase >= 350 and self.milkase >= 75 and self.beansase >= 20 and self.cupase >= 1):
                print("I have enough resources, making you a coffee!")
                self.waterase -= 350
                self.milkase -= 75
                self.beansase -= 20
                self.moneyase += 7
                self.cupase -= 1
            else:
                print("Sorry, not enough water!")
        else:
            if (self.waterase >= 250 and self.beansase >= 16 and self.cupase >= 1):
                print("I have enough resources, making you a coffee!")
                self.waterase -= 250
                self.beansase -= 16
                self.moneyase += 4
                self.cupase -= 1
            else:
                print("Sorry, not enough water!")



cm = Coffeemachine(400, 540, 120, 9, 550)
while True:
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    if (action == "exit"):
        break
    elif (action == "remaining"):
        print("")
        cm.rem()
        print("")
    elif (action == "take"):
        print("")
        cm.take()
        print("")
    elif (action == "fill"):
        print("")
        cm.fill()
        print("")
    else:
        print("")
        cm.buy()
        print("")
