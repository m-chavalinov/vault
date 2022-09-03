
premiere = 12.00
normal = 7.50
discount = 5.00

screening_type = input("What's the screening type?\n")
r = int(input("How many rows?\n"))
c = int(input("How many columns?\n"))

if screening_type == "premiere":
   price = premiere * (r*c)
   twochar = "{:.2f}".format(price)
   print(twochar + "\n leva")

elif screening_type == "normal":
    price = normal * (r*c)
    twochar = "{:.2f}".format(price)
    print(twochar + "\n leva")

elif screening_type == "discount":
    price = discount * (r*c)
    twochar = "{:.2f}".format(price)
    print(twochar + "\n leva")