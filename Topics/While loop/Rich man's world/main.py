amount = int(input())
max_protected_amount = 700000
years_needed = 0
while amount<=max_protected_amount:
    years_needed += 1
    amount = amount * 1.071
print(years_needed)
