from bs4 import BeautifulSoup
import csv, json
import re
import requests
from time import sleep
import os


def get_url():
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"
    }

    url = "https://news.ycombinator.com/newest"

    return url, headers


def is_medical(st):
    lst = []

    pattern = "doctor|medic|physician|sawbones|MD|health|healthcare"
    #pattern = "co|to|est"

    res = re.findall(pattern, st.lower())
    if res:
        lst.append(st)

    return lst if lst else None


def clear():
    try:
        return os.system("clear")
    except:
        return os.system("cls")


def recorder(dictlist):
    create_dir()
    with open('data/links.csv', 'w', newline='') as csvfile:
        fieldnames = ['title', 'link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in dictlist:
            writer.writerow(i)

    with open("data/links.json", "w", newline="") as jsonfile:
        for i in dictlist:
            json.dump(i, jsonfile, indent=4, ensure_ascii=False)


def converter(lst):
    list_dict = []
    for title, link in lst:
        dict_1 = {}
        dict_2 = {}
        dict_1["title"] = title
        dict_2["link"] = link
        list_dict.append(dict_1 | dict_2)
    return list_dict


def create_dir():
    dir = os.path.join(os.getcwd(), 'data')
    if not os.path.exists(dir):
        os.mkdir(dir)


def main(num):
    page = 0
    list_result = []
    while True:
        try:
            if page == 0:
                url, headers = get_url()
            elif page == num:
                clear()
                break

            else:
                url, headers = get_url()
                url = next_page_url

            row_html = requests.get(url, headers).text

            soup = BeautifulSoup(row_html, "html.parser")

            titles = soup.find_all(class_="titlelink")

            for title in titles:
                item = title.text
                link = title.get("href")
                finder = is_medical(item)
                if finder:
                    list_result.append((item, link))

            next_page_url = "https://news.ycombinator.com/" + soup.find(class_="morelink").get("href")
            print(f"Page number: {page+1}")
            page += 1
            





        except AttributeError:
            print("ycombinator.com close the access")
            break





    if list_result:
        list_dict = converter(list_result)
        recorder(list_dict)
        for item, link in list_result:
            print(f"\n{item}\n{link}\n")


    else:
        print("\nThe list is empty")


if __name__ == "__main__":
    # inp = int(input("Enter page count: "))
    inp = 100
    main(inp)

