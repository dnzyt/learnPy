class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        pathlist = path.split('/')
        for p in pathlist:
            if p:
                if p == '.':
                    continue
                elif p == '..':
                    if res:
                        res.pop()
                else:
                    res.append(p)
        return '/' + '/'.join(res)
