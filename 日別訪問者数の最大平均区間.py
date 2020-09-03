#入力
n, k = map(int, input().split())
ninzu_uchiwake = list(map(int, input().split()))

#初期値
kaishibi = 1
ninzu_0 = sum(ninzu_uchiwake[0 : k])
List = [ninzu_0]

#訪問者数候補の追加と開始日の更新
for i in range(1, n - k + 1):
    ninzu_1 = sum(ninzu_uchiwake[i : i + k])
    List.append(ninzu_1)
    
    if ninzu_0 < ninzu_1:
        ninzu_0 = ninzu_1
        kaishibi = i + 1
        
#出力
print(List.count(max(List)), kaishibi)