a=int(input("Please enter the lenht of side 1 :"))
b=int(input("Please enter the lenght of side 2 :"))
c=int(input("Please enter the lenght of side 3 :"))
while ((a+b)>c) and ((a+b)>b) and ((b+c)>a):
    print("Yes")
    break
while ((a+b)<c) or ((a+c)>b) or ((b+c)>a):
    print("No")
    break