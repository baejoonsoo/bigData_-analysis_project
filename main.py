from bs4 import BeautifulSoup as bs
import requests

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    "Host":"www.melon.com",
    "Cookie":"__T_=1; __T_=1; PCID=16679931330188269286283; _T_ANO=CzdYVlIrxdJfnUj/PiNc2AATLskrJ3zAv9TdO2+sMkPxEMbhJszYgkOm8aFl+75ooFgDJpTr3tPIBz3NaIXnnfLFT+DQ+ojy2aG4dCPfstQFSEwPXaER19lhxN6cEIqm9N6sQpzrzK8n+eN5MbWqg9VcRRn+5q00TfPzBuz4DoLfpDM1mhLNDSqtcTxs2KgyxTA56eLuT2TT22pzm0D6iXOFrjYXhPFe4mb0rM1/N5ula+iQqIIRyTMT+9uWVpFIPf7EPqJvea44rEwjgRGC/AP7WkDf7TkdDcTrr3pXcut3zXyK2hr+PykYZINumFzP3J1KmIVHIQ5lh603OcZvgg==; wcs_bt=s_f9c4bde066b:1668751998; __T_=1; melonlogging=1000002502; mainPop=2022%3A11%3A18%2023%3A59%3A59; POC=MP10; commerceBanner2=2022%3A11%3A18%2023%3A59%3A59; PC_PCID=16679931330188269286283"
}
url = "https://www.melon.com/chart/search/list.htm?chartType=YE&age=2020&year=2021&classCd=KPOP&moved=Y"

doc_page = requests.get(url, headers=header)
soup = bs(doc_page.text, "lxml").find("body").find("table").find_all("tr")[1:11]


id_list = []

for tr in soup:
    songId = tr.find("input")["value"]
    id_list.append(songId)

print(id_list)