print('This program will convert miles to kilometers or the other way round')

miles = input('Enter distance in miles: ')
km = input('Enter distance in kilometers: ')

if miles =="":
    miles = 0

if km == "":
    km = 0

if int(miles) == 0:
    distance = int(km) / 1.6
    print(f"{km} kilometers are {distance} miles")

if int(km) == 0:
    distance = int(miles) * 1.6
    print(f"{miles} miles are {distance} kilometers")

