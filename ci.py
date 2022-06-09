p = float(input("Enter the principal amount : "))
 
t = float(input("Enter the number of years : "))
 
r = float(input("Enter the rate of interest : "))
 
# compound interest
a =  p * (pow((1 + r / 100), t)) 
ci=a -p
print("Compound interest : {}".format(ci))
print("total amount : {}".format(a))
