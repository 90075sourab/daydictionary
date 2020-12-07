from datetime import datetime
'''
param_dic={"2020-01-01":4,"2020-01-02":4,"2020-01-03":6,"2020-01-04":8,"2020-01-05":2,
     "2020-01-06":-6,"2020-01-07":2,"2020-01-08":-2};

param_dic={"2020-01-01":4,"2020-01-02":4,"2020-01-03":6,"2020-01-04":8,"2020-01-05":2,
     "2020-01-06":-6,"2020-01-08":-2};

'''
def getDay(d_str):
   d_format="%Y-%m-%d"
   d=datetime.strptime(d_str,d_format)
   return d.strftime('%a');

def  get_dayval_dic(param_dic):
   
   blank_days_dic={"Mon":0,"Tue":0,"Wed":0,"Thu":0,"Fri":0,"Sat":0,"Sun":0}
   all_days=list(blank_days_dic.keys())
   not_found_days=list(set(all_days)-set(list(map(getDay,param_dic.keys()))))
   #print("found",found_days)
   for key in param_dic:
       blank_days_dic[getDay(key)]+=param_dic[key]
   #print(found_days)
   for key in blank_days_dic:
      if key in not_found_days:
         blank_days_dic[key]=None
         
         
   #print(temp)
   return blank_days_dic
'''
def setRestNone(cal_dic,param_dic):
    all_days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    days_have=list(map(getDay,param_dic.keys()))
    #days_dont_have=set(all_days)-set(days_have)
    for val in all_days:
        if val not in days_have:
            cal_dic[val]=None;
    return cal_dic
        
    
'''
'''


a=getDayValDic(param_dic)
print(a)
pr_dic=setRestNone(a,param_dic)
values=list(pr_dic.values());
print(remNone(values))
print(values)
#print(None)

'''
    
#l=[1,0,0,0,3]


#for val in range(l[0],l[-1]+1):
 #print(val)


'''


def D(param_dic):
    dayval_dic=get_dayval_dic(param_dic)
    dayval_list=list(dayval_dic.values())
    print(dayval_list)
    fillNone(dayval_list)
    return dict(zip(dayval_dic.keys(),dayval_list))
print(D(param_dic))
    
'''
   
