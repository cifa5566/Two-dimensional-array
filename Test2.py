def second_highest():
	students = [['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]]
	student_grade = []
	for student in students:
		student_grade.append(student[1])
		grade = sorted(student_grade, reverse = True)
	second = grade[1]

	for student in students:
		if student[1] == second:
 			print(student[0])
	
	


second_highest()