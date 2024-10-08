'''
Author: Nandana Hasheed
Date: 08-10-2024
python program to extract first name
version 1.0
'''
first_name=input("Enter your first name :")
last_name=input(" Enter your last name :")
full_name=first_name+" "+last_name
print(full_name)
length=len(first_name)
print(length)
extracted_last_name=full_name[:length]
print(extracted_last_name)