import sys

def my_frequency_with_dict(my_list):
    frequenct_dict={}
    for i in my_list:
        if(i in frequenct_dict):
            frequenct_dict[i]=frequenct_dict[i]+1
        else:
            frequenct_dict[i]=1
    return frequenct_dict

def mean(my_list):
    s,t=0,0
    for item in my_list:
        s+=1
        t+=item
    mean=t/s
    return mean

def bubble_sort(my_list):
    for i in range(len(my_list)-1,-1,-1):
        for j in range(0,i):
            if not(my_list[j]<my_list[j+1]):
                temp=my_list[j]
                my_list[j]=my_list[j+1]
                my_list[j+1]=temp
    return my_list

def median(my_list):
    list2=bubble_sort(list1)
    n=len(list2)
    if n%2==1:
        middle=int(n/2)+1
        median=list2[middle-1]
        print median
    else:
        middle1=int(n/2)-1
        middle2=middle1+1
        median=(list2[middle1]+list2[middle2])/2
        print median
    return median

list=[]

with open(sys.argv[1]+"input_hw_2.csv","r") as file:
    for line in file:
        list.append(int(line.split(";")[3].split("-")[1]))
print list

histogram=my_frequency_with_dict(list)
print histogram
for i in histogram:
    list2.append(histogram[i])
list3=bubble_sort(list2)

dosya1=open(sys.argv[2]+"180401015_hw_2_output.txt", "w")
dosya1.write("Medyan "+str(median(list3))+"\n")
dosya1.write("Ortalama "+str(mean(list3)))
