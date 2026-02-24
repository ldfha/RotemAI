'''
26 5
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
25
Raichu
3
Pidgey
Kakuna
'''
def reverse_dict(dictionary):
    return dict(map(reversed, dictionary.items()))
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
pocketmon={i+1:input().strip() for i in range(n)}
question=[input().strip() for i in range(m)]
rpkm = reverse_dict(pocketmon)
for q in question:
    if q.isnumeric():
        print(pocketmon[int(q)])
    else:
        print(rpkm[q])
# jikwon = set()
# for _ in range(n):
#     name, status = input().split()
#     if status == "enter":
#         jikwon.add(name)
#     else:
#         jikwon.remove(name)
# sorted_jikwon = sorted(jikwon, reverse=True)
# for j in sorted_jikwon:
#     print(j)