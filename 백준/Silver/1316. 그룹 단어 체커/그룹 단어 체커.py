N = int(input())
count = 0
for _ in range(N):
    word_list = []
    word = input()
    count += 1
    i = 0
    
    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            i += 1
            continue
        elif word[i] != word[i + 1]:
            if word[i + 1] in word_list:
                count -= 1
                break
            else:
                word_list.append(word[i])
                i += 1
                continue
print(count)
            