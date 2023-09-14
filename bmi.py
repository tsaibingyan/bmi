height = input('請輸入你的身高: ')
weight = input('請輸入你的體重: ')
height = float(height)
weight = float(weight)
height = height*0.01
height *= height
bmi = weight/height
if bmi < 18.5:
	print('你的bmi為%.2f' %bmi , '屬於體重過輕')
elif bmi >= 18.5 and bmi < 24:
	print('你的bmi為%.2f' %bmi , '屬於正常範圍')
elif bmi >= 24 and bmi < 27:
	print('你的bmi為%.2f' %bmi , '屬於過重')
elif bmi >= 27 and bmi < 30:
	print('你的bmi為%.2f' %bmi , '屬於輕度肥胖')
elif bmi >= 30 and bmi < 35:
	print('你的bmi為%.2f' %bmi , '屬於中度肥胖')
else:
	print('你的bmi為%.2f' %bmi , '屬於重度肥胖')