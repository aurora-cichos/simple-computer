def get_char(num):
    if num < 10:
        return str(num)
    elif num == 10:
        return 'a'
    elif num == 11:
        return 'b'
    elif num == 12:
        return 'c'
    elif num == 13:
        return 'd'
    elif num == 14:
        return 'e'
    elif num == 15:
        return 'f'
    else:
        return 'n'


def fancyprint(data):
    out = ''
    for section in range(int(len(data) / 4)):
        total = 0
        for i in range(4):
            total += data[4*section+i]*2**i
        out = get_char(total) + out
    print(out)
        
            

data = []

for i in range(16):
    data.append(0)

sig = {'x1': [0], 'x2': [1], 'x3': [2], 'x4': [3], 'x5': [4], 'x6': [5], 'x7': [6], 'x8': [7], 'x9_0': [8], 'x9_1': [9],
       'x10_0': [10], 'x10_1': [11], 'x11_0': [12], 'x11_1': [13], 'x12': [14], 'x13': [15]}
keys = sig.keys()

running = True

while running:
    inp = input('signal: ')

    if inp == 'q':
        running = False
    elif inp == 'print':
        fancyprint(data)
    elif inp == 'clear':
        for i in range(16):
            data[i] = 0
    elif inp in keys:
        for i in sig[inp]:
            data[i] = data[i] * (-1) + 1
    else:
        print('error: invalid input')

print(data)
