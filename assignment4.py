DIVIDER = "--------------------------------------------"
GREETING = "This is the beginning of this task! :)"
name = input("Hi, What is your name? ")

print(DIVIDER)
print(GREETING)
print(DIVIDER)   
# 1. Python List Transformation
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

# Task 1:
grades2= grades
grades2.sort(reverse=True)
print(f"Here is a sorted list of grades! {grades2}")

# Task 2
average=int(sum(grades))//int(len(grades))
print(f"The average grade of the students is: {average}")

# Task 3:
for i in range(len(grades)):
    if grades[i] < 80:
        grades[i] = "reproved"
print(f"Grades with reproved ones are: {grades}")

print(DIVIDER)
print(GREETING)
print(DIVIDER)   
# 2. Advanced List Methods and Identity Operators
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Task 1:
attsub =[]
for students in attended:
    if students in submitted:
        attsub.append(students)
print(f"Alumns that submitted their assignments and attended the class: {attsub}")

# Task 2:
if submitted == attended: 
    print("The lists are the same")
else:
    print("The list are not the same")
    
# Task 3:
for students in attended:
    if students not in submitted:
        attended.remove(students)
print(f"The new attended list is: {attended}")
        
print(DIVIDER) 
print(GREETING)  
print(DIVIDER)     
# 3. Advanced Slicing Techniques
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Task 1: 
segment=temperatures[7:14]
print(f"Temperatures from second week are: {segment}" ) 

# Task 2:
temp100=[]

for temp in temperatures:
    if temp > 100:
        temp100.append(temp)

print(f"temperatures greater than 100 are: {temp100}")

# Task 3:
temperaturesrev = temperatures

temperaturesrev.reverse()
extractedvalues=[]
extractedvalues.append(temperaturesrev[4:10])

print(f"the reversed temperatures are: {temperaturesrev}")
print(f"The 5th to 10th days are: {extractedvalues}")

print(DIVIDER)
print(GREETING)
print(DIVIDER)   
# 4. List Comprehensions and Membership Operators()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Task 1:
nums2 = []
for even in numbers:
    if even%2==0:
        nums2.append(even)
print(f"The even numbers in the list are: {nums2}")

# Task 2: 
nums5=[]
for num in numbers:
    if num>5:
        nums5.append(num)
print(f"Here are the numbers greater than 5 in the list!: {nums5}")

# Task 3:
if 7 in numbers:
    print("Hey there is a seven in numbers!")
else:
    print("No, there is not a seven in numbers :(")
    
print(DIVIDER)    
print(GREETING)
print(DIVIDER)       
# 5 Deep Dive into Python Lists
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

# Task 1:
for i in range(len(students)):
    if grades[i] < 80:
        print(f"Students with a grade below 80, their name, grade and activity: {students[i]}, {grades[i]}, {activities[i]}")

# Task 2:
students_approved = []

for i in range(len(students)):
    if grades[i] > 80:
        students_approved.append(students[i])

# Task 3:
print(f"Name of the students with a grade above 80: {students_approved}")
print(DIVIDER)  


print(f'Have a great day {name}!!')