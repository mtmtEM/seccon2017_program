# python3
# Vigenere3d(ヴィジュネル3d暗号)


def Decrypt():
    # 鍵
    key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz_{}'
    # 暗号文
    cipher = 'POR4dnyTLHBfwbxAAZhe}}ocZR3Cxcftw9'
    # フラグ形式
    flag = 'SECCON{'
    ans = ['0']
    # 暗号文と平文の文字の差を決定
    for j in range(len(flag)):
        for index_key in range(len(key)):
            if flag[j] == key[index_key]:
                break
        for index_C in range(len(key)):
            if cipher[j] == key[index_C]:
                break
        if index_key - index_C > 0:
            index_flag = len(key) - (index_key - index_C) + 1
        else:
            index_flag = index_C - index_key + 1
        ans.append(index_flag)
    del ans[0]

    # 復号
    plane = ['0']
    order = 0
    add = 1
    for k in range(len(cipher)):
        for index_C in range(len(key)):
            if cipher[k] == key[index_C] and index_C != len(key):
                index = index_C + 1
                break
            if cipher[k] == key[index_C] and index_C == len(key):
                index = 0
                break
        if order == len(ans):
            order = order - 1
            add = -1
        elif order == -1:
            order = order + 1
            add = 1
        if index - ans[order] < 0:
            plane.append(key[index + len(key) - ans[order]])
        else:
            plane.append(key[index - ans[order]])
        order = order + add

    del plane[0]
    decrypt = ''.join(plane)
    print(decrypt)


if __name__ == '__main__':
    Decrypt()
