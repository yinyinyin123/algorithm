

### heapsort

heap = [0]

def insertNum(heap, num):
    heap.append(num)
    i = len(heap)-1
    while(i != 1):
        if(heap[i//2] > heap[i]):
            heap[i//2], heap[i] = heap[i], heap[i//2]
            i = i // 2
        else:
            break

def makeheap():
    data = [4,5,6,1,2,10,25,1235,1,24,1]
    for num in data:
        insertNum(heap, num)
        print(heap)

def adjustheap(heap):
    idx = 1
    while(idx*2 < len(heap)):
        if(heap[idx] <= heap[idx*2]):
            if(idx*2+1 >= len(heap)):
                return
            elif(idx*2+1 < len(heap) and heap[idx] <= heap[idx*2+1]):
                return
            else:
                heap[idx], heap[idx*2+1] = heap[idx*2+1], heap[idx]
                idx = idx*2+1
        else:
            if(idx*2+1 >= len(heap) or (idx*2+1 < len(heap) and heap[idx] <= heap[idx*2+1])):
                heap[idx], heap[idx*2] = heap[idx*2], heap[idx]
                idx = idx*2
            else:
                if(heap[idx*2+1] < heap[idx*2]):
                    heap[idx*2+1], heap[idx] = heap[idx], heap[idx*2+1]
                    idx = idx*2+1
                else:
                    heap[idx*2], heap[idx] = heap[idx], heap[idx*2]
                    idx = idx*2

def heapsort(heap):
    length = len(heap) - 1
    for i in range(length):
        print(heap[1])
        heap[1], heap[-1] = heap[-1], heap[1]
        heap.pop()
        adjustheap(heap)


makeheap()
heapsort(heap)
