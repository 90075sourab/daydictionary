import math
#l=[1,2,None,None,None,8,10,9,None,None,8]

def fillNone(num_list):
    #this function find where None value start and where end
    #and pass start and end index,None count to setMean function with list 

    start_none=False
    count=0
    for i in range(0,len(num_list)):
        if num_list[i]==None and start_none==False:
            start_index=i
            start_none=True
            count+=1
        elif(num_list[i]==None and start_none==True):
            count+=1
            continue
        elif(num_list[i]!=None and start_none==True):
            end_index=i-1
            start_none=False
            
            setMean(num_list,start_index,end_index,count)
    #return start_index,end_index

def setMean(num_list,start_index,end_index,count):
    '''this function take first and last
    None value index and put mean to all of them
    
    '''
    f_num=num_list[start_index-1]
    l_num=num_list[end_index+1]
    diff=math.floor((l_num-f_num)/(count+1)) if l_num>f_num else -math.floor((f_num-l_num)/(count+1))
    #print(f_num,l_num,diff)
    for i in range(start_index,end_index+1):
        num_list[i]=num_list[i-1]+diff
         

#print(setNone(l))
#print(l)


