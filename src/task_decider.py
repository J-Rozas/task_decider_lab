def get_preferred_option(task1, task2):
    if task2.description in task1.preferred_over:
        return task1.description
    else:
        return task2.description
        



