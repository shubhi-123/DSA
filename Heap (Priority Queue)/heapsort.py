#SORT NEARLY SORTED ARRAY USING MEAN HEAP
#K is max of distance of elements original postiion to their sorted position
#if K is not given and we need to sort arr, take K=len(arr)-1
import heapq
arr = [6, 5, 3, 2, 8, 10, 9]
k = 3
min_heap = []
sorted_arr = []

# Put first k+1 elements into the heap
for i in range(k + 1):
    heapq.heappush(min_heap, arr[i])

# Process the remaining elements
for i in range(k + 1, len(arr)):
    sorted_arr.append(heapq.heappop(min_heap))
    heapq.heappush(min_heap, arr[i])

# Pop the remaining elements
while min_heap:
    sorted_arr.append(heapq.heappop(min_heap))
print(sorted_arr)