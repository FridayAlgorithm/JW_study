import heapq
import sys
heap = []
for _ in range(int(input())):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap,(abs(num),num))
                //heappush ->  힙에 원소를 추가하기 (원소를 추가할 대상 리스트,추가할 원소)

    else:
        if heap:
            print(heapq.heappop(heap)[1])
                    //heappop -> 원소를 삭제할 대상 리스트를 인자로 넘기면, 가장 작은 원소를 삭제 후에 그 값을 리턴

        else:
            print(0)
