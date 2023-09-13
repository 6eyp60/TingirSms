import asyncio
from truecallerpy import search_phonenumber

phone_number = "+1234567890"
country_code = "US"
installation_id = "a1i0C--gqXfNFFY-Eko32vIlZ2D7Iio_4rM1dFeGWi7talDi7Jv-wNLq76tYh9DD"

response = asyncio.run(search_phonenumber(phone_number, country_code, installation_id))
print(response)
