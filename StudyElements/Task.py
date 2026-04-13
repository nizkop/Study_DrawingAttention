from enum import Enum


class RESULTTYPE(Enum):
    VALUE = "Single value"
    LIST = "List of Items"

class Task(object):

    def __init__(self, number:int, max_total:int,
                 description:str=None, formula:str=None,
                 expected_result_cell:str=None, expected_operations:list[str]=None, expected_operands:list[str]=None,
                 result_type:RESULTTYPE=None):
        self.task_number = number
        self.task_description = description
        self.task_formula = formula
        self.task_expected_result_cell = expected_result_cell
        self.task_expected_operations = expected_operations
        self.task_expected_operands = expected_operands
        self.task_result_type = result_type
        assert max_total >= 0
        self.task_max_total = max_total


    def get_excel_line(self):
        return 2 + int(self.task_number)


