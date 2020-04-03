import random

def get_n_random_numbers(n,min,max):
    numbers=[]
    for i in range(n):
        numbers.append(random.randint(min,max))
    return numbers

def my_frequency_with_dict(list):
    frequenct_dict={}
    for item in list:
        if(item in frequenct_dict):
            frequenct_dict[item]=frequenct_dict[item]+1
        else:
            frequenct_dict[item]=1
    return frequenct_dict

def my_frequency_with_list_of_tuples(list):
    frequenct_list=[]
    for i in range(len(list)):
        s=False
        for j in range(len(frequenct_list)):
            if(list[i]==frequenct_list[j][0]):
                frequenct_list[j][1]=frequenct_list[j][1]+1
                s=True
        if(s==False):
            frequenct_list.append([list[i],1])
    return frequenct_list

#my_list=get_n_random_numbers(7,0,7)
#print my_frequency_with_dict(my_list)
#print my_frequency_with_list_of_tuples(my_list)
