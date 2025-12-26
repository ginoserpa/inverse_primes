from tkinter.constants import FALSE, TRUE


def is_proper(num:int, den:int) -> bool:
    if num >= den:
        return FALSE
    return TRUE
