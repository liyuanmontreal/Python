
# Creating a Set with
# a mixed type of values
# (Having numbers and strings)
Set = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of Mixed Values")
print(Set)
#output:
#Set with the use of Mixed Values
#{1, 2, 4, 6, 'For', 'Geeks'}


  
# Accessing element using
# for loop
print("\nElements of set: ")
for i in Set:
    print(i, end =" ")
print()
#output
#Elements of set: 
#1 2 4 6 For Geeks 

  
# Checking the element
# using in keyword
print("Geeks" in Set)
#output
#ture