from enum import Enum


class STRUCTURALTASKASPECT(Enum):
    # see Table 3.3 ("Structural aspects of tasks used in the study")
    COMP = "Comp (Operation type)"
    COND = "Cond (Operation type)"
    LOOK = "Look (Operation type)"

    CELL = "Cell (Operand type)"
    RANGE = "Range (Operand type)"
    LIT = "Lit (Operand type)"
    FUNC = "Func (Operand type)"

    VAL = "Val (Result type)"
    BATCH = "Batch (Result type)"
    LIST = "List (Result type)"

    BACK = "Back (Ref. direction)"
    FORWARD = "Forward (Ref. direction)"

    ON = "On (Ref. dispersion)"
    OFF = "Off (Ref. dispersion)"
    CROSS = "Cross (Ref. dispersion)"

    # LEN = "Len (Expression Size)"
    # DEPTH = "Depth (Expression Size)"

    # yellow marked values (more important):
    iCOMP = "Comp (Operation type)"
    iCOND = "Cond (Operation type)"
    iLOOK = "Look (Operation type)"

    iCELL = "Cell (Operand type)"
    iRANGE = "Range (Operand type)"
    iLIT = "Lit (Operand type)"
    iFUNC = "Func (Operand type)"

    iVAL = "Val (Result type)"
    iBATCH = "Batch (Result type)"
    iLIST = "List (Result type)"

    iBACK = "Back (Ref. direction)"
    iFORWARD = "Forward (Ref. direction)"

    iON = "On (Ref. dispersion)"
    iOFF = "Off (Ref. dispersion)"
    iCROSS = "Cross (Ref. dispersion)"