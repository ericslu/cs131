def foo(arr):
    print("Before: | ", arr)
    arr2=arr
    print_arrs("arr2 = arr", arr, arr2)
    arr += ['bean']
    print_arrs("arr += ['bean']", arr, arr2)
    arr[0] = 'chickpea'
    print_arrs("arr[0] = 'chickpea'", arr, arr2)
    arr = ['horchata']
    print_arrs("arr = ['horchata']", arr, arr2)
    arr.append('burrito' )
    print_arrs("arr.append('burrito')", arr, arr2)
    arr[1] = 'pasta'
    print_arrs("arr[1] = 'pasta'", arr, arr2)
    arr2[-1] = 'beet'
    print_arrs("arr2[-1] = 'beet'", arr, arr2)
    arr2 = arr2 + arr
    print_arrs("arr2 = arr2 + arr", arr, arr2)
    arr2.append('coconut')
    print_arrs("arr2.append('coconut')", arr, arr2)

def print_arrs(instruction, arr, arr2):
    print(instruction, '\nLocal Arr: ', arr, '\nLocal Arr2: ', arr2, '\n')

arr = ['apple', 'pear']
print('global arr:', arr)
foo(arr)
print('global arr:', arr)
