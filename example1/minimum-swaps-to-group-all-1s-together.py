def minSwaps(data):
    count1 = data.count(1)
    total = 0
    for i in range(count1): total += data[i]
    swaps = count1-total
    for r in range(count1, len(data)):
        total += data[r]
        total -= data[r-count1]
        swaps = min(swaps, count1-total)
    return swaps

minSwaps([1,0,1,0,1,0,0,1,1,0,1])