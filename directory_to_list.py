import os
import stat
import re
from trie import trie

class directory_to_list:
    def __init__(self,dir_filepath):
        self.__filepath=dir_filepath
        self.__file_list=[]
        
        self.__myprefix=[]
    def setprefixes(self):
        prefixes=[]
        for filename in os.listdir(self.__filepath):
            path=os.path.join(self.__filepath, filename)
            file = open(path, 'r')
            self.set_file_list(file) 
            filestr=file.read()
            str_without_special_ch=re.sub('[^A-Za-z0-9]+', ' ', filestr)
            if(prefixes==None):
                prefixes=str_without_special_ch.lower()
            else:
                prefixes.append(str_without_special_ch.lower())        
            file.close()
        j=0
        for i in prefixes:
            for k in i.split(" "):
                self.__myprefix.append(k)

    def get_myprefix(self):
        return self.__myprefix
        
    def set_file_list(self,file):
        self.__file_list.append(file)
    def get_file_list(self):
        return self.__file_list