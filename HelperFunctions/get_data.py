import pandas as pd

from StudyElements.Participant import Participant


def get_data(task_ids: list[int], participants: list[Participant]):
    data = []
    for task_id in task_ids:
        for p in participants:
            task = p.get_participant_task(task_id=task_id)
            if task is not None:
                data.append({
                    "id": f"task_{task.task_number}",
                    "group": p.studygroup.value,
                    "TTU": task.time_to_understand,
                    "DOU": task.degree_of_understanding,
                })
            else:
                raise Exception(f"missing task {p.id}_{task_id}")
    df = pd.DataFrame(data)
    return df