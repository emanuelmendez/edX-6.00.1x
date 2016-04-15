s = 'bovborbobobbobobobobt' # test

count = 0

for i in range(len(s)):
    if s[i] == 'b':
        if i+2 < len(s):
            if s[i+1] == 'o' and s[i+2] == 'b':
                count += 1
     
print "Number of times bob occurs is: " + str(count)   