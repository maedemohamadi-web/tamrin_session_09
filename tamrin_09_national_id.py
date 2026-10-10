from persian_tools import national_id

def my_national_id_info():
    my_id = input("Enter the National ID: ")
    if national_id.validate(my_id):
        place=national_id.find_place(my_id)
        return place["city"]
    return None

print(my_national_id_info())