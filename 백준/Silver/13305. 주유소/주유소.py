N = int(input())
distance_list = list(map(int, input().split()))
price_list = list(map(int, input().split()))
total = 0
min_price = 1000000000 
for i in range(N-1):
    if price_list[i] < min_price:
        min_price = price_list[i]
    total += min_price * distance_list[i]
print(total)
        
        