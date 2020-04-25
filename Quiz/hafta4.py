#Aldığı parametreyi çocukları ile karşılaştırıp küçüğü bulur ve sıralar.
def min_heapify(array, i):
    left = 2*i + 1
    right = 2*i +  2
    length = len(array)-1
    smallest = i
    if left <=length and array[i]>array[left]:
        smallest = left
    if right <=length and array[smallest]>array[right]:
        smallest = right
    if smallest !=i:
        array[i],array[smallest] =array[smallest], array[i]
        min_heapify(array,smallest)

#Dizideki tüm elemanlara heapify uygular
def build_min_heap(array):
    for i in reversed(range(len(array)//2)):
        min_heapify(array,i)

#Listeyi heap yapısına çevirir
#Kök ile son elemanın yerini değiştirir, son elemanı yeni listeye ekler ve listeden siler ardından heapify yapar
def heapSort(array):
    array = array.copy()
    build_min_heap(array)
    sorted_array=[]
    for i in range(len(array)):
        array[0],array[-1] = array[-1],array[0]
        sorted_array.append(array.pop())
        min_heapify(array,0)
    return sorted_array

#gönderilen parametreyi gönderilen diziye ekler
def Insert_item(heap,item):
    for i in range(len(my_heap)):
        if heap[i] == item:
           print("Sayi zaten var")
           return heap
    heap.append(item)
    build_min_heap(heap)
    return heap

#dizinin son elemanını siler
def remove_item(heap):
    if len(heap)<=0:
        print("Heap boş")
        return
    heap.pop()

array = [8,10,3,4,7,15,1,2,16]
build_min_heap(array)
print array
Insert_item(array,10)
Insert_item(array,49)
Insert_item(array,23)
remove_item(array)
remove_item(array)
