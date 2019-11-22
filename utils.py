import numpy as np

def read_muban(filename):
    result = []
    with open(filename, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            tmp = np.array(line.split(';'))
            tmp_array = []
            for key in tmp[0:]:
                tmp_array.append(key)
            result.append(np.array(tmp_array))
    return np.array(result)

def read_formula(filename):
    result = []
    with open(filename, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            tmp = np.array(line.split(';'))
            tmp_array = np.zeros((tmp.shape[0], 2), dtype=int)
            cnt = 0
            for key in tmp[0:]:
                tmp_array[cnt][0] = key.split(',')[0]
                tmp_array[cnt][1] = key.split(',')[1]
                cnt  = cnt + 1
            result.append(np.array(tmp_array))
    return np.array(result)


if __name__ == '__main__':
    filename = 'H:\\work\\code\\python\\gui\\excel\\pyGUI\\doc\\模板.txt'
    filename2 = 'H:\\work\\code\\python\\gui\\excel\\pyGUI\\doc\\公式.txt'
    # result = read_muban(filename)
    result = read_formula(filename2)
    print('end')
