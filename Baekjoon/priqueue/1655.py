import sys 
import heapq

max_heap = []
min_heap = []

for _ in range(int(input())):
    num = int(sys.stdin.readline())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-num, num))
        //heappush ->  힙에 원소를 추가하기 (원소를 추가할 대상 리스트,추가할 원소)
    else:
        heapq.heappush(min_heap, (num, num))

    if min_heap and max_heap[0][1] > min_heap[0][1]:
        max_value = heapq.heappop(max_heap)[1]
        min_value = heapq.heappop(min_heap)[1]
        //heappop -> 원소를 삭제할 대상 리스트를 인자로 넘기면, 가장 작은 원소를 삭제 후에 그 값을 리턴
        heapq.heappush(min_heap, (max_value, max_value))
        heapq.heappush(max_heap, (-min_value, min_value))

    print(max_heap[0][1])
   //공부필요
