age_dict={
"Ankit":22,
"Shubham":25,
"Rahul":28,
"Ravi":34,
"Raushan":28
}
name=input("enter a name: ")
age=age_dict.get(name,"not found")
print(age)
