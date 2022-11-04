name = input ("Enter your name: ")
login = "Weimer"

# if the comparison result (name==login) is True, then:
if name == login:
    print("Hello", name)
# if the user enters a name less than three letters, then:
elif len (name) <3:
    print("This name is not available")
# if the result of the comparison (name==login) is False, and the username is 3>=, then:
else:
    print("Hello, user")

print("The end")