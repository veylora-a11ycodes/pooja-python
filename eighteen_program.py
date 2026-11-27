#creating a list containing a string elements
friends=["pooja","english","10","11.4",'s']

# Checking and printing the data type of the element at index 4 ('s')
print(type(friends[4]))

# Updating the element at index 0 from "pooja" to "apple" (lists are mutable)
friends[0]="apple"  # unlike strings lists are mutable

#printing the updating list
print(friends)

# Adding a new string "crazy" to the end of the list
friends.append("crazy")


#printing the updating list
print(friends)


# Creating a list of numbers
l1=[10,4,5,89,54,34,32]

# Sorting the list in ascending order (smallest to largest)
l1.sort()
print(l1)

# Reversing the order of elements in the list

l1.reverse()
print(l1)

# Inserting 45 at index 3
l1.insert(3,45) #insert 45 such that it's index in list is 3
print(l1)

# Removing and returning the element at index 4
l1.pop(4)
print(l1)

# Removing the first occurrence of value 34 from the list
l1.remove(34)
print(l1)