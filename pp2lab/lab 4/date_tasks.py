#1 Write a Python program to subtract five days from current date.
from datetime import datetime
today = datetime.today()
newdate = datetime.fromtimestamp(today.timestamp() - 5 * 86400)
print("Five day ago:",newdate.strftime("%Y-%m-%d"))

#2 Write a Python program to print yesterday, today, tomorrow.
yesterday = datetime.fromtimestamp(today.timestamp()-86400)
today = datetime.today()
tomorrow = datetime.fromtimestamp(today.timestamp()+86400)
print('Yesterday:',yesterday.strftime("%Y-%m-%d"))
print('Today:',today.strftime("%Y-%m-%d"))
print('Tomorrow:',tomorrow.strftime("%Y-%m-%d"))

#3 Write a Python program to drop microseconds from datetime.
now = datetime.now()
without_microsecond = now.replace(microsecond=0)
print(without_microsecond)


#4 Write a Python program to calculate two date difference in seconds.
y = int(input("Enter the first year: "));y1 = int(input("Enter the second year: "))
m = int(input("Enter the first month: "));m1 = int(input("Enter the second month: "))
d = int(input("Enter the first day: "));d1 = int(input("Enter the second day: "))
h = int(input("Enter the first hour: "));h1 = int(input("Enter the second hour: "))
min = int(input("Enter the first minute: "));min1 = int(input("Enter the second minute: "))
sec = int(input("Enter the first second: "));sec1 = int(input("Enter the second second: "))
first_date = datetime(y,m,d,h,min,sec)
print(first_date)
second_date = datetime(y1,m1,d1,h1,min1,sec1)
print(second_date)
diff = (second_date-first_date).total_seconds()
print(int(diff))