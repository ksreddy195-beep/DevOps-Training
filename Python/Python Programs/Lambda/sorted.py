students = [("emil, 25"), ("tobias, 22"), ("linus, 28")]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)