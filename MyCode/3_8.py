dnaMolecularWeight = {'a':323.2, 'c':289.2, 't':304.2, 'g':329.2}

def oligoMolecularWeight(sequence):
    dnaMolecularWeight = {'a':323.2, 'c':289.2, 't':304.2, 'g':329.2}
    molecularWeight = 0.0
    for base in sequence:
        molecularWeight += dnaMolecularWeight[base]
    return molecularWeight

# dnaSequence = 'tagcgctttatcg'
# print(oligoMolecularWeight(dnaSequence))

restrictionEnzymes = {}
restrictionEnzymes['bamH1'] = ['ggatcc', 0]
restrictionEnzymes['sma1'] = ['cccggg', 2]
def restrictionDigest(sequence,enzyme):
    motif = restrictionEnzymes[enzyme][0]
    cutPosition = restrictionEnzymes[enzyme][1]
    fragments = []
    found = 0
    lastCut = found
    searchFrom = lastCut
    while found != -1:
        found = sequence.find(motif,searchFrom)
        if found != -1:
            fragment = sequence[lastCut:found+cutPosition]
            mwt = oligoMolecularWeight(fragment)
            fragments.append((fragment,mwt))
        else:
            fragment = sequence[lastCut:]
            mwt = oligoMolecularWeight(fragment)
            fragments.append((fragment,mwt))
        lastCut = found + cutPosition
        searchFrom = lastCut + 1
    return fragments

digestSequence = 'gcgatgctaggatccgcgatcgcgtacgatcgtacgcggtacggacggatccttctc'
print(restrictionDigest(digestSequence,'bamH1'))

