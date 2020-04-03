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
        median=my_list_2[middle]
        #print median
    else:
        middle_1=my_list_2[int(n/2)]
        middle_2=my_list_2[int(n/2)+1]
        median=(middle_1+middle_2)/2
        #print median
    return median
