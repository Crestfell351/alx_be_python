from datetime import datetime
def display_current_datetime():
    current_date = datetime.now()
    print(current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    current_date = datetime.now()
    future_date =input("Enter the number of days to add to the current date: ")
    current_date.timedelta(days = future_date)
    print(current_date.strftime("%Y-%m-%d"))
