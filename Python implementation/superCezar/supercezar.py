__author__ = "Marcin Ziajkowski"
# supercezar.py
# main module

from keygen_supercezar import create_keys_files
from keygen_supercezar import create_prime_key_file
from keygen_supercezar import save_filekey_into_memory
from keygen_supercezar import read_code_from_file
from keygen_supercezar import reproduce_key
import random
import time
from ready_to_use import pop_string


_list_legal_chars = [chr(x) for x in range(32,126)] # from space to ~
_rand = random
_rand.seed(time.perf_counter_ns())

def _sc_get_random_legal_char():
    r = _rand.randint(0,len(_list_legal_chars)-1)
    return _list_legal_chars[r]

def _check_if_mess_is_legal(message):
    for e in message:
        if e in _list_legal_chars:
            pass
        else:
            raise Exception("illegal character")

def _sc_preformat_encode(message):
    p = _sc_get_random_legal_char()
    return p + message

def _get_inv_dict(dic):
    invDict = dict()
    for K in dic.keys():
        for e in dic[K]:
            invDict[e] = K
    return invDict

def _get_inv_list_dicts(ldicts):
    newListDicts = []
    for dic in ldicts:
        newListDicts.append(_get_inv_dict(dic))
    return newListDicts


# set verify to False for complex messages and try provide legal character in other way
# lowestChar is character (for example 'a')
def sc_encrypt(formattedMessage, listDict, lowestChar, verify=True):
    # checking if lkey is correct
    if verify:
        _check_if_mess_is_legal(formattedMessage)
    firstKey = list(listDict[0].keys()) # object dict_keys() is not subscriptable
    safety = len(listDict[0][firstKey[0]])
    if safety < 256:
        print("Key can be not strong enough,\nPlease consider create stronger key.",safety)
    
    fm = formattedMessage
    ld = listDict
    border = safety-1
    r = _rand.randint(0,border)
    emessage = ld[0][fm[0]][r]

    
    for key,e in zip(fm[:-1],fm[1:]):
        r = _rand.randint(0,border)
        emessage += ld[ord(key)-ord(lowestChar)+1][e][r]
        while(emessage[-2:] == emessage[-4:-2]):
            emessage = pop_string(emessage)[1]
            emessage = pop_string(emessage)[1]
            r = _rand.randint(0,border)
            emessage += ld[ord(key)-ord(lowestChar)+1][e][r]
            
    return emessage


# lowestChar is character (for example 'a')
def sc_decrypt(encryptedMessage, invListDict, lowestChar, complexity = 256):
    em = encryptedMessage
    ild = invListDict    

    # primary
    sign = em[0:2]
    emessage = ild[0][sign]

    # main message
    for e in range(2,len(em),2):
        sign = em[e:e+2]
        emessage += ild[ord(emessage[-1])-ord(lowestChar)+1][sign]

    return emessage


if __name__ == "__main__":
    # TEST DATA
    m="abcaaaaaaabbbbbbbccccccc"
    pr = {'a':['E1', 'A1', 'Q1', 'W1'], 'b':['R1', 'S1', 'D1', 'F1'], 'c':['X1', 'Z1', 'C1', 'V1']}
    da = {'a':['Z2', 'C2', 'X2', 'V2'], 'b':['F2', 'D2', 'S2', 'A2'], 'c':['R2', 'E2', 'W2', 'Q2']}
    db = {'a':['A3', 'Q3', 'Z3', 'W3'], 'b':['X3', 'S3', 'E3', 'D3'], 'c':['C3', 'R3', 'F3', 'V3']}
    dc = {'a':['E4', 'A4', 'Q4', 'W4'], 'b':['R4', 'S4', 'D4', 'F4'], 'c':['X4', 'Z4', 'C4', 'V4']}
    ld = [pr,da,db,dc]
    
    # _sc_preformat_encode TEST
    '''m1 = _sc_preformat_encode('message')
    print(m)
    m2 = _sc_preformat_encode('message')
    print(m)
    m3 = _sc_preformat_encode('message')
    print(m)
    m4 = _sc_preformat_encode('message')
    print(m)
    assert m1 != m2 != m3 != m4'''

    # ENCRYPT test
    '''for x in range(5):
        print(sc_encrypt(m,ld))'''

    # inverted listofdicts
    '''ild = _get_inv_list_dicts(ld)
    print(ild)'''

    # TEST DECRYPT
    em = sc_encrypt("abcabc", ld, 'a')
    ild = _get_inv_list_dicts(ld)
    mess = sc_decrypt(em, ild, 'a', 4)
    print(mess)
    

    
    
