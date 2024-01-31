import heapq

def solution(jobs):
    # jobs를 작업요청이 빠른 순으로 정렬
    jobs.sort()
    
    # 현재 시간에 처리할 수 있는 작업들 중에서 작업의 소요시간이 가장 적은 작업부터 처리
    # 작업을 관리할 힙 초기화
    heap = []
    
    # 현재 시간, 완료된 작업 수, 총 대기 시간
    current_time, completed_jobs, total_response_time = 0, 0, 0
    # 현재 처리중인 jobs 인덱스
    jobs_idx = 0
    
    # 모든 작업이 완료될 때까지 반복
    while completed_jobs < len(jobs):
        # 현재 시간에서 처리할 수 있는 작업들을 우선순위 큐에 추가
        while jobs_idx < len(jobs) and jobs[jobs_idx][0] <= current_time:
            start, duration = jobs[jobs_idx]
            heapq.heappush(heap, (duration, start))
            jobs_idx += 1
            
        if heap: # 처리할 작업이 있으면 처리
            duration, start = heapq.heappop(heap)
            current_time += duration
            total_response_time += current_time - start
            completed_jobs += 1
        else: # 처리할 작업이 없다면 현재 시간 증가
            current_time = jobs[jobs_idx][0]
                
    return total_response_time // completed_jobs
        
        
        