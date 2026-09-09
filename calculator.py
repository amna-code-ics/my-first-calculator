print('--- Board Marks Percentage Calculator ---')

obtained_marks = input('Apne Hasil Karda (Obtained) Marks Likhein: ')
total_marks = input('Apne Total Marks Likhein: ')

percentage = (int(obtained_marks) / int(total_marks)) * 100
print('Amna, aapki board exam percentage hai:', percentage, '%')

if percentage >= 80:
    gpa = 4.0
    grade = 'A+'
elif percentage >= 70:
    gpa = 3.5
    grade = 'A'
elif percentage >= 60:
    gpa = 3.0
    grade = 'B'
else:
    gpa = 2.0
    grade = 'C'

print('Amna, aapka estimated International GPA hai:', gpa, 'aur Grade hai:', grade)
