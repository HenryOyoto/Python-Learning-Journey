def greet(message):
    if "hello" in message:
        return "Hello there!"

    else:
        return "I dont understand what you are saying."

text = input("Enter a message: ") 
result = greet(text)
print(result)