def tavaliDNA(DNA, tedad_tavali):
    sequence_count = {}
    S = 0
    for i in range(len(DNA) - tedad_tavali + 1):
        sequence = DNA[i:i+tedad_tavali]
        sequence_count[sequence] = sequence_count.get(sequence, 0) + 1
        S += 1
    return sequence_count, S

DNA = input("Enter the DNA strand: ").upper().strip().replace(" ","")
tedaad_tavali = int(input("Enter the sequence length: "))

print(f"All {tedaad_tavali}-sequences within the DNA :")
sequences, s = tavaliDNA(DNA, tedaad_tavali)

for sequence, count in sequences.items():
    print(sequence,":", count)

print(f"Total number of {tedaad_tavali}-sequences: {s}")









