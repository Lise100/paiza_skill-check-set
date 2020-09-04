import numpy as np

#入力
H, W, N = map(int, input().split())
haichi = [list(map(int, input().split())) for i in range(H)]
L = int(input())

Keii = [list(map(int, input().split())) for i in range(L)] #カードの配置は行列の方がイメージがつきやすかったため
Haichi = np.array(haichi) #選んだカードに関してはリストの方が扱いやすかった
seiseki = [0] * N #獲得したカード枚数を収納するリスト
player = 0 #現在のプレイヤーが誰であるかを判断するための変数

for i in range(L):
    kumi = Keii[i]
    
    if Haichi[kumi[0] - 1, kumi[1] - 1] == Haichi[kumi[2] - 1, kumi[3] - 1]:
        seiseki[player % N] += 2

    else:
        player += 1
        
#出力
for i in range(len(seiseki)):
    print(seiseki[i])