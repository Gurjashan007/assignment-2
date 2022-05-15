#Q6
def countthebits(n):
    count=0
    while n:
        n&=(n-1)
        return count
    def flipthecount(a,b):
        return countthebits(a^b)
    a=int(input("enter first number="))
    b=int(input("enter second number="))
    print(flipthecount(a,b))
