from datetime import datetime, timedelta

def display_current_datetime():
    """
    Get and display the current date and time.
    
    Returns:
        datetime: Current date and time object
    """
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date

def calculate_future_date(current_date):
    """
    Calculate a future date based on user input.
    
    Args:
        current_date (datetime): The current date to add days to
    
    Returns:
        datetime: Future date object
    """
    while True:
        try:
            days_to_add = int(input("Enter the number of days to add to the current date: "))
            if days_to_add < 0:
                print("Please enter a non-negative number.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")
    
    future_date = current_date + timedelta(days=days_to_add)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    return future_date

def main():
    """
    Main function to run the datetime exploration script.
    """
    try:
        # Part 1: Display current date and time
        current_date = display_current_datetime()
        
        # Part 2: Calculate future date
        future_date = calculate_future_date(current_date)
        
        # Additional information
        time_difference = future_date - current_date
        print(f"\nAdditional Information:")
        print(f"Days between dates: {time_difference.days}")
        print(f"Future date's weekday: {future_date.strftime('%A')}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()