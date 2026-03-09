first_name = "gilbert"
last_name = "mwangi"
full_name = first_name +" "+ last_name
print(full_name)
str_1 = "12345678"
str_2 = str_1[-1: :-1]
print(str_2)
regristration_number = "ENE211-0028/2025"
year_of_reg = regristration_number[-4:]
code = regristration_number[0:3]
admission_number = regristration_number[3:11]
student_details = f'Name: {full_name} RGN: {str_2} Year of Regristration: {year_of_reg} Student Code {code} ADM NO {admission_number} '
print(student_details)
