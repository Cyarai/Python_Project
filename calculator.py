def calculator():

    print("""\n           ******** Calculator ********
          
          ------ Choose Operation ------

            Addition = +
            Substraction = -
            Multiplication = *
            Division = /
          
          """)

    try:    
        first = input('Enter the first input: ')
        second = input('Enter second input: ')
        operation = input('Enter operation (+, -, *, /): ')

        value_first = int(first)
        value_second = int(second)

        if operation == '+':
            print(f"Output: {value_first + value_second} ")
        elif operation == '-':
            print(f"Output: {value_first - value_second} ")
        elif operation == '*':
            print(f"Output: {value_first * value_second} ")
        elif operation == '/':
            if value_second == 0:
                print("Cannot be divide to 0")
            else:    
                print(f"Output: {value_first / value_second} ")

        else: 
            print('Invalid operation')

    except ValueError:
        print("Please Enter a valid number or operation")

def main():

    while True: 
        calculator()

        while True:
            calculate_again = input("Do you want to calculate again? (yes / no): ").lower()

            if calculate_again == "yes":
                break
            elif calculate_again == "no":
                print("\n         Thank you for calculating!          \n")
                return
            else:
                print("Try again please input yes or no only!")
            


main()
        
