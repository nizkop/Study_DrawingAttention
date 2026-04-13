from datetime import datetime, time

from Task import Task


class ParticipantTask(Task):

    def __init__(self, p_id:str, task:Task):
        super().__init__(number=task.task_number, max_total=task.task_max_total)
        self.p_id = p_id

        self.id = f"{self.p_id}-{self.task_number}"

        self.raw_data = {}

    def set_raw_data(self, raw_data:dict):
        if len(self.raw_data) > 0:
            return
        self.raw_data = raw_data

        #TODO separat abspeichern:
        start = self.raw_data["start (of new slide)"]
        if " " in start:
            start = start.split(" ")[-1]
        try:
            self.start = datetime.strptime(start, '%H:%M:%S').time()
        except Exception as e:
            print(e)
            self.start = start

        understanding = self.raw_data["timestamp where participant realizes"]
        if " " in understanding:
            understanding = understanding.split(" ")[-1]
        try:
            self.understanding = datetime.strptime(understanding, '%H:%M:%S').time()
        except Exception as e:
            print(understanding, flush=True)
            print(e)
            self.understanding = understanding

        time_diff = datetime.combine(datetime.min, self.start) - datetime.combine(datetime.min, self.understanding)
        self.time_to_understand = time_diff.total_seconds()


        self.understood_result_cell = raw_data["Result Cell understood (1 / 0)"]
        self.understood_result_type = raw_data["Result Type understood (1.0/0.5/0)"]
        self.understood_operation = raw_data["each operation understood (1 point for each)"]
        self.understood_operand = raw_data["each expected operand understood (1 point for each)"]

        self.total = [
            value if value != "x" and value is not None else 0
            for value in (
                *self.understood_operand.values(),
                *self.understood_operation.values(),
                *self.understood_result_type.values(),
                *self.understood_result_cell.values()
            )
        ]
        self.total = sum(self.total)

        self.notes = self.raw_data["notes"]
        return

    def get_degree_of_understanding(self):
        return self.total / self.task_max_total
