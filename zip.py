# use zip with conditional logic to get the highest grade that the student has achieved and throw out their lowest grade
midterms = [90, 76, 94]
finals = [78, 79, 90]
students = ["Marie", "Michael", "Marge"]

final_grades = [max(pair) for pair in zip(midterms, finals)]

final = dict(zip(students, final_grades))

print(final)
