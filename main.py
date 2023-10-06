from durable.lang import *

#---------------------------------------------------------------------------------------
# when prog Triggered by 'interests' 
#---------------------------------------------------------------------------------------
with ruleset('interests'):

	@when_all((m.interest == 'aiml engineer') & (m.cgpa >= 6))
	def career1(a):
		a.assert_fact({'subject':'You can proceed','predicate':'with this Career :','object':'AI-ML Engineer'})
		a.assert_fact({'subject':'You can proceed','predicate':'with this Career :','object':'Data Science'})


	@when_all((m.interest == 'full-stack development') & (m.cgpa >= 5.5))
	def career2(a):
		a.assert_fact({'subject':'You can proceed','predicate':'with this Career :','object':'Full-Stack Development'})
		a.assert_fact({'subject':'You can proceed','predicate':'with this Career :','object':'Freelancing'})


	@when_all((m.interest == 'data science') & (m.cgpa >= 7)) 
	def career3(a):
		a.assert_fact({'subject':'You can proceed','predicate':'with this Career :','object':'Data Science and work as Data Scientist @MAANG'})


	@when_all((m.interest == 'block chain') & (m.cgpa >= 6)) 
	def career4(a):
		a.assert_fact({'subject':'You can proceed','predicate':'with this Career :','object':'Block Chain Developer'})


	@when_all((m.interest == 'banking') & (m.cgpa >= 5.8)) 
	def career5(a):
		a.assert_fact({'subject':'You can proceed','predicate':'with this Career :','object':'Banking and work in both govt. and private banks'})


	@when_all((m.interest == 'management') & (m.cgpa >= 6)) 
	def career6(a):
		a.assert_fact({'subject':'You can','predicate':'go for :','object':'MBA'})


	@when_all((m.interest == 'higher studies abroad') & (m.cgpa >= 6.4)) 
	def career7(a):
		a.assert_fact({'subject':'You can','predicate':'go for :','object':'doing MS from Stanford like Universities'})


	@when_all((m.interest == 'enterpreneurship') & (m.cgpa >= 6.1)) 
	def career8(a):
		a.assert_fact({'subject':'You can','predicate':'proceed with :','object':'Enterpreneurship and build startup'})


	@when_all((m.interest == 'civil services') & (m.cgpa >= 5.6)) 
	def career9(a):
		a.assert_fact({'subject':'You can','predicate':'go for :','object':'Civil Services Examination and Crack it'})


	@when_all((m.interest == 'jobs in psu') & (m.cgpa >= 6)) 
	def career10(a):
		a.assert_fact({'subject':'You can','predicate':'try for :','object':'PSUs Jobs'})


	@when_all((m.interest == 'freelancing') & (m.cgpa >= 6)) 
	def career11(a):
		a.assert_fact({'subject':'You can','predicate':'proceed with :','object':'Freelancing'})


	@when_all((m.interest == 'research domain') & (m.cgpa >= 8)) 
	def career12(a):
		a.assert_fact({'subject':'You can','predicate':'try for :','object':'Research Domain'})

	@when_all(+m.subject)
	def output(a):
		print('Fact: {0} {1} {2}'.format(a.m.subject, a.m.predicate, a.m.object))



#---------------------------------------------------------------------------------------
# when prog Triggered by 'coursesDone' 
#---------------------------------------------------------------------------------------
with ruleset('coursesDone'):
	# 1
	@when_all((m.courses=='dsa+cs-cores') & (m.cgpa >= 5)) 
	def SDE(b):
		b.assert_fact({'subject':'You can proceed','predicate':'with this Career :','object':'Software Development and work as SDE @MAANG'})
	# 2
	@when_all((m.courses=='maths') & (m.cgpa >= 5.7)) 
	def InvestmentBanking(b):
		b.assert_fact({'subject':'You can proceed','predicate':'with this Career :','object':'Investment Banker'})
	# 3
	@when_all((m.courses=='bio') & (m.cgpa >= 5.8)) 
	def bionomics(b):
		b.assert_fact({'subject':'You can go','predicate':'in the field of :','object':'Bionomics and AI in Healthcare'})
	# 4
	@when_all((m.courses=='ssh') & (m.cgpa >= 5)) 
	def ssh(b):
		b.assert_fact({'subject':'You can proceed','predicate':'with this Career :','object':'Teaching and Politics'})
		b.assert_fact({'subject':'You can proceed','predicate':'with this Career :','object':'grade A level govt. job'})
	# 5
	@when_all((m.courses=='eco') & (m.cgpa >= 5.9)) 
	def economics(b):
		b.assert_fact({'subject':'You can proceed','predicate':'in the field of :','object':'Economics'})

	@when_all(+m.subject)
	def output(b):
		print('Fact: {0} {1} {2}'.format(b.m.subject, b.m.predicate, b.m.object))

#********************************************************************************





dict_interests = {1:"aiml engineer", 2:"full-stack development", 3:"data science", 4:"block chain", 5:"banking", 6:"management", 7:"higher studies abroad", 8:"enterpreneurship", 9:"civil services", 10:"jobs in psu", 11:"freelancing", 12:"research domain"}
dict_courses = {1:"dsa+cs-cores", 2:"maths", 3:"bio", 4:"ssh", 5:"eco"}






# Starting point of the program
print("======================Welcome to Career Advisory System======================")
print('\n')

# Calculating CGPA of the graduating student 
print("Calculating CGPA")
lstOfgradePts = [int(x) for x in input("Enter your Grade points of the Courses as space-separated [10 9 9 8 7 7 8 8 9 10] : ").split()]
# print(lstOfgradePts, len(lstOfgradePts), type(lstOfgradePts[0]), lstOfgradePts[0])

lstOfCredits = [int(x) for x in input("Enter your Credits corresponding to each course as space-separated [4 4 4 4 4 4 4 4 4 2] : ").split()]
# print(lstOfCredits, len(lstOfCredits), type(lstOfCredits), lstOfCredits[0])

sum1 = 0 #sigma(gradePt*credit)
sum2 = 0 #sigma(credit)
for idx in range(len(lstOfgradePts)):
  # print(idx)
  sum1 += lstOfCredits[idx]*lstOfgradePts[idx]
  sum2 += lstOfCredits[idx]

cgpa = sum1/sum2
# print("Sum1 = {}, Sum2 = {}".format(sum1, sum2))
# print("CGPA = ",cgpa)

# cgpa = 7.9 #delete after use
print("CGPA =", cgpa) #delete after use
# lst of interests shows
print("Select the interest which best for you amongs listed below:")
print("-"*30)
print("[Code]  [Interest]")
print("-"*30)
print("   1    ai-ml engineer \n   2    full-stack development \n   3    data science \n   4    block Chain \n   5    banking \n   6    management \n   7    higher Studies abroad \n   8    Enterpreneurship \n   9    Civil Servies \n   10   Jobs in PSUs \n   11   freelancing \n   12   research domain") 
print("-"*30)
print()


# while for student interest
stu_interest = ""
while(True):
	interest_code = int(input("Enter the Code of your interest : "))
	if(interest_code>=1 and interest_code<=12):
		stu_interest = dict_interests[interest_code]
		# print(stu_interest)
		break
	else:
		print("Sorry, You didn't satisfy the above criteria!!!")


#-----------lst of courses shows---------------
print()
print("Select the courses which you have done amongs listed below:")
print("-"*30)
print("[Code]  [Course]")
print("-"*30)
print("   1    DSA+CS-Core_fundamental \n   2    Maths(M1-M4) \n   3    Bio Courses(Healthcare) \n   4    SocialSci and Humanities \n   5    Eco Courses") 
print("-"*30)
print()    

# taking student's courses information that done or not
numOfCourses = int(input("How many courses you have done ? : "))
stu_course = ""
tmp = []
for i in range(1, numOfCourses+1):
    # print(i)
	while(True):
		course_code = int(input("Enter the code of your courses : "))
		if(course_code>=1 and course_code<=5):
			# stu_course = dict_courses[course_code]
			# print(stu_course)
			tmp.append(course_code)
			break
		else:
			print("Invalid course code, pls enter again!!")		
	
print()
for idx_code in tmp:
	# print(idx_code)
	stu_course = dict_courses[idx_code]
	# triggering courseDone
	try:
		assert_fact('coursesDone', {'courses': stu_course, 'cgpa': cgpa})
	except BaseException as error:
		print('Sorry, You did not satisfy the above criteria!!!' )


# triggering interests
try:
	assert_fact('interests', {'interest': stu_interest, 'cgpa': cgpa})
except BaseException as error:
	print('Sorry, Your CGPA did not satisfy the above criteria!!!' )

print("============================END of The program================================")
