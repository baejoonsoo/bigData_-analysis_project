from bs4 import BeautifulSoup as bs
import requests
import json


header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    "Host": "www.melon.com",
    "Cookie": "__T_=1; __T_=1; PCID=16679931330188269286283; _T_ANO=CzdYVlIrxdJfnUj/PiNc2AATLskrJ3zAv9TdO2+sMkPxEMbhJszYgkOm8aFl+75ooFgDJpTr3tPIBz3NaIXnnfLFT+DQ+ojy2aG4dCPfstQFSEwPXaER19lhxN6cEIqm9N6sQpzrzK8n+eN5MbWqg9VcRRn+5q00TfPzBuz4DoLfpDM1mhLNDSqtcTxs2KgyxTA56eLuT2TT22pzm0D6iXOFrjYXhPFe4mb0rM1/N5ula+iQqIIRyTMT+9uWVpFIPf7EPqJvea44rEwjgRGC/AP7WkDf7TkdDcTrr3pXcut3zXyK2hr+PykYZINumFzP3J1KmIVHIQ5lh603OcZvgg==; wcs_bt=s_f9c4bde066b:1668751998; __T_=1; melonlogging=1000002502; mainPop=2022%3A11%3A18%2023%3A59%3A59; POC=MP10; commerceBanner2=2022%3A11%3A18%2023%3A59%3A59; PC_PCID=16679931330188269286283"
}

song_detail_url = 'https://www.melon.com/song/detail.htm?songId='
top_num = 100
count = 1

singer_score_table = {}

def format_age(year):
    return year // 10 * 10


def make_url(year):
    age = format_age(year)
    return fr'https://www.melon.com/chart/search/list.htm?chartType=YE&age={age}&year={year}&classCd=KPOP&moved=Y'

def save_singer_score(singer):
    global count
    new_score = 101 - count

    if singer in singer_score_table:
        singer_score_table[singer] += new_score
    else:
        singer_score_table[singer] = new_score


def get_song_singer(id):
    global count
    song_detail_page = requests.get(song_detail_url + str(id), headers=header)
    entry = bs(song_detail_page.text, "lxml").find('body').select_one("div.entry")
    artist = entry.select_one("div.info > div.artist > a > span").text

    save_singer_score(artist)

    print(artist)

    print(f'{count}/{top_num}')
    print('------------------------------------')
    count += 1


def get_one_year_top_id(year):
    doc_page = requests.get(make_url(year), headers=header)
    soup = bs(doc_page.text, "lxml").find("body").find("table").find_all("tr")[1:top_num + 1]

    for tr in soup:
        song_id = tr.find("input")["value"]
        print(year, song_id)
        get_song_singer(song_id)

def save_json(year):
    age = format_age(year)

    with open('singer.json', encoding="UTF-8") as f:
        json_object = json.load(f)

    json_object[str(age)][year] = singer_score_table

    with open('singer.json', 'w', encoding="UTF-8") as f:
        json.dump(json_object, f, indent=2, ensure_ascii=False)


targetYear = 1988

get_one_year_top_id(targetYear)
save_json(targetYear)

print(singer_score_table)