def to_do(task_list):
    if task_list == None:
        raise Exception("No task list provided")
    elif "#TODO" in task_list:
        return "Yes, you have something #TODO"
    elif task_list == "":
        raise Exception("The task list is empty")
    else:
        return "No, you have nothing to do"