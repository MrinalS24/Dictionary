Employees = {
    'Mrinal' : {
        'age' : 29,
        'department' : 'Medicine',
        'salary' : 100000
    },
    'Aadya' : {
        'age' : 31,
        'department' : 'Finance',
        'salary' : 85000
    },
    'Saimeera' : {
        'age' : 30,
        'department' : 'Law',
        'salary' : 70000
    }
}

print(Employees)
print()


Employees['Shreya'] = {
    'age' : 30,
    'department' : 'Management',
    'salary' : 45000
}

print(Employees)
print()


REmploy = input('Which employees data would you like to see?  ')
print(Employees[REmploy])
print()


UEmploy = input('Which emplyees salary would you like to update?  ')
Employees[UEmploy] ['salary'] += 5000
print(Employees[UEmploy])
print()


DEmploy = input('Which employee would you like to remove?  ')
del(Employees[DEmploy])
print(Employees)
print()


"""for key in Employees.values():
    print(Employees['department'])"""

for key in Employees:
    print(key, Employees[key]['department'])