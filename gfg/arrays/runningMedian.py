# from heapq import heapqpush, heapqpop, _heapify_max
#
# def addNumber(number, max_heap, min_heap):
#     if(len(max_heap) == 0 or max_heap[0] > number):
#         max_heap.append(number)
#         _heapify_max(max_heap)
#     else:
#         heappush(min_heap, number)
#     return max_heap, min_heap
#
# def reBalanceHeaps(max_heap, min_heap):
#     if(len(max_heap)-len(min_heap) >= 2):
#         pop = max_heap[0]
#         max_heap[0] = max_heap[len(max_heap)-1]
#         max_heap = max_heap[:len(max_heap)-1]
#         _heapify_max(max_heap)
#         heappush(min_heap, pop)
#     elif(len(min_heap)-len(max_heap) >= 2):
#         pop = heappop(min_heap)
#         max_heap.append(pop)
#         _heapify_max(max_heap)
#     return max_heap, min_heap
#
# def getMedian(max_heap, min_heap):
#     if(len(max_heap) == len(min_heap)):
#         return (float(max_heap[0]) + float(min_heap[0]))/2.0
#     elif(len(max_heap) > len(min_heap)):
#         return float(max_heap[0])
#     else:
#         return float(min_heap[0])
#
# def runningMedian(L):
#     max_heap = []
#     min_heap = []
#     medians = []
#     for i in L:
#         max_heap, min_heap = addNumber(i, max_heap, min_heap)
#         max_heap, min_heap = reBalanceHeaps(max_heap, min_heap)
#         print getMedian(max_heap, min_heap)
#     return medians
#
# L = [int(raw_input()) for _ in range(int(raw_input()))]
# runningMedian(L)




import heapq

def addNumber(number, max_heap, min_heap):
    if(len(min_heap) == 0 or -(max_heap[0]) < number):
        heappush(min_heap, number)
    else:
        heappush(max_heap, -number)
    return max_heap, min_heap

def reBalanceHeaps(max_heap, min_heap):
    if(len(max_heap)-len(min_heap) >= 2):
        pop = heappop(max_heap)
        heappush(min_heap, -pop)
    elif(len(min_heap)-len(max_heap) >= 2):
        pop = heappop(min_heap)
        heappush(max_heap, -pop)
    return max_heap, min_heap

def getMedian(max_heap, min_heap):
    if(len(max_heap) == len(min_heap)):
        return (float(max_heap[0]) + float(min_heap[0]))/2.0
    elif(len(max_heap) > len(min_heap)):
        return float(-max_heap[0])
    else:
        return float(min_heap[0])

def runningMedian(L):
    max_heap = []
    min_heap = []
    for i in L:
        max_heap, min_heap = addNumber(i, max_heap, min_heap)
        max_heap, min_heap = reBalanceHeaps(max_heap, min_heap)
        print getMedian(max_heap, min_heap)

L = [int(raw_input()) for _ in range(int(raw_input()))]
runningMedian(L)
