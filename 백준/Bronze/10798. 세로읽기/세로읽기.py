import sys
word_max = 0
words = []
read = []
for _ in range(5):
    word = list(sys.stdin.readline())
    if word_max < len(word):
        word_max = len(word)
    words.append(word)
        
for j in range(word_max - 1):
    for i in range(5):
        try:
            if words[i][j] == '\n':
                continue
            read.append(words[i][j])
        except:
            continue
print(''.join(map(str, read)))