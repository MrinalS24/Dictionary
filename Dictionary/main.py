location = ['21','Laan 1954','De Meern', 'Utrecht', 'Netherlands']

for item in location:
    print(item)
print()
sample_dictionary = {
    "house" : 21, 
    "street" : 'Laan 1954',
    "province" : 'De Meern',
    "city" : 'Utrecht',
    "country" : 'Netherlands'
}

print(sample_dictionary)
print()
print(sample_dictionary["city"])
print()
#print only keys
print(sample_dictionary.keys())
print()
# print all values
print(sample_dictionary.values())
print()

# for loop on dictionary
for key in sample_dictionary:
    print(key, sample_dictionary[key])
print()

for value in sample_dictionary.values():
    print(value)
print()

# add new key and value

student = {
    "name" : 'Mrinal',
    "age" : 13,
    "grade" : 8,
    "marks" : [8,7,6,8]
}

student["teacher"] = 'Ms. Sanne'

print (student)
print()

# check if key is presesnt

if "tree" in student:
    print('It exists')
else:
    print('Does not exist')


# modify value in key
student['grade'] = 9

print(student)

print()

# removing a value and key
del(student["name"])

print(student)

print()

print(student["marks"][2])

print()

# store multiple values in 1 key

students = {
    "Mrinal" : {
        "age" : 13,
        "grade" : 8,
        "marks" : [8,7,8,9],
        "teacher" : 'Ms. Rashmi'
    },
    "Aadya" : {
        "age" : 14,
        "grade" : 8,
        "marks" : [8,7,8,6],
        "teacher" : 'Ms. Rashmi'
    }
    
}

print(students)

print()

print(students["Aadya"])

print()

print(students["Mrinal"]["marks"][1])