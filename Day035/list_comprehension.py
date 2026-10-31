# This is Day 35 of Python
# Today is all about list and dictionary comprehensions

## List Comprehension
words = ["Henry", "Oyoto", "Owade", "Man-U", "Toss"]

lowercase_words = [word.lower() for word in words if len(word) > 4]

print(lowercase_words)

## Dictionary Comprehension 

counts = {word: lowercase_words.count(word) for word in lowercase_words}

print(counts)