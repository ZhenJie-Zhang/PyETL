s = "absadfqwerfasdf"
result = {}
for c in s:
    if c in result:
        result[c] = result[c] + 1
    else:
        result[c] = 1
print(result)

result2 = {}
for c in s:
    try:
        result2[c] = result2[c] + 1
    except KeyError:
        result2[c] = 1
print(result2)