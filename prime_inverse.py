def is_proper(num: int, den: int) -> bool:
    if num >= den:
        return False
    return True


print(is_proper(200, 39))
