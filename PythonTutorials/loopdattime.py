for i in range(1,2):
    print(i)




import datetime


d = datetime.date(2016,7,24)
print(d)


#Time Delta number of days

delta = datetime.timedelta(days=7)

print(d+delta)

#Date fomr a date

bday = datetime.date(2016,9,24)

till_bday = bday -d

print(till_bday.total_seconds())


#Date time 

t = datetime.time(9,30,45,10000)

print(t)


print(datetime.datetime.today())

print(f"The date time is {t}")


#to conver strftime
#to conver string to date datetime.datetime.strptime(str,'%B %d,T)

str = 'July 26, 2016'