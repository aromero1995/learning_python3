#this project is a gradebook that lists the courses taken and the grades received and practices list creation and modification
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print(gradebook)
#this adds the course computer science and grade 100
gradebook.append(["computer science", 100])
print(gradebook)
#this adds visual arts and grade 93
gradebook.append(["visual arts", 93])
print(gradebook)
#this will modify the grade for visual arts to grade 98 
gradebook[-1][-1] = 98
print(gradebook)
#this removes poetry and grade 85
gradebook.remove(gradebook[2])
print(gradebook)
#this adds poetry and changed number grade to pass/fail grade
gradebook[2] = "poetry", "pass"
print(gradebook)
#this combines the last semester grades with the current semester grades to provide the full gradebook
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
