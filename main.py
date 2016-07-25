import os
import stat
import re

from directory_to_list import directory_to_list
from trie import trie

dirfilepath=input('type the filepath of the directory: ')
dir_to_list=directory_to_list(dirfilepath)
dir_to_list.setprefixes()
myprefix=dir_to_list.get_myprefix()

file_list=dir_to_list.get_file_list()
our_trie=trie(myprefix,file_list)
our_trie.make_trie()

#The prefix/words to search
a=[]
a.append('a')
a.append('As')
our_trie.check_prefixes(a) 