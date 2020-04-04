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

my_list=get_n_random_numbers(5,-3,3)
my_hist_d=my_frequency_with_dict(my_list)
my_hist_list=my_frequency_with_list_of_tuples(my_list)


def my_mode_with_dict(my_hist_d):
    frequency_max=-1
    mode=-1
    for key in my_hist_d.keys():
        #print(key,my_hist_d[key])
        if my_hist_d[key]>frequency_max:
            frequency_max=my_hist_d[key]
            mode=key
    return mode,frequency_max

def my_mode_with_list(my_hist_list):
    frequency_max=-1
    mode=-1
    for item,frequency in my_hist_list:
        #print(item,frequency)
        if frequency>frequency_max:
            frequency_max=frequency
            mode=item
    return mode,frequency_max


print my_mode_with_list(my_hist_list)

def my_linear_search(my_list,item_search):
    found=(-1,1)
    n=len(my_list)
    for indis in range(n):
        if my_list[indis]==item_search:
            found=(my_list[indis],indis)
    return found

def my_mean(my_list):
    s,t=0,0
    for item in my_list:
        s+=1
        t+=item
    mean_=t/s
    return mean_

def my_bubble_sort(my_list):
    n=len(my_list)
    print my_list
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if not(my_list[j]<my_list[j+1])
            temp=my_list[j]
            my_list[j]=my_list[j+1]
            my_list[j+1]=temp
    return my_list

def my_binary_search(my_list,item_search):
    found=(-1,1)
    low=0
    high=len(my_list)-1
    while(low<=high):
        mid=(low+high)//2
        if my_list[mid]==item_search:
            return my_mean[mid],mid
        elif my_list[mid]>item_search:
            high=mid-1
        else:
            low=mid+1
    return found



size=input("dizi boyutunu gir:")
size=int(size)
my_list_1=get_n_random_numbers(size)
print("liste ",my_list_1)

def my_median(my_list):
    my_list_2=my_bubble_sort(my_list_1)
    #print my_list_2
    n=len(my_list_2,)
    if n%2==1:
        middle=int(n/2)+1
        median=my_list_2[middle-1]
        #print median
    else:
        middle_1=int(n/2)-1
        middle_2=middle_1+1
        median=(my_list_2[middle_1]+my_list_2[middle_2])/2
        #print median
    return median
