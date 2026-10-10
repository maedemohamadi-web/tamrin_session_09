from persian_tools import plate

def my_plate_data():
    car_plate_number=input("Enter car plate number: ")
    if plate.is_valid(car_plate_number):
        plate_province=plate.get_info(car_plate_number)
        return plate_province["province"]
    return None

print(my_plate_data())