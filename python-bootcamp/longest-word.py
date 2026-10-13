
w = ["apple", "icecream", "elephant", "cat", "strawberry", "rabbit"]

longest = max(w, key=lambda word: len(word))

print("The longest word is:", longest)
print("Length:", len(longest))