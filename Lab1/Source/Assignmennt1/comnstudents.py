#Students belongs to python class
pythn=['raju','ram','krishna','kishore']
print("python class students:",pythn)

#Students belongs to Web Application class
webapp=['ram','kumar','raju','raheem']
print("Web Application class students are:",webapp)
print("-----------------------------------------")
#Common students from both classes
students=list(set(pythn).intersection(webapp))
print('Common students are:',students)

#Unique Students from both classes
cal=list(set(pythn)^set(webapp))
print('Other students:',cal)