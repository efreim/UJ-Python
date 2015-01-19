# coding=utf-8

import lists


def heap_sort(my_list):
    heapify(my_list)

    for end in range(len(my_list) - 1, 0, -1):
        tmp = my_list[end]
        my_list[end] = my_list[0]
        my_list[0] = tmp
        sift_down(my_list, 0, end - 1)
    return my_list


def heapify(my_list):
    start = (len(my_list) - 2) / 2
    for item in range(start, -1, -1):
        sift_down(my_list, item, len(my_list) - 1)


def sift_down(my_list, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break
        if child + 1 <= end and my_list[child] < my_list[child + 1]:
            child += 1
        if my_list[root] < my_list[child]:
            tmp = my_list[root]
            my_list[root] = my_list[child]
            my_list[child] = tmp
            root = child
        else:
            break


def show(lst):
    print lst
    heap_sort(lst)
    print lst
    print


r_list = lists.random_list(20)
show(r_list)
as_list = lists.almost_sorted_list(20)
show(as_list)
asr_list = lists.almost_sorted_reversed_list(20)
show(asr_list)
g_list = lists.gauss_list(20)
show(g_list)
rr_list = lists.random_repeated_list(20)
show(rr_list)
