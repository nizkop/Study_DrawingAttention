from enum import Enum


class RESULTTYPE(Enum):
    VALUE = "Single value"
    LIST = "List of Items"

class Task(object):

    def __init__(self, number:int, description:str, formula:str,
                 expected_result_cell:str, expected_operations:list[str], expected_operands:list[str],
                 result_type:RESULTTYPE, max_total:int):
        self.number = number
        self.description = description
        self.formula = formula
        self.expected_result_cell = expected_result_cell
        self.expected_operations = expected_operations
        self.expected_operands = expected_operands
        self.result_type = result_type
        assert max_total >= 0
        self.max_total = max_total
