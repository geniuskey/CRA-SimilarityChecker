class Game:
    def run(self):
        pass

    def check_alpha(self, a, b) -> int:
        a_map = [False] * 26
        b_map = [False] * 26
        for c in a:
            index = ord(c) - ord('A')
            a_map[index] = True

        for c in b:
            index = ord(c) - ord('A')
            b_map[index] = True

        total_count, same_count = 0, 0
        for i in range(26):
            if a_map[i] or b_map[i]:
                total_count += 1
            if a_map[i] and b_map[i]:
                same_count += 1
        return int((same_count/total_count) * 40)
