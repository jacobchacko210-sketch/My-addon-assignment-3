def validate_booking(requested, available):
    if requested <= 0:
        raise Exception("Invalid request: You must book at least 1 ticket.")
    if requested > available:
        raise Exception(f"Booking failed: Only {available} seats remaining.")
    return True

def start_booking():
    total_seats = 50
    TICKET_PRICE = 180

    print("--- Cinema Ticket Booking System ---")
    print(f"Standard Price: ₹{TICKET_PRICE} per seat")

    while total_seats > 0:
        print(f"\nRemaining Seats: {total_seats}")
        user_input = input("How many tickets? (or 'q' to quit): ")

        if user_input.lower() == 'q':
            break

        try:
            num_tickets = int(user_input)

            if validate_booking(num_tickets, total_seats):
                cost = num_tickets * TICKET_PRICE
                total_seats -= num_tickets
                
                print("-" * 30)
                print(f"✅ Success! {num_tickets} tickets booked.")
                print(f"💰 Total Amount: ₹{cost}")
                print("-" * 30)

        except ValueError:
            print("❌ Error: Please enter a whole number (e.g., 2, 5).")
            
        except Exception as e:
            print(f"❌ {e}")

    print("\n" + "="*30)
    print(f"Final Report")
    print(f"Remaining Seats: {total_seats}")
    print("="*30)

if __name__ == "__main__":
    start_booking()