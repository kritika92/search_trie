import os
import stat
import re
from node import node        
    
class trie:
    def __init__(self,prefixes,file_list):
        self.file_list=file_list
        self.root_hash={}
        self.prefixes=prefixes
     
    def add_files(self,file):
        self.file_list.append(file)
        
#     
    def get_words(self,mynode,prefix):
        if(mynode.is_leaf):
            print('one of the prefix for '+ prefix+ ' is '+mynode.word)
            
        else:
            if(mynode.is_word):
                print('one of the prefix for '+ prefix+ ' is '+mynode.word)
            list=[]
            list=mynode.children.values()
            for k in list:
                self.get_words(k,prefix)
                 
    def check_prefixes(self,prefix_list):
        word_list=[]
        temp_list=[]
        for i in prefix_list:
            temp_list.append(i.lower())
        prefix_list=temp_list
        for prefix in prefix_list:
            mynode=None
            if(self.root_hash.has_key(prefix[0])):
                        mynode=self.root_hash[prefix[0]]
                        if(len(prefix)==1):
                            self.get_words(mynode,prefix)
                
            else:
                print(prefix+' it doesnot exist')
                break
            for i in range(1,len(prefix)):
                    if(mynode.children.has_key(prefix[i])):
                        mynode=mynode.children[prefix[i]]
                        if(mynode.is_leaf==True and i+1!=len(prefix)):
                            print(prefix+' it doesnnot exist')
                            break
                        elif(mynode.is_leaf==True and i+1==len(prefix)):
                            print(prefix+' exists')
                            print(mynode.word)
                            break
                        elif(i== len(prefix)-1):
                            self.get_words(mynode,prefix)
                        else:
                            continue
        
                    else:
                        print(prefix+' it doesnt exist')
                        break
                   
                    
                        
            
       
            
    def make_node(self,prefix,letter_index):        
        if(len(prefix)==letter_index+1):
            new_node=node(prefix[letter_index],True,prefix,True)
            
        else:
            new_node=node(prefix[letter_index],False,prefix,False)
            
        return new_node    
            
                
    def make_trie(self):
        myhash=self.root_hash
        prefixes=self.prefixes
        for prefix in prefixes:
            prev_node=None
            if(self.root_hash!=None):
                        if(self.root_hash.has_key(prefix[0])):
                            parent_node=self.root_hash[prefix[0]]
                            if(len(prefix)==1):
                                parent_node.is_word=True
                                parent_node.word=prefix
                        else:
                            root_node=self.make_node(prefix,0)
                            self.root_hash[prefix[0]]=root_node
                            parent_node=root_node
                        prev_node=parent_node
            else:
                root_node=self.make_node(prefix,0)
                self.root_hash[prefix[0]]=root_node
                parent_node=root_node
                prev_node=parent_node
            for letter_index in range(1,len(prefix)):
                    if(letter_index==len(prefix)-1 and parent_node.children.has_key(prefix[letter_index])):
                        parent_node=parent_node.children[prefix[letter_index]]
                        if(parent_node.is_word==False):
                            parent_node.is_word=True
                            parent_node.word=prefix
                    elif(parent_node.children.has_key(prefix[letter_index])):
                        parent_node=parent_node.children[prefix[letter_index]]
                        prev_node=parent_node

                    else:
                        if(prev_node):
                            prev_node.is_leaf=False
                        child_node=self.make_node(prefix, letter_index)
                        parent_node.children[prefix[letter_index]]=child_node
                        parent_node=child_node
      
