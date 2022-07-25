# O(nlog(n)) time | O(n) space
def taskAssignment(k, tasks):
    pairedTasks = []
    taskDurationsToIndices = getTaskDurationsToIndices(tasks)

    sortedTask = sorted(tasks)
    for idx in range(k):
        task1Duration = sortedTask[idx]
        indicesWithTask1Duration = taskDurationsToIndices[task1Duration]
        task1Index = indicesWithTask1Duration.pop()

        task2SortedIndex = len(tasks) - 1 - idx
        task2Duration = sortedTask[task2SortedIndex]
        indicesWithTask2Duration = taskDurationsToIndices[task2Duration]
        task2Index = indicesWithTask2Duration.pop()

        pairedTasks.append([task1Index, task2Index])

    return pairedTasks

def getTaskDurationsToIndices(tasks):
    taskDurationsToIndices = {}

    for idx, taskDuration in enumerate(tasks):
        if taskDuration in taskDurationsToIndices:
            taskDurationsToIndices[taskDuration].append(idx)
        else:
            taskDurationsToIndices[taskDuration] = [idx]

    return taskDurationsToIndices
