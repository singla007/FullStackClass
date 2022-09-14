while True:
    try:
        input1 = int(input("Please input first number: "))
        input2 = int(input("Please input second number: "))
        
        if input2==0:
            print("Division is not possible with 0 in denominator, try again with some other value")
            continue
        
        print("Subtraction = ",input1-input2)
        print("Addition = ",input1+input2)
        print("Division = ",input1/input2)
        print("Multiplication = ",input1*input2)
        print("Power = ",input1**input2)
        
        if int(input("Press 0 to quit and any other number to continue: "))==0:
            break
    except:
        print("Please input correct datatype for mathematical functions")
