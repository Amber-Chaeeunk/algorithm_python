import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while any(i < K for i in scoville):
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        answer += 1
        
        if len(scoville) == 1 and scoville[0] < K:
            return -1
            
    return answer