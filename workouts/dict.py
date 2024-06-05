details = {
    'name': 'nidal',
    'age': 13,
    'school': 'pkv'
}

print(details)
print(details['age'])

details['school'] = 'THSS'

print(details)
print(details.keys())
print(details.values())


school = {
    'student1': {
        'name': 'farzan',
        'age': 18
    },
    'student2': {
        'name': 'hamsik',
        'age': 17
    },
    'student3': {
        'name': 'muller',
        'age': 18
    }
}
for std_key in school:
    print(school[std_key]['name'])