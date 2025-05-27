cword = input()
words = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
num = 0

for x in words:
    if x in cword:
        num += cword.count(x)
        cword = cword.replace(x, " ")

cword = cword.replace(" ","")
num += len(cword)
print(num)
                