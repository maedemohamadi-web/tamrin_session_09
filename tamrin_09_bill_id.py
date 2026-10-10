from persian_tools import bill

def my_bill_info():
    the_barcode=input("Enter Barcode: ")
    information = bill.get_detail(barcode=the_barcode)
    if information is not None and information["is_valid"]:
        return information
    return None

print(my_bill_info())