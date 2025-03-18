student_frequency = input('Insira a sua frequência em porcentagem (exemplo - 83,4): ').replace(',', '.')
student_test_score = input('Insira a sua frequência em porcentagem (exemplo - 9,4): ').replace(',', '.')

student_frequency = float(student_frequency)
student_test_score = float(student_test_score)

if student_frequency >= 75:
    if student_test_score >= 6:
        print(True)
    else:
        print(False)
else:
    print(False)