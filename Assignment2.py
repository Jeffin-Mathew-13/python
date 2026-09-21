age_list=[24,25,26,27,28]
name_list=['abi','ebi','baby','ravi','pavi']

name_list.append('yazhini')
age_list.insert(2,30)
name_list.remove('yazhini')
age_list.pop(-1)

l=[29,30,31]
age_list.extend(l)

name_list.sort()

sum=sum(age_list)
max=max(age_list)
min=min(age_list)

print(age_list)
print(name_list)
print(name_list[0])
print(name_list[-1])
print(name_list[2:4])
print(name_list[::-1])

student_marks={'Abi':88,'Baby':95,'Ravi':78,'Pavi':79}
print(student_marks['Abi'])

student_marks['Janani']=82

student_marks['Baby']=82

print(student_marks)

print(student_marks.keys())
print(student_marks.values())
print(student_marks.items())

my_set={'a','e','i','o','u','a','a','i'}
print(my_set)

set1={1,3,5,7,9}
set2={2,3,5,8,10}

#my_set[4]='s'

print("union",set1.union(set2))
print("intersection",set1.intersection(set2))


print("Enter you score (0-10):")
score=float(input())
if(score>10 or score<0):print("Your score must be between 0 and 10")
elif score>7:print("Above Average\nGood Job!!!")
elif score>=4:print("Average\nPractice More!!!!")
else:print("Below Average\nStudy More!!!!!!!!")
