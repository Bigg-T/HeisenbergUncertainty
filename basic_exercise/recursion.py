#!/usr/bin/python3

def getSchedule(data):
    """
    Tail recursion of DFS implementation to create a schedule jobs.
    The graph of jobs and its dependencies must be a DAG.
    """
    schedule = scheduleHelper(data, list(data.keys()),0, {})
    return schedule

def scheduleHelper(data, stack, count, completedJob):
    if count >= len(data.keys()):
        return completedJob
    job = stack.pop()
    # Getting rid of seen jobs
    while (job in completedJob):
        job = stack.pop()

    if (isRunnable(data, completedJob, job)):
        completedJob.update({job : count})
        count = count + 1
    else:
        dependent = data[job]
        stack.append(job)
        stack.extend(dependent)
    return scheduleHelper(data, stack, count, completedJob)

# True if the job can be run
def isRunnable(data, completedJob, job):
    dependent = data[job]
    temp = True
    # Check if all job dependencies had ran
    for d in dependent:
        temp = temp and (d in completedJob)
    return temp
