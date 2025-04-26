import heapq
def solution(n, works):
    if sum(works) <= n:
        return 0
    
    jobs = []
    for w in works:
        heapq.heappush(jobs, -w)
    
    for _ in range(n):
        max_job_time = heapq.heappop(jobs)
        heapq.heappush(jobs, max_job_time+1)
        
    answer = 0
    for w in jobs:
        answer += w ** 2
        
    return answer

print(solution([4, 3, 3], 4))