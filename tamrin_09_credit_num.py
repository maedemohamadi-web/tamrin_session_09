from persian_tools.bank import card_number

def credit_num_info():
    credit_num=input("Enter the credit card number: ")
    if card_number.validate(credit_num):
        my_bank=card_number.bank_data(credit_num)
        return my_bank["name"]
    return None

print(credit_num_info())