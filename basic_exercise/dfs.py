#!/usr/bin/python3

def getSchedule(data):
    """
    The Graph must be a DAG.
    """
    stack = list(jobs.keys())
    completedJob = {}
    count = 0
    totalJobs = len(data.keys())
    while(count < totalJobs):
        job = stack.pop()
        if (job in completedJob):
            continue
        if (isRunnable(data, completedJob, job)):
            completedJob.update({job : count})
            count = count + 1
        else:
            dependent = data[job]
            stack.append(job)
            stack.extend(dependent)
    return completedJob

# True if the job can be run
def isRunnable(data, completedJob, job):
    dependent = data[job]
    temp = True
    # Check if all job dependencies had ran
    for d in dependent:
        temp = temp and (d in completedJob)
    return temp
