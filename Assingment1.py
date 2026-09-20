from operator import concat

s1="Enter your name :"
s2="Hello"
s3=", welcome to python programming"

print(s1)
s4 = input()
s5=concat(s2," ")
s5=concat(s5,s4)
s5=concat(s5,s3)
print(s5)

print("First character :",s5[0],
      "\nLast character :",s5[-1],
      "\nFirst 5 characters :",s5[:5],
      "\nLast 11 characters :",s5[-11:],
      "\nin reverse order :",s5[::-1])

start=s5.index("python")
print("\nsliced python :", s5[start:start+6],"\n")

s6="Python beginner tutorial"
print("\nUppercase :",s6.upper())
print("\nLowercase :",s6.lower())
print("\nCapitilized :",s6.capitalize())
print("\nNo. of t :",s6.count("t"))
print("\nafter replacement :\n",s6.replace("Python","Machine Learning"))

t1=(10,20,30)
t2=(40,50,60)
t_combine=t1+t2
print("\ncombined tuple :",t_combine)
print("\ncombined tuple printed 3 times :\n",t_combine*3)
print("\nthird element from t_combine :",t_combine[2])
print("\nfirst 3 elements from t_combine :",t_combine[:3])
print("\nlast 3 elements from t_combine :",t_combine[-3:])