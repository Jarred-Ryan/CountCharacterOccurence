# word = input("Enter a word: ") #tyrannosaurus
# ch = input("Enter a character: ") #n = 2
word = input("Enter a word: ").lower()
ch = input("Enter a character: ").lower()
count = 0

for x in word:
    if x == ch:
        count += 1

print("Total amount of given character: ", count)
