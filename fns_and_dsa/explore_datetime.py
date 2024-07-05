from datetime import datetime
def display_current_datetime():
    current_date = datetime.now()
    print(current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    future_date = datetime.now()
    no_days = input("Enter the number of days to add to the current date: ")
    future_date.timedelta(days = no_days)
    print(future_date.strftime("%Y-%m-%d"))
