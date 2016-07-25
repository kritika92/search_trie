class node:
    def __init__(self,parent_key,is_word,word,is_leaf):
        self.children={}
        self.parent_key=parent_key
        self.is_word=is_word
        self.word=None
        self.is_leaf=is_leaf
        if(is_word):
            self.word=word
