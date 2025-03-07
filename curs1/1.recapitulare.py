

vocale = "aeiouAEIOU"
input_string = "Salutare, ce mai faci?"
# v1
rezultat = ""
for i in input_string:
    if i not in vocale:
        rezultat += i

print(rezultat)

# v2
for i in input_string:
    if i not in vocale:
        print(i, end="")


