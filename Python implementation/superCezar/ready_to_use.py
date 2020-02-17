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
	
