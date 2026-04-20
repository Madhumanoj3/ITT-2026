from datetime import datetime

ts1_str = input("Enter first timestamp (DD-MM-YYYY HH:MM:SS): ")
ts2_str = input("Enter second timestamp (DD-MM-YYYY HH:MM:SS): ")
date_format = "%d-%m-%Y %H:%M:%S"
try:
    dt1 = datetime.strptime(ts1_str, date_format)
    dt2 = datetime.strptime(ts2_str, date_format)
    diff = abs(int((dt2 - dt1).total_seconds()))
    print(f"Difference: {diff} seconds"
except ValueError:
    print("Error: Please ensure the date format is exactly DD-MM-YYYY HH:MM:SS")
