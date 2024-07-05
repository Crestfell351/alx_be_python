from datetime import datetime
def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date.year}-{current_date.month}-{current_date.day} {current_date.hour}:{current_date.minute}:{current_date.second}:")

def calculate_future_date():
    current_date = datetime.now()
    future_date =input("Enter the number of days to add to the current date: ")
    current_date.timedelta(days = future_date)
    print(f"Future date: {current_date.year}-{current_date.month}-{current_date.day}")
