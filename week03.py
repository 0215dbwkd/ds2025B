import array

arr = array.array('f',[11, 9, -77, 8])

for i in range(len(arr)):
    print(f"{arr[i]:3} {id(arr[i])}")

#print(arr[2])

#print(f"{array[0]:3} {id(array[0])}")
#print(f"{array[1]:3} {id(array[1])}")
#print(f"{array[2]:3} {id(array[2])}")
#print(f"{array[3]:3} {id(array[3])}")