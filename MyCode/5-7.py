f = open("C:\Github_repo\py4lifesci\Sequences.fasta", 'r')
lines = f.readlines()
seq_dict = {}
seq_name = None
for line in lines:
    if line[0] == '>':
        seq_name = line[1:].strip()
        seq_dict[seq_name] = ''
    else:
        if seq_name:
            seq_dict[seq_name] = seq_dict[seq_name] + line.strip()
print(seq_dict)
f.close()