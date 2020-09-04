#入力
H, W = map(int, input().split())
banmen = [input() for i in range(H)]

for i in range(H):
    for j in range(W):
        
        #0行目
        if i == 0 and banmen[1][j] == "#":
            if (j == 0 and banmen[0][1] == "#") or (j == W - 1 and banmen[0][W - 2] == "#"): #左上と右上
                print(i, j)
                
            if 0 < j < W - 1 and banmen[0][j - 1] == "#" and banmen[0][j + 1] == "#":
                print(i, j)
        
        #i行目        
        if 0 < i < H - 1 and banmen[i - 1][j] == "#" and banmen[i + 1][j] =="#":
            if (j == 0 and banmen[i][1] == "#") or (j == W - 1 and banmen[i][W - 2] == "#"): #左端と右端
                print(i, j)
                
            if 0 < j < W - 1 and banmen[i][j - 1] == "#" and banmen[i][j + 1] == "#":
                print(i, j)
        
        #H-1行目        
        if i == H - 1 and banmen[H - 2][j] == "#":
            if (j == 0 and banmen[H - 1][1] == "#") or (j == W - 1 and banmen[H - 1][W - 2] == "#"): #左下と右下
                print(i, j)
                
            if 0 < j < W - 1 and banmen[H - 1][j - 1] == "#" and banmen[H - 1][j + 1] == "#":
                print(i, j)