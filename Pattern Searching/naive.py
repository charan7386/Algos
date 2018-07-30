s = raw_input()
pat = raw_input()
for i in range(len(s)-len(pat)+1):
    for j in range(len(pat)):
        if(s[i+j] != pat[j]):
            break
        if(j == len(pat)-1):
            print 'Pattern found at ', i    
