import numpy as np

input_array = np.random.randint(low=1, high=1000000, size=10000)

with open('input_array.py', 'w') as f:
    f.write('input_array = [')
    for i in range(len(input_array)):
        num = input_array[i]
        f.write(str(num))
        if  i < len(input_array) - 1:
            f.write(', ')
    f.write(']')