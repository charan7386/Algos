#LPS array defination
def LPS_array(pat, M, lps):
    len = 0
    i = 1
    while i<M:
        if(pat[i] == pat[len]):
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1

def KMP(s, pat):
    N = len(s)
    M = len(pat)
    lps = [0]*M
    j = 0
    LPS_array(pat, M, lps)
    i = 0
    while i < N:
        if(s[i] == pat[j]):
            i += 1
            j += 1
        if j == M:
            print 'Found at ', (i-j)
            j = lps[j-1]
        elif i<N and s[i] != pat[j]:
            if j!= 0:
                j = lps[j-1]
            else:
                i += 1


s = raw_input()
pat = raw_input()
KMP(s, pat)
