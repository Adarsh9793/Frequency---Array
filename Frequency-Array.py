arr = [34, 12, 45, 67, 23, 89, 7,12]
freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
        
print("Frequency of elements in the array:")
for num, count in freq.items():
    print(f"{num}: {count}")    
    
