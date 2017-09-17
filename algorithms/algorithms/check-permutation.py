import functools

def checkpermutation(s1, s2):
    sum1 = functools.reduce(lambda x,y: x+y, 
                            map(lambda x: ord(x), s1))
    sum2 = functools.reduce(lambda x,y: x+y, 
                            map(lambda x: ord(x), s2))
    return sum1 == sum2

s1, s2 = "hello", "lehlo"

assert checkpermutation(s1, s2) == True

s1, s2 = "xydsfdgd", "fdgfdlloyt"
assert checkpermutation(s1, s2) == False
