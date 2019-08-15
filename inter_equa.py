from math import isclose

a = -0.1234567
b = -0.1234569

if isclose(a,b,rel_tol=1e-5):
    print("isclose")
else:
    pass
c = -1.1861406564712524

result1 = 2 * c ** 2 + 7
result2 = c + 11
print(result1)
print(result2)