nombres=int(input("Entrez la quantité de nombres à afficher :"))
def Fibonacci(n) :
    if n<=1 :
        return n
    else :
        return Fibonacci(n-2)+Fibonacci(n-1)
print(f"les {nombres} premiers de suites de Fibonacci sont : ".format(nombres) , end=" ")
for i in range(nombres) :
    print(Fibonacci(i),end=" ")