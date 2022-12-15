import matplotlib.pyplot as plt
import json

start_year = 1970
end_year = 2021

genreSet = set()
genreTable = {}
percentTable = {}


def format_age(y):
    return y // 10 * 10


with open('input2.json', encoding="UTF-8") as f:
    json_object = json.load(f)

# 각 년도별 장르 점유율 딕셔너리 생성
for year in range(start_year, end_year + 1):
    new_obj_table = {}
    age = format_age(year)
    percentTable[str(year)] = {}
    obj = json_object[str(age)]

    for genre in obj[str(year)].keys():
        if genre in new_obj_table:
            new_obj_table[genre] += obj[str(year)][genre]
        else:
            new_obj_table[genre] = obj[str(year)][genre]

    all_value = sum(new_obj_table.values())

    for key, value in new_obj_table.items():
        percent = (value / all_value) * 100
        if percent >= 25:
            # key_lst = list(percentTable[str(year)].keys())
            genreSet.update([key])
        percentTable[str(year)][key] = percent

# genreTable 0으로 초기화
for genre in list(genreSet):
    genreTable[genre] = [0] * 52

# genreTable에 곡 갯수 저장
for year in range(start_year, end_year + 1):
    obj = percentTable[str(year)]

    for key in list(obj.keys()):
        if key in genreTable:
            value = obj[key]
            print(value, year, key)
            genreTable[key][year - 1970] += value
    print("----------------------------------------------")

colorTable = ["red", "limegreen", 'violet', 'dodgerblue', 'orange']

# line 그래프 생성
for idx, genre in enumerate(list(genreSet)):
    if genre in genreTable.keys():
        plt.plot(genreTable[genre], label=genre, color=colorTable[idx % len(colorTable)])

x = range(0, 53, 10)
values = range(1970, 2022, 10)

plt.xlabel('year')
plt.ylabel('percent')
plt.xticks(x, values)

plt.grid(True, axis='x', color='gray', alpha=0.5, linestyle="--")
plt.grid(True, axis='y', color='gray', alpha=0.5, linestyle="--")

plt.rc('font', family='AppleGothic')
plt.rc('font', family='AppleGothic')
plt.title('top5 genre')

plt.legend()
plt.show()
