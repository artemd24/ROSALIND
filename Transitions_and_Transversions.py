

def transitions(s1: str, s2: str):
    k = 0
    for i in range(len(s1)):
        if (s1[i] == "A" and s2[i] == "G") or (s1[i] == "G" and s2[i] == "A") or (s1[i] == "C" and s2[i] == "T") or (s1[i] == "T" and s2[i] == "C"):
            k += 1

    return k


def transversions(s1: str, s2: str):
    k = 0

    for i in range(len(s1)):
        if (s1[i] in ("A", "G") and s2[i] in ("T", "C")) or (s1[i] in ("T", "C") and s2[i] in ("A", "G")):
            k += 1

    return k


s1 = input()
s2 = input()

print(transitions(s1, s2)/transversions(s1, s2))
