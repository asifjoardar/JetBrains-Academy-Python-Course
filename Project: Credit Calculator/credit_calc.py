import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal",type=float)
parser.add_argument("--payment",type=float)
parser.add_argument("--periods",type=int)
parser.add_argument("--interest",type=float)

args = parser.parse_args()

def msg():
    print("Incorrect parameters.")

if args.type=="diff" and args.principal and args.periods and args.interest:
    p = args.principal
    n = args.periods
    i = (args.interest/100.0)/12.0
    sum = 0.0
    ans = []
    for j in range(0,n):
        x = p - ((p * float(j))/float(n))
        df = (p/n) + ( i * x )
        df = math.ceil(df)
        sum += df
        ans.append(df)
    if((sum-p)>=0):
        for j in range(0,n):
            print("Month {}: paid out {}".format(j+1,ans[j]))
        print("")
        print("Overpayment = ", int(sum - p))
    else:
        msg()

elif args.type=="annuity":
    if(args.principal and args.payment and args.interest):
        cp = args.principal
        mp = args.payment
        ci = args.interest

        i = (ci / 100) / 12
        n = math.log((mp / (mp - i * cp)), (1.0 + i))
        n = math.ceil(n)
        yr = int(n // 12)
        mnth = int(n) % 12
        if (yr == 0):
            print("You need {} months to repay this credit!".format(mnth))
        elif (mnth == 0):
            print("You need {} years to repay this credit!".format(yr))
        else:
            print("You need {} years and {} months to repay this credit!".format(yr,mnth))

        print("Overpayment = ",int((n*mp)-cp))

    elif(args.principal and args.periods and args.interest):
        cp = args.principal
        n = args.periods
        ci = args.interest
        i = (ci / 100) / 12
        a = cp * ((i * math.pow((i + 1), n)) / (math.pow((i + 1), n) - 1))
        print("Your annuity payment = {}!".format(int(math.ceil(a))))
        print("Overpayment = ", int((n * int(math.ceil(a))) - cp))

    elif(args.payment and args.periods and args.interest):
        mp = args.payment
        n = args.periods
        ci = args.interest
        i = (ci / 100) / 12
        cp = mp / (((i * math.pow((i + 1), n)) / (math.pow((i + 1), n) - 1)))
        print("Your credit principal = {}!".format(int(cp)))
        print("Overpayment = ", int((n * mp) - int(cp)))
    else:
        msg()

else:
    msg()
