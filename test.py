#from collector import *
from copy import copy
from les3 import *
# b={'chongzhang': {'age': 18, 'word': {'wrong': {'fuck': (1.1, 1.2)}}, 'sex': 'gay'}}
# b['zhouhan']={'sex':'gay'}
# a=open('test','a+')
# a.write(repr(b))
# a.close()
# new = data('test')
# print type(new)
# print new

# c= basic_parser('input.txt').parser()
# print type(c)
# new.update(c)
# print new

# def foo():
# 	print 'original info is \n %s' %(info)
# 	p(info)
# 	print 'new info after mutation is \n %s'%(info)
# 	print_dict(info)
# a = data('mastertest.txt')
# f = lambda x: 'fuck you'
# a.update(f)
@trace
def foo(a='b',**kargs):
	print map(repr,kargs.items())
	print kargs

foo(a='b',c='d')
a = open('foo.txt','a+')
a.write('a\nbc')
a.close()