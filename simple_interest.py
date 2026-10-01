def calculate_simple_interest(principal: float, rate: float, time: float) -> float:
    """
    Calculate Simple Interest using the formula: SI = (P * R * T) / 100
    """
    return (principal * rate * time) / 100

def main():
    print("=== Simple Interest Calculator ===")
    try:
        principal = float(input("Enter Principal amount (P): "))
        rate = float(input("Enter Rate of interest per year (%): "))
        time = float(input("Enter Time in years (T): "))

        interest = calculate_simple_interest(principal, rate, time)
        total_amount = principal + interest

        print("\n--- Calculation Results ---")
        print(f"Principal Amount: ${principal:,.2f}")
        print(f"Interest Rate:    {rate:.2f}% per year")
        print(f"Time Period:      {time:.2f} years")
        print(f"Simple Interest:  ${interest:,.2f}")
        print(f"Total Amount:     ${total_amount:,.2f}")

    except ValueError:
        print("Error: Please enter valid numerical values.")

if __name__ == "__main__":
    main()
