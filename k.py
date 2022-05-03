'''
def count_inversion(arr):
    inverse = 0
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]<arr[j]:
                break
            else:
                inverse+=1
    return inverse

print(count_inversion([1,20,6,4,5]))

'''

def merge(list_):
    if len(list_)>1:
        mid = len(list_)//2
        l_list = list_[:mid]
        r_list = list_[mid:]

        i = j = k = 0
        while i<len(l_list) and j<len(r_list):
            if l_list[i]<r_list[j]:
                list_[k] = l_list[i]
                i+=1
            else:
                list_[k] = r_list[j]
                j+=1
            k+=1
        while i<len(l_list):
            list_[k] = l_list[i]
            i+=1
            k+=1
        while j<len(r_list):
            list_[k] =r_list[j]
            j+=1
            k+=1
        merge(l_list)
        merge(r_list)


    




print(merge([4,3,1,2]))