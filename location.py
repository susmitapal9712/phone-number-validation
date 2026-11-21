import phonenumbers
from phonenumbers import geocoder,carrier

number=input("enter phonenumber with country code (e.g.+915654356906)")

try:
    phone_number=phonenumbers.parse(number)

    print("valid number:", phonenumbers.is_valid_number(phone_number))
    print("country/region:", geocoder.description_for_number(phone_number,"en"))
    print("carrier:",carrier.name_for_number(phone_number,"en"))

except Exception:
     print("invalid phone number!")          