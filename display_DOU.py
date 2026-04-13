
from Participant import Participant
from basic_boxplot import basic_boxplot

def display_DOU(task_ids: list[int], participants: list[Participant]):
    if participants is None:
        raise ValueError("Participants list must be provided.")

    x_values = []
    y_values = []

    for task_id in task_ids:
        x_values.append(task_id)
        y_values.append([])
        for p in participants:
            task = p.get_participant_task(task_id=task_id)
            if task is not None:
                y_values[-1].append(task.degree_of_understanding)
            else:
                raise Exception(f"missing task {p.id}_{task_id}")

    fig, ax = basic_boxplot(x_values=x_values, y_values=y_values,
                  y_label="Degree of Understanding [ ]", x_label="Task ID")

