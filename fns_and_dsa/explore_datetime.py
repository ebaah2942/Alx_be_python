from datetime import datetime, timedelta, date

def display_current_datetime():
    current_date_new = datetime.now()
    formated_date_new = current_date_new.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formated_date_new}")

display_current_datetime()



def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    current_date = date.today()
    future_date = current_date + timedelta(days=number_of_days)
    formated_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formated_date}")



if __name__ == "__main__":
    calculate_future_date()


    






