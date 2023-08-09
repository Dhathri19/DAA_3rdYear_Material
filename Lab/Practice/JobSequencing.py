class Job:
    def __init__(self, taskId, deadline, profit):
        self.taskId = taskId
        self.deadline = deadline
        self.profit = profit

def scheduleJobs(jobs, T):
    profit = 0
    slot = [-1] * T
    jobs.sort(key=lambda x: x.profit, reverse=True)
 
    
    for job in jobs:
        
        for j in reversed(range(job.deadline)):
            if j < T and slot[j] == -1:
                slot[j] = job.taskId
                profit += job.profit
                break
 
    print('The scheduled jobs are', list(filter(lambda x: x != -1, slot)))
    print('The total profit earned is', profit)

jobs = [
        Job(1, 9, 15), Job(2, 2, 2), Job(3, 5, 18), Job(4, 7, 1), Job(5, 4, 25),
        Job(6, 2, 20), Job(7, 5, 8), Job(8, 7, 10), Job(9, 4, 12), Job(10, 3, 5)
    ]
T = 15
scheduleJobs(jobs, T)
 