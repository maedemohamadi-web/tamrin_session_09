from persian_tools import phone_number

def phone_number_info():
    my_phone_number=input("Enter your phone number: ")
    if phone_number.validate(my_phone_number):
        phone_province=phone_number.operator_data(my_phone_number)
        return phone_province["province"]
    else:
        print("Invalid phone number")
    return None

print(phone_number_info())