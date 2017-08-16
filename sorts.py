# -*- coding: utf-8 -*-
## 常见排序算法的python3实现


## 利用装饰器做预先判断
## 保证输入的L是数组类型
## 如果输入的L是空的或者只有一个元素则返回自己
## 否则按排序传入的排序方法进行排序
import functools
def prejudge(sort_func):
    @functools.wraps(sort_func)
    def judge(L):
        assert(type(L) == type([])) 
        if len(L) == 0 or len(L) == 1:
            return L
        else:
            return sort_func(L)

    return judge


## 插入排序：
## 对比模型，原数组上排序
## 优点：稳定
## 缺点：慢（O(n^2)）
@prejudge
def insert_sort(L):
    for i in range(1, len(L)):
        key = L[i]
        j = i-1
        while j>=0:
            if L[j] > key:
                L[j+1], L[j] = L[j], key
            j -= 1
    return L


## 冒泡排序
## 对比模型，原数组上排序
## 优点：稳定
## 缺点：慢（O(n^2)）
@prejudge
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]
    return L
                

## 直接选择排序
## 对比模型，原数组上排序
## 优点：稳定
## 缺点：慢（O(n^2)）
@prejudge
def select_sort(L):
    for i in range(len(L)):
        min_index = i
        for j in range(i+1, len(L)):
            if L[min_index] > L[j]:
                min_index = j
        L[min_index], L[i] = L[i], L[min_index]
    return L


## 归并排序
## 对比模型，非原数组上排序
## 优点：稳定，速度较快（O(nlogn)）
## 缺点：空间复杂度（O(n)）
@prejudge
def merge_sort(L):
##    if len(L) <= 1:
##        return L  
    left = merge_sort(L[:len(L)//2])
    right = merge_sort(L[len(L)//2:])
    
    i = j = 0
    result = []
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result += left[i:]
    result += right[j:] 
    return result






## 测试方法
def main(sort_func):
    ## 测试输入
    L0 = []
    L1 = [3]
    L = [4, 6, 1, 3, 9, 0, 3, 5]
    print(sort_func.__name__, 'testing...')
    for L in map(sort_func, [L0, L1, L]):
        print(list(L))


if '__main__' == __name__:
    main(insert_sort)
    main(bubble_sort)
    main(select_sort)
    main(merge_sort)
            
