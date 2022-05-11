subject_marks = [ ('Discrete Mathematics', 93), ('Python Programming', 95), ('Environmental Science', 88), ('Engineering Physics', 83)]
print("Original list of tuples:")
print(subject_marks)
subject_marks.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
print(subject_marks)
