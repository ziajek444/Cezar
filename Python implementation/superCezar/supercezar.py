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


_list_legal_chars = [chr(x) for x in range(32,126)] # from space to ~
_rand = random
_rand.seed(time.perf_counter_ns())

def _sc_get_random_legal_char():
    r = _rand.randint(0,len(_list_legal_chars)-1)
    return _list_legal_chars[r]

def _sc_preformat_encode(message):
    p = _sc_get_random_legal_char()
    return p + message

if __name__ == "__main__":
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

    

    
    
