
def deposit():
    while True:
        amount = input("What would you like to deposit? $")

        if amount.isdigit():
            amount = int(amount)
            
            if amount > 10:
                break

            else:
                print("Amount must be greater than 10.")

        else: 
            print("Please enter a number.")
    
    return amount

def main():
    balance = deposit()