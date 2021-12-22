def shell_sort(alist):

    n = len(alist)

    # 初始步长

    gap = n / 2

    gap = int(gap)
    while gap > 0:

        # 按步长进行插入排序

        for i in range(gap, n):

            j = i

            # 插入排序

            while j>=gap and alist[j-gap] > alist[j]:

                alist[j-gap], alist[j] = alist[j], alist[j-gap]

                j -= gap

        # 得到新的步长

        gap = gap / 2
        gap = int(gap)


alist = [49,58,65,97,26,13,27,49,55,4]

shell_sort(alist)

print(alist)