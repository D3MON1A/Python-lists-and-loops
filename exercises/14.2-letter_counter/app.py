par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
#your code go here:
par = par.lower()

for letter in par:
    if letter == " ":
        continue
    if letter not in counts:
        counts[letter] = 1 
    else :
        counts[letter] = counts[letter]+1

print(counts)

