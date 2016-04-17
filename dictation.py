#coding=utf-8
import random
f=open('马立平1.txt')
s=f.read()
f.close()
chars=sorted([k for k in set(s.decode('utf-8')) if u'\u4e00' <=k <=u'\u9fff'])
print ' '.join(chars)
print len(chars)
random.shuffle(chars)
print ' '.join(chars[0:10])
