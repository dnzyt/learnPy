class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        s = set([start])
        q = [start]
        count = 0
        while q:
            count += 1
            node = []
            for item in q:
                for i in range(len(item)):
                    for c in ['A', 'C', 'G', 'T']:
                        newStr = item[:i] + c + item[i + 1:]
                        if newStr not in bank:
                            continue
                        if newStr in s:
                            continue
                        if newStr == end:
                            return count
                        if newStr in bank:
                            s.add(newStr)
                            node.append(newStr)
            q = node
        return -1
