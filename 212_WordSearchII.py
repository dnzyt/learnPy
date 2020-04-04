import collections

class TrieNode:
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.isWord = False
        self.word = ''
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        cur = self.root
        for w in word:
            cur = cur.child[w]
        cur.isWord = True
        cur.word = word

class Solution(object):
    def findWords(self, board, words):
        res = []
        trie = Trie()
        for word in words:
            trie.insert(word)
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                self._def(board, i, j, trie.root, res)
        return res



    def _def(self, board, i, j, root, res):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        val = board[i][j]
        cur = root.child.get(val)

        if not cur:
            return
        if cur.isWord:
            cur.isWord = False
            res.append(cur.word)

        board[i][j] = '#'
        self._def(board, i + 1, j, cur, res)
        self._def(board, i - 1, j, cur, res)
        self._def(board, i, j + 1, cur, res)
        self._def(board, i, j - 1, cur, res)
        board[i][j] = val



