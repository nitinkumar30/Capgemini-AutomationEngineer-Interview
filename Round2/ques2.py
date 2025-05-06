ls = [72, 35, 83] 
# # -find the second highest number

first = second = float('-inf')
for num in ls:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num
        
print(second)
