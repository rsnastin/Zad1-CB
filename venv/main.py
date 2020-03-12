import datetime
print('Wybor programu\n1.Zadanie temperatura\n2.Zadanie kalendarz "wersje krotka"\n3.Zadanie kalenarz "wersja dluga" ')
menu=int(input("Wybor: "))
if(menu==1):
    temperature = input("Podaj wartosc temperatury:")
    unit = input("Podaj jednostke C/F:")
    if(unit == "C"):
        temperature = (int(temperature) * 9/5)+32
        print(str(temperature) + "F")
    elif(unit == "F"):
        temperature = (int(temperature)-32)*5/9
        print(str(temperature)+ "C")
if(menu==2):
    year = int(input("Rok: "))
    month = int(input("Miesiac: "))
    day = int(input("Dzien: "))
    date = datetime.date(year, month, day)
    print("D:"+str(date.day)+" M"+str(date.month)+" Y:"+str(date.year))
    for i in range(10):
        date =date + datetime.timedelta(days=1)
        print("D:"+str(date.day)+" M"+str(date.month)+" Y:"+str(date.year))
if(menu==3):
    year = int(input("Rok: "))
    month = int(input("Miesiac: "))
    day = int(input("Dzien: "))
    sumDays= 0;
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        leap = 29
    else:
        leap = 28
    year_struct = [31, leap, 31, 30,31,30,31,31,30,31,30,31]

    for x in range(month):
        sumDays+=int(year_struct[x])

    sumDays-=int(year_struct[month-1])
    sumDays+=int(day)

    if(leap == 29):
        print("W tym roku minelo " +str(sumDays)+" dni, jest to rok przestepny")
    if(leap == 28):
        print("W tym roku minelo " +str(sumDays)+" dni, nie jest to rok przestepny")

    for y in range(10):
        day+=1
        if(day>year_struct[month-1]):
            day=1
            if(year_struct[11]):
                month=1
                year+=1
            else:
                month+=1
        print("D:" +str(day)+" M:"+str(month)+" Y:"+str(year))
