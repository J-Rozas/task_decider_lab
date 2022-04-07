def get_preferred_option(task1, task2):
    if task1.preferred_over == task2.description:
        return task1.description
    else:
        return task2.description
        

