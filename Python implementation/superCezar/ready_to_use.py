__author__ = "Marcin Ziajkowski"
# ready_to_use.py
# ready to use
# conv_str2dict
# pop_string

def conv_str2dict(s):
    newDict = dict(eval(s))
    return newDict

def pop_string(s,index=-1):
	l = len(s)
	if l == 0:
		raise Exception("nothing to pop")
	if index >= l:
		raise Exception("unreachable index")
	if index < 0 and abs(index) > l:
		raise Exception("unreachable index (-)")
	popped = s[index]
	if l == 1:
		s = ""
	elif index == -1:
		s=s[:-1]
	else:
		s = s[0:index] + s[index+1:]
	return popped, s

def conv_dec2four_byte_bin(dec):
    if dec > 0xffffffff:
        raise Exception("Value too large")
    bin32 = bin(dec)[2:]
    diff = 32 - len(bin32)
    bin32 = '0b' + '0'*diff + bin32
    return bin32

def split_number2four_bytes_numbers(number):
    list4BytesNumbers = []
    binNumber = bin(number)
    binNumber = binNumber[2:]
    while(not len(binNumber)%32 == 0):
        binNumber = '0' + binNumber
    binNumber = binNumber

    if len(binNumber) < 32:
        raise Exception("to short number")
    
    for byte in range(0,len(binNumber),32):
        list4BytesNumbers.append('0b'+binNumber[byte:byte+32])
    list4BytesNumbers = list(map(lambda x: int(x,2), list4BytesNumbers))
        
    return list4BytesNumbers


print(conv_dec2four_byte_bin(8))

print(split_number2four_bytes_numbers(0x0000000f0000000f))

