dna_file = open('./dna2.fasta').read()

# find all occurance of a condon
def find_all(condon,string):
    occs = []
    last = string.rfind(condon)
    index = 0
    while index < last:
        occ = string.find(condon,index)
        index = occ + 1
        if occ%3 == 0:
            occs.append(occ)
    return occs

# find the longest ORF in one seq (of 3 possible frames)
def longest_ORF(string):
    frames = [ string, string[1:],string[2:] ]
    longest = 0
    location_ = 0
    for frame in frames:
        start = find_all('ATG',frame)
        end = []
        end_condons = ['TAA','TAG','TGA']
        for condon in end_condons:
            end = end + (find_all(condon, frame) )   
        
        substraction = top = len(frame)
        location = 0
        for i in range(len(start)):
            for j in range(len(end)):
                substraction = int(end[j]) - int(start[i]) + 3
                if substraction > 0 and substraction < top:
                    top = substraction
                    location = start[i]

            if top > longest:
                longest = top
                location_ = location
    return {'length':longest,'start':location_}     

# find the longest ORF and its identifier in a file
seqs = dna_file.split('>')[1:]
seqs_longest = 0
for i in range(records_num):
    identifier = seqs[i].split(' ')[0]
    seq = ''.join(seqs[i].split('\n')[1:]).replace("\n", "")
    seq_longest = longest_ORF(seq)['length']
    if seq_longest > seqs_longest:
        seqs_longest = seq_longest
        iden = identifier
print seqs_longest,iden