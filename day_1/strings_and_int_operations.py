first_name = "gilbert"
last_name = "mwangi"
full_name = first_name +" "+ last_name
print(full_name)
str_1 = "12345678"
str_2 = str_1[-1: :-1]
print(  str_2)
regristration_number = "ENE211-0028/2025"
year_of_reg = regristration_number[-4:]
code = regristration_number[0:3]
admission_number = regristration_number[3:11]
student_details = f'Name: {full_name} RGN: {str_2} Year of Regristration: {year_of_reg} Student Code {code} ADM NO {admission_number} '
print(student_details)
int_1 = 39
int_2 = 7
int_add = 0
int_add += int_1 + int_2
int_sub = int_1 - int_2
int_multiplication = int_1 * int_2
int_div = int_1 / int_2
int_rounded = round(int_div, 2)
print("integer 1:", int_1 ,"integer 2:", int_2 , 'addition:',int_add ,"subtraction:" , int_sub ,"multiplication:", int_multiplication ,'division:', int_div ,'rounding of:', int_rounded)
