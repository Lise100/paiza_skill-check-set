#入力
X, Y, N = map(int, input().split())

#リスト同士の足し算を行いたいため
import numpy as np

#進む方向のリスト
hogaku = []
for i in range(int(N / 4 + 1)):
    hogaku.append("E")
    if len(hogaku) == N:
        break
    hogaku.append("S")
    if len(hogaku) == N:
        break
    hogaku.append("W")
    if len(hogaku) == N:
        break
    hogaku.append("N")
    if len(hogaku) == N:
        break
    
#各方角に進むための関数
def hokotenkan(D):
    if D == "E":
        return np.array([1, 0])
    if D == "S":
        return np.array([0, 1])
    if D == "W":
        return np.array([-1, 0])
    if D == "N":
        return np.array([0, -1])
        
#歩数のリスト
hosu = [1, 1]
for i in range(9):
    hosu += [i + 2, i + 2]
    
#初期位置と歩いた回数のカウント
genzai = np.array([X, Y])
kaisu = 0

break_loop = False
for i in range(len(hogaku)):
    for j in range(hosu[i]):
        genzai += hokotenkan(hogaku[i])
        kaisu += 1
        if kaisu == N:
            break_loop = True
            break
    if break_loop:
        break
    
#出力
print(genzai[0], genzai[1])