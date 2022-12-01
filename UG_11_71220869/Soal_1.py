print("Select operation.")
print("1. add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
opsi = input("Enter choice (1/2/3/4): ")

if opsi == '1':
    a1 = float(input("Enter first number : "))
    a2 = float(input("Enter second number : ")) 
    def add():
        tmbah = float(a1 + a2)
        print (a1, "+", a2, "=", tmbah)
    add()

elif opsi == '2':
    a3 = float(input("Enter first number : "))
    a4 = float(input("Enter second number : ")) 
    def subtract():
        krg = float(a3 - a4)
        print (a3, "-", a4, "=", krg)
    subtract()

elif opsi == '3':
    a5 = float(input("Enter first number : "))
    a6 = float(input("Enter second number : ")) 
    def multiply():
        bagi = float(a5 * a6)
        print (a5, "*", a6, "=", bagi)
    multiply()

elif opsi == '4':
    a7 = float(input("Enter first number : "))
    a8 = float(input("Enter second number : ")) 
    def divide():
        kali = float(a7 / a8)
        print (a7, ":", a8, "=", kali)
    divide()
else :
    print("error")

    


    