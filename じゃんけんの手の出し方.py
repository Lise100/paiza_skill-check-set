N, M = map(int, input().split())
s = input()

List = []

for kaisu_c in range(int(M / 2) + 1):
    nokori = M - 2 * kaisu_c

    if(nokori % 5 != 0):
        continue

    kaisu_p = int(nokori / 5)
    kaisu_g = N - (kaisu_c + kaisu_p)

    if(kaisu_g < 0 or kaisu_p < 0):
        continue

    if(kaisu_g <= s.count('C')):
        kachi_g = kaisu_g
    else:
        kachi_g = s.count('C')

    if(kaisu_c <= s.count('P')):
        kachi_c = kaisu_c

    else:
        kachi_c = s.count('P')

    if(kaisu_p <= s.count('G')):
        kachi_p = kaisu_p

    else:
        kachi_p = s.count('G')

    List.append(kachi_g + kachi_c + kachi_p)

print(max(List))