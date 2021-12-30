def build_person(first_name, last_name, age=''):
    if age:
        person = {'first': first_name, 'last': last_name, 'age': age}
        return person
    else:
        person = {'first': first_name, 'last': last_name}
        return person
'''
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
'''
p = build_person('ying', 'liu')
print(p)
p = build_person('ds', 'dw', age=8)
print(p)