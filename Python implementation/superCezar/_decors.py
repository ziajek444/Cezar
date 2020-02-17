# _decors.py
# decorators
__author__ = "Marcin Ziajkowski"

def dcrt_ascii_list2dic(func):
    def decorator(*args, **kwargs):
        uniqueList = func(*args, **kwargs)
        uniqueDict = dict()
        
        for i,c in zip(range(127-33), range(33,127)): # 33-126
            character = chr(c)
            f = 0+(256*i)
            t = f+256
            uniqueDict[character] = uniqueList[f:t]
        return uniqueDict
    return decorator
    
