students = ['Amit','Binny','Carle','David']
marks = [85, 90, 78, 72]

result = {students[i]: marks[i] for i in range(len(students))}

x = input('Enter student name: ')
print(result[x] if x in result else 'Student not found')