import phonenumbers
from phonenumbers import carrier,timezone,geocoder
from time import sleep
import asyncio
from truecallerpy import search_phonenumber

print("Number Information")
print("	")
print("1. Phone Information")
print("2. Phone Sms Bomber")
print("3. Phone JSON Format")
print("	")
print("What Is Your Change? `1 2 or 3`")
ch=input(">>> ")

if ch == "1" :
   number = input("Telefon Numarasını  Gir  `+90 Olmadan' ")
   number =  "+90" + number
   Numara = phonenumbers.parse(number)
   zaman = timezone.time_zones_for_number(Numara)
   sim_adi = carrier.name_for_number(Numara, "tr")
   bolge = geocoder.description_for_number(Numara, "tr")
   print("Saat Dilimi :", zaman)
   print("Sim adı:", sim_adi)
   print("Yaşadığı Ülke(bölge) :", bolge)
if ch == "2":
   import enough
   
if ch == "3":
   number = input("Telefon Numarasını  Gir '90 Olacak Sekilde + Olmayacak' ")
   number =  "+90" + number
   country_code = "TR"
   installation_id = "a1i0C--gqXfNFFY-Eko32vIlZ2D7Iio_4rM1dFeGWi7talDi7Jv-wNLq76tYh9DD"
   response = asyncio.run(search_phonenumber(number, country_code, installation_id))
   print(response)
