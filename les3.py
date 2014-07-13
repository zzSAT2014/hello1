def matchset(pattern, text):
    "Match pattern at start of text; return a set of remainders of text."
    op, x, y = components(pattern)
    if 'lit' == op:
        return set([text[len(x):]]) if text.startswith(x) else null
    elif 'seq' == op:
        return set(t2 for t1 in matchset(x, text) for t2 in matchset(y, t1))
    elif 'alt' == op:
        return matchset(x, text) | matchset(y, text)
    elif 'dot' == op:
        return set(text[1:]) if len(text)> 0 else null
    elif 'oneof' == op:
        return set(t1 for char in x for t1 in matchset(char,text))
    elif 'eol' == op:
        return set(['']) if text == '' else null
    elif 'star' == op:
        return (set([text]) |
                set(t2 for t1 in matchset(x, text)
                    for t2 in matchset(pattern, t1) if t1 != text))
    else:
        raise ValueError('unknown pattern: %s' % pattern)



#----------------
# User Instructions
#
# Write the compiler for alt(x, y) in the same way that we 
# wrote the compiler for lit(s) and seq(x, y). 

'''
def matchset(pattern, text):
    op, x, y = components(pattern)
    if 'lit' == op:
        return set([text[len(x):]]) if text.startswith(x) else null
    elif 'seq' == op:
        return set(t2 for t1 in matchset(x, text) for t2 in matchset(y, t1))
    elif 'alt' == op:
        return matchset(x, text) | matchset(y, text)
'''

def lit(s): return lambda text: set([text[len(s):]]) if text.startswith(s) else null

def seq(x, y): return lambda text: set().union(*map(y, x(text)))

def alt(x, y): return lambda text: set.union(x(text),y(text))
        
null = frozenset([])

def test():
    g = alt(lit('a'), lit('b'))
    assert g('abc') == set(['bc'])
    return 'test passes'

#print test()

from functools import update_wrapper
from functools import wraps

def hii(func):
    def inner():
        hi()
    #print update_wrapper(hii,func)
    return inner
@ hii
def hi(): '''do nothing'''; print 'hi'

def decorator(d):
    def _d(f):
        return update_wrapper(d,f)
    update_wrapper(_d,d)
    return _d

def counts(f):
    counts.num = 0
    
    def _f(*args):
        counts.num+=1
        return f(*args)
    return _f

#@decorator
def trace(f):
    #print f
    indent = '  '
    trace.level = 0
    name = f.__name__
    @wraps(f)
    def d(*args,**kargs):
        print '%s===>%s(%s)' %(trace.level*indent,name,map(repr,args))
        try: 
            trace.level+=1
            result = f(*args,**kargs)

            print '%s %s<===%s( %s, %s)' %(trace.level*indent,result,name,map(repr,args),map(repr,kargs.items()))
        finally:
            trace.level -=1
        return result
    return d

def memo(f):
    cache={}
    @wraps(f)
    def _f(*args):
        if args in cache: return cache[args]
        else: result = cache[args]=f(*args); return result 
    return _f

def gay(f):
    @wraps(f)
    def _f(*args):
        print 'i am a gay'
        return f(*args)
    return _f

#@gay
@trace
@memo
def fibo(num):
    #fibo.num =1
    if num<2: return num
    return fibo(num-1)+fibo(num-2)


#print fibo.__name__


#print fibo(10)

