import json

with open('singer.json', encoding="UTF-8") as f:
    json_object = json.load(f)

singer_score_table = {}


def format_data(age):
    obj = json_object[str(age)]

    temp_obj = {}
    for year in obj.keys():
        for singer, value in obj[str(year)].items():
            if singer in temp_obj:
                temp_obj[singer] += value
            else:
                temp_obj[singer] = value
    singer_score_table[str(age)] = temp_obj


for targetYear in range(1980, 2030, 10):
    print(targetYear)
    format_data(targetYear)
print(singer_score_table)

with open('singer2.json', 'w', encoding="UTF-8") as f:
    json.dump(singer_score_table, f, indent=2, ensure_ascii=False)