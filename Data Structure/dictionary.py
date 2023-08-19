# Creating a Dictionary
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("Creating Dictionary: ")
print(Dict)      #{'Name': 'Geeks', 1: [1, 2, 3, 4]}

  
# accessing a element using key
print("Accessing a element using key:")
print(Dict['Name'])    #Geeks

  
# accessing a element using get()
# method
print("Accessing a element using get:")
print(Dict.get(1))     #[1, 2, 3, 4]

  
# creation using Dictionary comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print(myDict)    #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}