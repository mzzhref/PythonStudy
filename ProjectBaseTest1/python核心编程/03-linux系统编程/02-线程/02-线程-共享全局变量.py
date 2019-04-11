#coding:utf-8

from threading import Thread
import time

# g_num=100

# def work1():
#     global g_num
#     for i in range(3):
#         g_num+=1

#     print('---in work1,g_num is %d'%g_num)

# def work2():
#     global g_num
#     print('---in work2,g_num is %d'%g_num)

# if __name__=='__main__':    
#     print('---线程创建之前g_num is %d'%g_num)

#     t1=Thread(target=work1)
#     t1.start()

#     #延迟一会，保证t1线程中的事情做完
#     time.sleep(1)

#     t2=Thread(target=work2)
#     t2.start()


#列表当做实参传递到线程中
def work1(nums):
    nums.append(44)
    print('---in work1---',nums)

def work2(nums):
    #延迟一会，保证t1线程中的事情做完
    time.sleep(1)
    print('---in work2---',nums)

g_nums=[11,22,33]

if __name__=="__main__":
    t1=Thread(target=work1,args=(g_nums,))
    t1.start()

    t2=Thread(target=work2,args=(g_nums,))
    t2.start()