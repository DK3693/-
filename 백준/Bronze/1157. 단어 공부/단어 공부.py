a = input().lower()
alpha = [chr(x) for x in range(97, 123)]
n = a.count(alpha[0])
a_count = []

for x in alpha:
    a_count.append(a.count(x))

if a_count.count(max(a_count)) == 1:
    print(alpha[a_count.index(max(a_count))].upper())
else:
    print("?")   
 