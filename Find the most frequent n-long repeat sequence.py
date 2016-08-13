# find all occurance of substr in a str
def find_All(substring,string):
    occs = []
    last = string.rfind(substring)
    index = 0
    while index < last:
        occ = string.find(substring,index)
        index = occ + 1
        occs.append(occ)
    return len(occs)

# compute repeatance of n-long substr and return the most frequent one
def compute_repeat(string,n):
    repeats = {}
    highest_occ = 0
    for i in range(0,len(string)-n+1):
        find_area = string[i:]
        substr = string[i:i+n]
        all_occ = find_All(substr,find_area) 
        
        if all_occ > highest_occ:
            highest_occ = all_occ
            nmer = substr
    return highest_occ,nmer      

test = 'GACCTCGAAGTTGTCGAATTTCCACGCGTTCTGCGAGCCTGCCGCCGGCTGGTTCGCGAAGTACAGATTC'
print compute_repeat(test,4)