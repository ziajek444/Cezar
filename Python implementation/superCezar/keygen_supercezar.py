# generate key for super cezar
# generating basic key (24064 x 2B = 48128B)
# basic key have got 24064 unique sets saved at 16 bits (from 65 536 posibilities)
# 256 sets per 94 legal signs

import random
import os.path
import _decors
from ready_to_use import pop_string
from ready_to_use import conv_str2dict

_combinaltions = 256 # 95 * 256 = 24320 # 24064 old for 94 chars
_legal_chars = 97 # ASCII 32-126 # 18.02.2020 added space
_defElements = 24320
_defRange = (32,126)


# warning, do not try to print !!
@_decors.dcrt_ascii_list2dic # that decorator provide return dict instead of list.
def _generate_unique_list(amountElements=24320,rangeElements=(0,65536),seed=None):
    population = list(range(rangeElements[0],rangeElements[1]))
    k = amountElements
    random.seed(a=seed, version=2)
    uniqueList = random.sample(population, k)
    return uniqueList


def create_keys_files(ascii_range = (32,126), lseeds = []):
    if ascii_range[0] < 0 or ascii_range[1] > 255:
        raise Exception("not byte for ASCII")
    if ascii_range[1] < ascii_range[0]:
        ascii_range = ascii_range[::-1]
        
    length = ascii_range[1] - ascii_range[0] + 1
    if len(lseeds) > 0:
        if len(lseeds) < length:
            raise Exception("list of seeds is too short")
        else:
            pass
    else:
        lseeds = [None for x in range(length)]
        print('generated list of None for seeds')
        
        
    npath = "Keys/"
    if not os.path.exists(os.path.dirname(npath)):
        try:
            os.makedirs(os.path.dirname(npath))
        except OSError as exc: # Guard against race condition
            print("directory can not be created !")

    armin = ascii_range[0]
    armax = ascii_range[1]+1
    streamString = ""
    for numberOfKey in range(armin,armax):
        nameOfFile = npath + "unique_key_{}.key".format(numberOfKey)
        streamString = chr(numberOfKey) + str(_generate_unique_list(seed=lseeds[numberOfKey-armin])) + '\n'
        with open(nameOfFile, 'w') as KeyFile:
            KeyFile.write(streamString)

    print("done")


def create_prime_key_file(seed=None):
    npath = "Keys/"
    if not os.path.exists(os.path.dirname(npath)):
        try:
            os.makedirs(os.path.dirname(npath))
        except OSError as exc:  # Guard against race condition
            print("directory can not be created !")


    nameOfFile = npath + "prime_key.pkey"
    with open(nameOfFile, 'w') as KeyFile:
        KeyFile.write(str(_generate_unique_list(seed=seed)) + str('\n'))

    print("done")

def save_filekey_into_memory(path,isPrimeKey=False):
    nameOfFile = path
    rawKey = ""
    with open(nameOfFile, 'r') as KeyFile:
        rawKey = str(KeyFile.read())
    
    mainKey = ''
    if not isPrimeKey:
        mainKey, rawKey = pop_string(rawKey,0)
        
    newDict = conv_str2dict(rawKey)
    
    return mainKey, newDict

def create_keys_dicts(ascii_range = (32,126), lseeds = []):
    if ascii_range[0] < 0 or ascii_range[1] > 255:
        raise Exception("not byte for ASCII")
    if ascii_range[1] < ascii_range[0]:
        ascii_range = ascii_range[::-1]
        
    length = ascii_range[1] - ascii_range[0] + 1
    if len(lseeds) > 0:
        if len(lseeds) < length:
            raise Exception("list of seeds is too short")
        else:
            pass
    else:
        lseeds = [None for x in range(length)]
        print('generated list of None for seeds')
        
    armin = ascii_range[0]
    armax = ascii_range[1]+1
    streamString = ""
    for numberOfKey in range(armin,armax):
        nameOfFile = npath + "unique_key_{}.key".format(numberOfKey)
        streamString = chr(numberOfKey) + str(_generate_unique_list(seed=lseeds[numberOfKey-armin])) + '\n'
        with open(nameOfFile, 'w') as KeyFile:
            KeyFile.write(streamString)

    print("done")

# file needs to contain code
def reproduce_key(filePath = None, code = None):
    if (filePath == None and code == None) or (filePath != None and code != None):
        raise Exception("You need to pass one argument (code or filePath)")
    elif filePath != None:
        # read from file
        pass
    else:
        # read from code
        
    


if __name__ == "__main__":
    
    # CREATING KEYS
    create_keys_files()
    create_prime_key_file()

    # SAVING KEYS
    '''primeKeyPath = "Keys/prime_key.pkey"
    sign, nd = save_filekey_into_memory(primeKeyPath,True)
    print(sign,nd['x'])
    listOfDicts = []
    for e in range(33,127):
        uniqueKeyPath = "Keys/unique_key_"+str(e)+".key" 
        sign, nd = save_filekey_into_memory(uniqueKeyPath,False)
        if chr(e) == sign:
            listOfDicts.append(nd)
        else:
            raise Exception("Not perfect")
    print(listOfDicts[ord('G')]['='])'''
        
            
    
