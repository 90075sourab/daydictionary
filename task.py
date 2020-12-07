from mod1 import *
from mod2 import *


param_dic1={"2020-01-01":4,"2020-01-02":4,"2020-01-03":6,"2020-01-04":8,"2020-01-05":2,
     "2020-01-06":-6,"2020-01-07":2,"2020-01-08":-2};

param_dic2={"2020-01-01":12,"2020-01-04":6,"2020-01-05":14,"2020-01-06":2,
     "2020-01-07":4};

def solution(D):
    dayval_dic=get_dayval_dic(D)
    '''this fuction count day , sum values and set None to
    day that not persent'''
    #print(dayval_dic)
    dayval_list=list(dayval_dic.values())
    #print(dayval_list)
    fillNone(dayval_list)
    return dict(zip(dayval_dic.keys(),dayval_list))

print(solution(param_dic1))
