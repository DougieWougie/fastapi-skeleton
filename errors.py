class Missing(Exception):
    """Handle missing items"""
    def __init__(self, msg: str):
        self.msg = msg


class Duplicate(Exception):
    """Handle duplicated items"""
    def __init__(self, msg: str):
        self.msg = msg
