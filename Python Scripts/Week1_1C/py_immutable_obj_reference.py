def foo(arr):
    print("before", arr)
    arr2=arr
    print("arr2=arr", arr, arr2)
    arr += ['bean']
    print("arr += ['bean']", arr, arr2)
    arr[0] = 'chickpea'
    print("arr[0] = 'chickpea'", arr, arr2)
    arr = ['horchata']
    print("arr = ['horchata']", arr, arr2)
    arr.append('burrito' )
    print("arr.append('burrito' )", arr, arr2)
    arr[1] = 'pasta'
    print("arr[1] = 'pasta'", arr, arr2)
    arr2[-1] = 'beet'
    print("arr2[-1] = 'beet'", arr, arr2)
    arr2 = arr2 + arr
    print("arr2 = arr2 + arr", arr, arr2)
    arr2.append(' coconut' )
    print("arr2.append(' coconut' )", arr, arr2)

arr = ['apple', 'pear']
print(arr)
foo(arr)
print(arr)
