## question 1
s1 = """
“'And' and 'or' are the basic operations of logic. Together with 'no' (the logical operation 
of negation) they are a complete set of basic logical operations — all other logical 
operations, no matter how complex, can be obtained by suitable combinations of these.” 
― John von Neumann, The Computer and the Brain
"""

s2 = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit 
esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt 
in culpa qui officia deserunt mollit anim id est laborum.
"""

resultOfS1 = {}
resultOfS2 = {}

for leter in s1:
    if leter.isalpha():
        resultOfS1[leter] = resultOfS1.get(leter, 0) + 1

for leter in s2:
    if leter.isalpha():
        resultOfS2[leter] = resultOfS2.get(leter, 0) + 1

# print(resultOfS1)
# print(resultOfS2)

## -----------------------------------
## question 2
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'d': 100, 'e': 200, 'f': 300}
d3 = {'f': 30, 'g': 40}

key_list = []
value_list = []

for dict_item in [d1, d2, d3]:
    for key, value in dict_item.items():
        key_list.append(key)
        value_list.append(value)

# print('key_list', key_list)
# print('value_list', value_list)

## -----------------------------------
## question 3
grades = {
    'John': [90, 95, 98],
    'Eric': [86, 84, 92],
    'Michael': [90, 89, 85]
}

exam = {
    'Eric': 99,
    'John': 100
}

for student_name, student_grades in grades.items():
    student_grades.insert(0, exam.get(student_name))

# print('grades', grades)
## -----------------------------------