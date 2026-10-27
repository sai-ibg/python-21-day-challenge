first_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")

age=input("Enter your age: ")

first_name_upper=first_name.upper()
last_name_upper=last_name.upper()

first_name_without_space=first_name.replace(" ","")
last_name_without_space=last_name.replace(" ","")

patent_id=f"{first_name_upper[0]}{last_name_upper[0]}-{age}"

print(patent_id)

