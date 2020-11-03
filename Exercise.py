# Solution to "Find most repeated character in sentence 'This is a common interview question'"

question = "This is a common interview question"

most = {}

for char in question:
    if char in most:
        most[char] += 1
    else:
        most[char] = 1


print('Most: ', most)
