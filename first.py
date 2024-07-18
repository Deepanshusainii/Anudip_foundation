# a = int(input("enter first no :"))
# b = int(input("enter second no :"))
# c = int(input("enter third no :"))
# d = int(input("enter fourth no :"))

# if(a>b and a>c and a>d):
#     print("A is greater")
# elif(a<b and c<b and d<b):
#     print("B is greater")
# elif(a<c and b<c and d<c):
#     print("C is greater")
# elif(a<d and c<d and b<d):
#     print("D is greater")
# else:
#     print("All are equal")

      
# for i in range(12,50,3):
#     print(i)            

# print("print a numbers between in 10 to 700 which are divsible by 3 and 5")
# for x in (10,700):
#     if(x%3==0 and x%5==0):
#         print(x,end=',')
        
        
# print("------------")
# print("print a numbers between in 10 to 700 which are divsible by 4")
# x=10
# while(x<700 and x%4==0):
#     print(x,end=',')
#     x =x+1
    
# print("------------")
# print("print a numbers between in 10 to 700 which are divsible by 4")
# x=10
# while(x<700):
#     if(x%4==0):
#         print(x,end=',')
#     x =x+1



# List = [3,6,8,5,2,9]
# List.insert(2,1)
# print(List)


    
    
    
student_data = ["studentId","studentName","standard","age","hindi","english","maths","science","computer","total"] 

round1    = [101,"Ashish",10,15,67,89,87,89,90,422]
round2    = [102,"Abhishek",10,14,85,45,48,90,45,313]
round3    = [103,"Aman",10,15,23,56,78,78,67,302]
round4    = [104,"Rahul",10,14,45,67,45,45,56,258]
round5    = [105,"Ruby",10,13,89,67,89,93,65,403]
round6    = [106,"Suman",10,13,90,46,67,67,67,337]
round7    = [107,"Saurabh",10,15,45,23,37,45,34,181]
round8    = [108,"Sumit",10,14,23,45,67,78,90,303]
round9    = [109,"Kamlesh",10,15,45,56,78,99,67,345]
round10   = [110,"Rohan",10,15,34,12,24,45,56,171]

student_data = [round1,round2,round3,round4,round5,round6,round7,round8,round9,round10]

# To print the list of student data
for student in student_data:
    print(student)


#Display the name of students whose marks in english is greater than 50
print("Students with English marks > 50:")
for student in student_data:
    if student[5] > 50:  # Check marks in English (index 5)
        print(student[1])  # Print name of the student (index 1)
        
        
        
#Display Student name and age of top four score of maths
student_data_sorted = sorted(student_data, key=lambda x: x[7], reverse=True)
print("Top four scorers in Maths:")
for i in range(4):
    print("Name:", student_data_sorted[i][1])  # Index 1 is for Name
    print("Age:", student_data_sorted[i][3])   # Index 3 is for Age
    print()  # Empty line for separation
    
    
    
    
#Display name,id,aghe of student who are bottom three scorer in computer           
student_data_sorted = sorted(student_data, key=lambda x: x[8])
print("Bottom three scorers in Computer:")
for i in range(3):
    print("Name:", student_data_sorted[i][1])  # Index 1 is for Name
    print("ID:", student_data_sorted[i][0])    # Index 0 is for ID
    print("Age:", student_data_sorted[i][3])   # Index 3 is for Age
    print()  # Empty line for separation