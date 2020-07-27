class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        n = max(len(version1), len(version2))

        for i in range(n):
            v1 = int(version1[i]) if i < len(version1) else None
            v2 = int(version2[i]) if i < len(version2) else None
            if v1 and not v2:
                return 1
            elif v2 and not v1:
                return -1
            elif v1 and v2:
                if v1 > v2:
                    return 1
                elif v1 < v2:
                    return -1
        return 0
