import matplotlib.pyplot as plt
import json

with open('input2.json', encoding="UTF-8") as f:
    json_object = json.load(f)


def get_genre(age):
    new_obj_table = {}
    obj = json_object[str(age)]

    for key in obj.keys():
        for genre in obj[key].keys():
            if genre in new_obj_table:
                new_obj_table[genre] += obj[key][genre]
            else:
                new_obj_table[genre] = obj[key][genre]

    obj_keys = []
    obj_values = []
    all_value = sum(new_obj_table.values())
    etc_genre_value = 0

    for key, value in new_obj_table.items():
        t = (value/all_value)*100
        if t > 3:
            obj_keys.append(key)
            obj_values.append(value)
        else:
            etc_genre_value += value
    obj_keys.append("기타")
    obj_values.append(etc_genre_value)
    return [obj_keys, obj_values]


f, axes = plt.subplots(3, 2)
f.set_size_inches((12, 18))
plt.rc('font', family='AppleGothic')
f.suptitle('시대별 장르 점유도', fontsize=15)

for i in range(3):
    for j in range(2):
        _age = 1970 + (j + i * 2) * 10
        keys, values = get_genre(_age)

        axes[i, j].set_title(_age, fontsize=12)
        axes[i, j].pie(values, labels=keys, autopct='%.1f%%')
plt.show()
