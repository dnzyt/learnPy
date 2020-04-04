class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        visited = set()
        beginSet = set([beginWord])
        count = 1
        letters = 'abcdefghijklmnopqrstuvwxyz'
        if endWord not in wordList:
            return 0

        while len(beginSet) != 0:
            temp = set()
            for word in beginSet:
                for i in range(len(word)):
                    oldChr = word[i]
                    for c in letters:
                        word = word[:i] + c + word[i + 1:]
                        if word == endWord:
                            return count + 1
                        if word not in visited and word in wordList:
                            temp.add(word)
                            visited.add(word)
                    word = word[:i] + oldChr + word[i + 1:]
            count += 1
            beginSet = temp
        return 0

    def ladderLength2(self, beginWord, endWord, wordList):
        beginSet = set([beginWord])
        endSet = set([endWord])
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        letters = 'abcdefghijklmnopqrstuvwxyz'
        visited = set()
        count = 2

        while len(beginSet) != 0 and len(endSet) != 0:
            if len(beginSet) > len(endSet):
                t = beginSet
                beginSet = endSet
                endSet = t
            temp = set()
            for word in beginSet:
                for i in range(len(word)):
                    oldChr = word[i]
                    for l in letters:
                        word = word[:i] + l + word[i + 1:]
                        if word in endSet:
                            return count
                        if word not in visited and word in wordList:
                            visited.add(word)
                            temp.add(word)
                    word = word[:i] + oldChr + word[i + 1:]
            beginSet = temp
            count += 1
        return 0
