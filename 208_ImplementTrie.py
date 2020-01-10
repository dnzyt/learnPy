class Trie(object):
    def __init__(self):
        self.d = dict()

    def insert(self, word):
        p = self.d
        for w in word:
            if w not in p:
                p[w] = {}
            p = p[w]
        p['#'] = True

    def search(self, word):
        t = self.__find(word)
        return t is not None and '#' in t

    def startsWith(self, prefix):
        t = self.__find(prefix)
        return t is not None


    def __find(self, word):
        p = self.d
        for w in word:
            if w not in p:
                return None
            p = p[w]
        return p
