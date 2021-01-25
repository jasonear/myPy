# -*- coding:utf-8 -*-
import time

#test1: 不加参数，默认就是time.localtime()返回的时间结构元组
print("test1: print time.asctime():",time.asctime())

#test2: time.loaltime() 本地时间
t1 = time.localtime()
print("test2: t1(localtime):",t1)
print("test2: time.asctime(t1):",time.asctime(t1))

#test3: time.gmtime() 格林威治标准时间
t2 = time.gmtime()
print( "test3: t2(gmtime):",t2)
print( "test3: time.asctime(t2):",time.asctime(t2))

#test4: 按time_struct,人工指定时间结构元组
t3 = [2018,5,27,1,5,27,6,147,-1]
print( "test4: t3:",t3)
#print( "test4: time.asctime(t3):",time.asctime(t3))

print("time.time(): %f " %  time.time())
print( time.localtime( time.time() ))
print( time.asctime( time.localtime(time.time()) ))