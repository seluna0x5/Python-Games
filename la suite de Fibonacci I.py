nombres=int(input("Entrez la quantité de nombres à afficher :"))
a=0
b=1
total=0
print(f"les {nombres} premiers de suites de Fibonacci sont : ".format(nombres) , end=" ")
for i in range(nombres) :
    print(total , end=" ")
    a=b
    b=total
    total=a+b