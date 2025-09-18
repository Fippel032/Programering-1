import datetime
import requests

DIS = 0.2
DAY_FARE = 5
TAX = 1.25

print("Vilket år?")
year = int(input())

print("Månad?")
month = int(input())

print("Dag?")
day = int(input())

print("Slut år?")
endyear = int(input())

print("Slut månad?")
endmonth = int(input())

print("Slut dag?")
endday = int(input())

response = ""

if endmonth < 10 and endday >= 10:
    response = requests.get(f'https://www.elprisetjustnu.se/api/v1/prices/{endyear}/0{endmonth}-{endday}_SE2.json')
elif endmonth >= 10 and endday < 10:
    response = requests.get(f'https://www.elprisetjustnu.se/api/v1/prices/{endyear}/{endmonth}-0{endday}_SE2.json')
elif endmonth < 10 and endday < 10:
    response = requests.get(f'https://www.elprisetjustnu.se/api/v1/prices/{endyear}/0{endmonth}-0{endday}_SE2.json')
else:
    response = requests.get(f'https://www.elprisetjustnu.se/api/v1/prices/{endyear}/{endmonth}-{endday}_SE2.json')




data = response.json()
kwh_price = float(data[0]["SEK_per_kWh"])
print(data)

start_date = datetime.datetime(year, month, day)
end_date = datetime.datetime(endyear, endmonth, endday)
date_diff = end_date - start_date

print("Hur många kwh har du använt?")
kwh=float(input())

days = date_diff.days
calculation = days * DAY_FARE
calculation2 =kwh_price * kwh * TAX
calc=calculation+calculation2
print(round(calc, 2), "kr")

print("Har du solceller? För då kan du få rabatt")
has_solar = input()

if has_solar == "ja":
    discount = calc * DIS
    print("Du får", round(discount, 2), "kr rabatt")
    print("Slutpris är", round(calc - discount, 2), "kr")
else:
    print("Ditt pris är", calc, "kr")

    