class Game:
    def run(self):
        pass

    def check_length(self, a, b) -> int:
        la, lb = len(a), len(b)
        if len(a) == len(b):
            return 60
        if la >= lb * 2 or lb >= la * 2:
            return 0
        gap = abs(la - lb)
        return int((1 - gap / lb) * 60)
