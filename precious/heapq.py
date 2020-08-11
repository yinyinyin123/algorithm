
import heapq as hq
import numpy as np

data = np.arange(10)
np.random.shuffle(data)

heap = []
for datum in data:
    hq.heappush(heap, datum)

print(heap)

while(heap):
    print(hq.heappop(heap))
