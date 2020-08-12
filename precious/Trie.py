
### Trie树


class Node:
    def __init__(self):
        self.dic = {}
        self.word_end = False

class Trie:
    def __init__(self):
        self.root = {}

    def insert_word(self, word, idx):
        if word == '': return
        cur_dic = self.root
        for char in word:
            cur_dic.setdefault(char, Node())
            ob = cur_dic[char]
            cur_dic = ob.dic
        ob.word_end = True
        ob.word_idx = idx

class Solution:
    def multiSearch(self, big, smalls):
        for i in range(len(big)):
            cur = self.trie.root
            for j in range(i, len(big)):
                if(big[j] in cur):
                    ob = cur[big[j]]
                    if(ob.word_end):
                        pass
                    cur = ob.dic
                else:
                    break


### Trie树

class Node:
    def __init__(self):
        self.char = [0]*26
        self.flag = -1

Trie = [Node()]

def insertWord(word, index):
    idx = 0
    for char in word:
        temp = ord(char)-ord('a')
        if(Trie[idx].char[temp] == 0):
            Trie.append(Node())
            Trie[idx].char[temp] = len(Trie)-1
        idx = Trie[idx].char[temp]
    Trie[idx].flag = index

def findWord(word):
    idx = 0
    for char in word:
        temp = ord(char)-ord('a')
        if(Trie[idx].char[temp] == 0):
            return -1
        idx = Trie[idx].char[temp]
    return Trie[idx].flag
