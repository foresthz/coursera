#encoding=utf-8
'''
Created on 2014-7-13

@author: jack
'''
from os.path import dirname, basename
class ConfigMgr(object):
    def __init__(self):
        self.configFile = dirname(dirname(__file__)) + '/' + 'account.txt'
        self.parse()
        
    def parse(self):
        self.map=dict()
        for line in open(self.configFile):
            pair=line.split('=')
            self.set(pair[0], pair[1])
    
    def get(self, key):
        return self.map[key].strip()
    def set(self, key, value):
        self.map[key]=value

if __name__=='__main__':
    obj = ConfigMgr()
    print obj.get('username')
    print obj.get('password')