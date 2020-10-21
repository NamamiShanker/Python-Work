ages = list(map(int, input().split()))
age_sum = sum(ages)

# List comprehension
fracs = [age/age_sum for age in ages]

fecnc = [frac**2 * 100 for frac in fracs]

print(fecnc)
