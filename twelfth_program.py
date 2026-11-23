                    #slicing
name="pooja"
print(len(name))
# method 1: (direct method) 

#positive slicing

#index: p(0) o(1) o(2) j(3) a(4)
name="pooja"
print(name[0:3])


# Method 2: (Input Method)
# Method 1: Taking string input from me
text = input("Enter a word: ")

# Slicing from index 0 to 4 (stops before index 4)
print("First 4 characters:", text[0:4])

#negative slicing

#index: p(-5) o(-4) o(-3) j(-2) a(-1)
#method 1: (direct method)
name="pooja"
print(name[-4:-1])

# Method 2: (Input Method)
word = input("Enter a word: ")

print("Negative slice [-4:-1]:", word[-4:-1])



