n, m = map(int, input().split()) #(座席数, グループ数)
uchiwake = [list(map(int, input().split())) for i in range(m)] #[グループの人数, 着席開始座席番号]のリスト

ninzu = 0
List = list(range(1, n + 1)) #空いている座席番号のリスト

for i in range(m):
    group = uchiwake[i]
    bango_list_0 = list(range(group[1], group[1] + group[0])) #上限を無視した現グループの座席番号
    bango_list_1 = [i - n if i > n else i for i in bango_list_0] #上限を考慮した現グループの座席番号

    if set(bango_list_1) <= set(List): #集合を用いてList内にbango_list_1が含まれているか
        ninzu += group[0]
        for j in range(len(bango_list_1)):
            List.remove(bango_list_1[j]) #埋まった席をListから削除
        
print(ninzu)