def process_conditions(curnt_balance, amount):

    if amount <= 0:
        raise ValueError("Amount must be a positive number greater than 0")
    if amount > curnt_balance:
        raise ValueError(f"Insufficient funds!, (your balance is only{curnt_balance}")
    return curnt_balance-amount

def simlt_atm():
    balance = 10000
    print("=== Welcome to the Python ATM ===")

    while True:
        print(f"Your Current Balance is: {balance} in Rupees")
        widr_exit = input("Enter withdrawal amount or type 'exit' to quit: ")
    
        if widr_exit.lower() == 'exit':
            yrn = input(f"Thank you for using our atm.")
            break
        
        try:
            amount = float(widr_exit)
            balance = process_conditions(balance, amount)   
            print(f" Withdrawal successful! Please collect your cash.")

        except ValueError as e:
            if "could not convert" in str(e):
                print("Error: Invalid input. Please enter a numeric value.")
            else:
                print(f"Error: {e}")

if __name__ == "__main__":
    simlt_atm()
