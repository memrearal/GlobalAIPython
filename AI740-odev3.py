studentInfo = [
	{
		"name": "",
		"surname": "",
		"midterm": 0,
		"project": 0,
		"final": 0,
		"passingGrade": 0
	},
	{
		"name": "",
		"surname": "",
		"midterm": 0,
		"project": 0,
		"final": 0,
		"passingGrade": 0
	},
	{
		"name": "",
		"surname": "",
		"midterm": 0,
		"project": 0,
		"final": 0,
		"passingGrade": 0
	},
	{
		"name": "",
		"surname": "",
		"midterm": 0,
		"project": 0,
		"final": 0,
		"passingGrade": 0
	},
	{
		"name": "",
		"surname": "",
		"midterm": 0,
		"project": 0,
		"final": 0,
		"passingGrade": 0
	}
]
for i in range(5):
	print("\nSetting student {} information: ".format(i))
	name = input("Student Name: ")
	surname = input("Student Surname: ")
	midterm = int(input("Student Midterm Grade: "))
	project = int(input("Student Project Grade: "))
	final = int(input("Student Final Grade: "))
	studentInfo[i]["name"] = name
	studentInfo[i]["surname"] = surname
	studentInfo[i]["midterm"] = midterm
	studentInfo[i]["project"] = project
	studentInfo[i]["final"] = final
	studentInfo[i]["passingGrade"] = midterm * 0.3 + project * 0.3 + final * 0.4

studentInfo = sorted(studentInfo, reverse=True, key=lambda k: k['passingGrade'])