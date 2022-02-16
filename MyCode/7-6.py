import string

class Sequence:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence
    def search(self, pattern):
        return self.sequence.find(pattern)

# mySequence = Sequence('Some made up sequence','cgtatgcgct')
# print(mySequence.name)
# print(mySequence.sequence)
# print(mySequence.search('gcg'))

rnaToProtein = {'uuu':'F','uuc':'F','uua':'L','uug':'L',
                'ucu':'S','ucc':'S','uca':'S','ucg':'S',
                'uau':'Y','uac':'Y','uaa':'STOP','uag':'STOP',
                'ugu':'C','ugc':'C','uga':'STOP','ugg':'W',
                'cuu':'L','cuc':'L','cua':'L','cug':'L',
                'ccu':'P','ccc':'P','cca':'P','ccg':'P',
                'cau':'H','cac':'H','caa':'Q','cag':'Q',
                'cgu':'R','cgc':'R','cga':'R','cgg':'R',
                'auu':'I','auc':'I','aua':'I','aug':'M',
                'acu':'T','acc':'T','aca':'T','acg':'T',
                'aau':'N','aac':'N','aaa':'K','aag':'K',
                'agu':'S','agc':'S','aga':'R','agg':'R',
                'guu':'V','guc':'V','gua':'V','gug':'V',
                'gcu':'A','gcc':'A','gca':'A','gcg':'A',
                'gau':'D','gac':'D','gaa':'E','gag':'E',
                'ggu':'G','ggc':'G','gga':'G','ggg':'G'}

class RNASequence(Sequence):
    def __init__(self,name,sequence):
        Sequence.__init__(self,name,sequence)
    def translate(self):
        peptide = []
        for n in range(0,len(self.sequence),3):
            codon = self.sequence[n:n+3]
            peptide.append(rnaToProtein[codon])
        peptideSequence = ''.join(peptide)
        return peptideSequence

# myRNASequence = RNASequence('My first RNA sequence','gcugauauc')
# print(myRNASequence.name)
# print(myRNASequence.sequence)
# print(myRNASequence.search('gau'))
# print(myRNASequence.translate())

class DNASequence(Sequence):
    def __init__(self,nam,sequence):
        Sequence.__init__(self,name,sequence)
        self.resudues = {'a': 313.2, 'c': 289.2, 't':304.2, 'g':329.2}
    def transcribe(self):
        return self.sequence.replace('t','u')
    def transcribeToRNA(self):
        rnaSequence = self.sequence.replace('t','u')
        rnaName = 'Transcribe from ' + self.name
        return RNASequence(rnaName,rnaSequence)