s = raw_input("type a word: ") # uncomment this for the code grader

vowels = 0
for letter in s:
    if letter in "aeiou":
        vowels +=1
print "Number of vowels: " + str(vowels)