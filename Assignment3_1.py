hrs  = input("How many hours do you work?")
h = float(hrs)
rate = input("What is the rate per hour")
r = float(rate)
# upto 40 , rate = 10.50
# over 40 , rate = 15.75
if (h>40):
    excess = h-40
    e = float(excess)
    #excess x (10.50 * 1.50) + 40 * normal rate.
    income = (e * (r * 1.50)) + (40 * r)
    print(income)
elif (h <= 40) :
    income = (h * r)
    print (income)
