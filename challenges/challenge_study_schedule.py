def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int):
        return None

    count = 0
    for entry_time, exit_time in permanence_period:
        if type(entry_time) != int or type(exit_time) != int:
            return None
        if entry_time <= target_time <= exit_time:
            count += 1
    return count
