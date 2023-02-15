def calculateAbsolute():
    # This first line is provided for you
    in_num  = int(input("Enter a number: "))
    if in_num > 21:
        diff = abs(in_num - 21)*2
    else:
        diff = abs(in_num - 21)
    
    print(f"Result: {diff}")


## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()
