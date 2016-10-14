def min(arr):
    min = arr[0]
    for i in arr:
        if min > i:
            min = i
    return min


def average(arr):
    average = 0
    for i in arr:
        average = average + i
    count = len(arr)
    return average / count


if __name__ == "__main__":
    arr = list(range(1,5))
    arr2 = [5,6,4,3]
    print(arr)
    print('Минимум ' + str(min(arr)))
    print('Среднее ' + str(average(arr)))
    print(arr2)
    print('Минимум ' + str(min(arr2)))
    print('Среднее ' + str(average([5,6,4,3])))