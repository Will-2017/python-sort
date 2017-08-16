# -*- coding: utf-8 -*-
# 常见排序算法的python3实现
import functools
import random


# 利用装饰器做预先判断
# 保证输入的L是数组类型
# 如果输入的L是空的或者只有一个元素则返回自己
# 否则按排序传入的排序方法进行排序
def prejudge(sort_func):
    @functools.wraps(sort_func)
    def judge(*args):
        assert(type(args[0]) == type([]))
        if len(args[0]) == 0 or len(args[0]) == 1:
            return args[0]
        else:
            return sort_func(*args)

    return judge


# 插入排序：
# 对比模型，原数组上排序
# 优点：稳定
# 缺点：慢（O(n^2)）
@prejudge
def insert_sort(seq):
    for i in range(1, len(seq)):
        key = seq[i]
        j = i-1
        while j>=0:
            if seq[j] > key:
                seq[j+1], seq[j] = seq[j], key
            j -= 1
    return seq


# 冒泡排序
# 对比模型，原数组上排序
# 优点：稳定
# 缺点：慢（O(n^2)）
@prejudge
def bubble_sort(seq):
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if seq[i] > seq[j]:
                seq[i], seq[j] = seq[j], seq[i]
    return seq
                

# 直接选择排序
# 对比模型，原数组上排序
# 优点：稳定
# 缺点：慢（O(n^2)）
@prejudge
def select_sort(seq):
    for i in range(len(seq)):
        min_index = i
        for j in range(i+1, len(seq)):
            if seq[min_index] > seq[j]:
                min_index = j
        seq[min_index], seq[i] = seq[i], seq[min_index]
    return seq


# 归并排序
# 对比模型，非原数组上排序
# 优点：稳定，速度较快（O(nlogn)）
# 缺点：空间复杂度（O(n)）
@prejudge
def merge_sort(seq):
    left = merge_sort(seq[:len(seq)//2])
    right = merge_sort(seq[len(seq)//2:])
    
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


# 快速排序
# 对比模型，原数组上排序
# 时间复杂度：最坏的情况O(n**2)
# 空间复杂度：O(log n)
# 稳定性：不稳定
def partition(seq, left, right, pivot_index):
    pivot_value = seq[pivot_index]
    seq[pivot_index], seq[right] = seq[right], seq[pivot_index]
    store_index = left
    for i in range(left, right):
        if seq[i] < pivot_value:
            seq[i], seq[store_index] = seq[store_index], seq[i]
            store_index += 1
    seq[store_index], seq[right] = seq[right], seq[store_index]
    return store_index


@prejudge
def quick_sort_in_place(seq, left, right):
    if len(seq) <= 1:
        return seq
    elif left < right:
        pivot = random.randrange(left, right)
        pivot_new_index = partition(seq, left, right, pivot)
        quick_sort_in_place(seq, left, pivot_new_index - 1)
        quick_sort_in_place(seq, pivot_new_index + 1, right)
        return seq
    

# 测试方法
def main(sort_func):
    # 测试输入
    test_seq = list(range(15))
    random.shuffle(test_seq)
    print('test sequence: ',test_seq)
    print(sort_func.__name__, 'testing...')
    if sort_func != quick_sort_in_place:
        print(sort_func(test_seq))
    else:
        print(sort_func(test_seq, 0, len(test_seq)-1))
    print()


if '__main__' == __name__:
    main(insert_sort)
    main(bubble_sort)
    main(select_sort)
    main(merge_sort)
    main(quick_sort_in_place)
            
