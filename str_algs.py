def str1(arr):
    length = len(arr)
    arr1 = ''
    for i in range(len(arr)):
        a = length - i-1
        arr1 += arr[a]
    return arr1


if __name__ == "__main__":
    arr = "hello, world"
    print(arr)
    print(str1(arr))

