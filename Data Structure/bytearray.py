# Creating bytearray
a = bytearray((12, 8, 25, 2))
print("Creating Bytearray:")
print(a)                              #bytearray(b'\x0c\x08\x19\x02')
  
# accessing elements
print("\nAccessing Elements:", a[1])   #8
  
# modifying elements
a[1] = 3
print("\nAfter Modifying:")            #bytearray(b'\x0c\x03\x19\x02')
print(a)
  
# Appending elements
a.append(30)
print("\nAfter Adding Elements:")       #bytearray(b'\x0c\x03\x19\x02\x1e')
print(a)