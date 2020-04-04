class Solution:
    def slidingPuzzle(self, board):
        moves = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        used = set()
        s = "".join([str(c) for row in board for c in row])
        q = [(s, s.index("0"))]
        count = 0
        while q:
            temp = []
            for s, i in q:
                if s == "123450":
                    return count

                arr = [c for c in s]
                for move in moves[i]:
                    newarr = arr[:]
                    newarr[i], newarr[move] = newarr[move], newarr[i]
                    news = "".join(newarr)
                    if news not in used:
                        temp.append[news]
            count += 1
        return -1
