import matplotlib.pyplot as plt
import json

start_year = 1970
end_year = 2021

genreSet = set()
genreTable = {}


def format_age(year):
    return year // 10 * 10


with open('input2.json', encoding="UTF-8") as f:
    json_object = json.load(f)

for year in range(start_year, end_year + 1):
    age = format_age(year)
    key_lst = list(json_object[str(age)][str(year)].keys())

    genreSet.update(key_lst)

for genre in list(genreSet):
    genreTable[genre] = [0] * 52

for year in range(start_year, end_year + 1):
    age = format_age(year)

    obj = json_object[str(age)][str(year)]

    for key in list(obj.keys()):
        value = obj[key]
        genreTable[key][year - 1970] += value


genreTable2 = {}
for genre in genreTable.keys():
    lst = genreTable[genre]
    isInsert = False

    for n in lst:
        if n > 20:
            isInsert = True
            break
    if isInsert:
        genreTable2[genre] = genreTable[genre]

print(len(genreTable.keys()))
print(len(genreTable2.keys()))


x = range(0, 53, 10)
values = range(1970, 2022, 10)

for genre in list(genreSet):
    if genre in genreTable2.keys():
        plt.plot(genreTable2[genre])

plt.xlabel('year')
plt.ylabel('count')
plt.xticks(x, values)

plt.grid(True, axis='x', color='gray', alpha=0.5, linestyle="--")
plt.grid(True, axis='y', color='gray', alpha=0.5, linestyle="--")

plt.show()
