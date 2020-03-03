first_DNA = input()
second_DNA = input()
substring_numbers = []


def find_line(fl, sl):
    if fl.find(sl) != -1:
        if len(substring_numbers) != 0:
            substring_numbers.append(fl.find(sl) + 1 + substring_numbers[-1])
        else:
            substring_numbers.append(fl.find(sl) + 1)
        find_line(fl[fl.find(sl) + 1:], sl)
    else:
        return


find_line(first_DNA, second_DNA)

print(substring_numbers)
