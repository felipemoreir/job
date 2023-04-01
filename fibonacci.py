def fibonacci(num):
    if num== 0 or num==1:
           return true

    a,b = 0,1
    

    while b <= num:
        if b == num :
            return True
        a,b=b,a+b
    return False


num = int(input("digite o valor: "))

if fibonacci(num):
     print(f"{num} pertence a fibonacci")
else:
     print(f"{num} não pertence a fibonacci")
