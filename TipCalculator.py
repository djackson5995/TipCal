def calculating_bill():
    """Welcome message"""
    print("Welcome to the Tipping Assistant Calculator")

    # Asking what the bill amount and tip should be.
    bill = float(input("What is your total bill? "))
    tip_amount = float(input("How much would you like to tip? 10%, 15%, 20%, etc.: "))

    # Calculations for bill and the amount of people splitting it.
    ppl_splitting_bill = int(input("How many people are splitting the bill? "))
    total_amount_plus_tip = bill + tip_amount
    amount_per_person = total_amount_plus_tip / ppl_splitting_bill

    print(f"Each person pays ${amount_per_person:.2f}")


# Call the function to run the program
calculating_bill()
