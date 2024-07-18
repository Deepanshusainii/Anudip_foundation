#Dictionary
student_dicts = [
    {'studentId': 101, 'studentName': 'Ashish', 'standard': 10, 'age': 15, 'hindi': 67, 'english': 89, 'maths': 87, 'science': 89, 'computer': 90, 'total': 422},
    {'studentId': 102, 'studentName': 'Abhishek', 'standard': 10, 'age': 14, 'hindi': 85, 'english': 45, 'maths': 48, 'science': 90, 'computer': 45, 'total': 313},
    {'studentId': 103, 'studentName': 'Aman', 'standard': 10, 'age': 15, 'hindi': 23, 'english': 56, 'maths': 78, 'science': 78, 'computer': 67, 'total': 302},
    {'studentId': 104, 'studentName': 'Rahul', 'standard': 10, 'age': 14, 'hindi': 45, 'english': 67, 'maths': 45, 'science': 45, 'computer': 56, 'total': 258},
    {'studentId': 105, 'studentName': 'Ruby', 'standard': 10, 'age': 13, 'hindi': 89, 'english': 67, 'maths': 89, 'science': 93, 'computer': 65, 'total': 403},
    {'studentId': 106, 'studentName': 'Suman', 'standard': 10, 'age': 13, 'hindi': 90, 'english': 46, 'maths': 67, 'science': 67, 'computer': 67, 'total': 337},
    {'studentId': 107, 'studentName': 'Saurabh', 'standard': 10, 'age': 15, 'hindi': 45, 'english': 23, 'maths': 37, 'science': 45, 'computer': 34, 'total': 181},
    {'studentId': 108, 'studentName': 'Sumit', 'standard': 10, 'age': 14, 'hindi': 23, 'english': 45, 'maths': 67, 'science': 78, 'computer': 90, 'total': 303},
    {'studentId': 109, 'studentName': 'Kamlesh', 'standard': 10, 'age': 15, 'hindi': 45, 'english': 56, 'maths': 78, 'science': 99, 'computer': 67, 'total': 345},
    {'studentId': 110, 'studentName': 'Rohan', 'standard': 10, 'age': 15, 'hindi': 34, 'english': 12, 'maths': 24, 'science': 45, 'computer': 56, 'total': 171}
]

# print the dictionary of student data
for student in student_dicts:
    print(student)
    print() 
    
    
    
# Display the name of students whose marks in english is greater than 50
print("Students with English marks > 50:")
for student in student_dicts:
    if student['english'] > 50:
        print(student['studentName'])


#Display Student name and age of top four score of maths
student_dicts_sorted = sorted(student_dicts, key=lambda x: x['maths'], reverse=True)
print("Top four scorers in Maths:")
for student in student_dicts_sorted[:4]:
    print(f"Name: {student['studentName']}, Age: {student['age']}")



#Display name,id,age of student who are bottom three scorer in computer      
student_dicts_sorted = sorted(student_dicts, key=lambda x: x['computer'])
print("Bottom three scorers in Computer:")
for student in student_dicts_sorted[:3]:
    print(f"Name: {student['studentName']}, ID: {student['studentId']}, Age: {student['age']}")