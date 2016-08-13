dna_file = open('./dna2.fasta').read()

# cpmpute how many records in the file
print dna_file
records_num = dna_file.count('>')
print records_num

#compute lengths of the sequences
seqs = dna_file.split('>')[1:]
lengths = {}
for i in range(records_num):
    identifier = seqs[i].split(' ')[0]
    seq = ''.join(seqs[i].split('\n')[1:]).replace("\n", "")
    length = len(seq)
    lengths[identifier] = length
print sorted(lengths.items(), key=lambda x: x[1])