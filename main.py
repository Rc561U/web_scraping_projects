from bs4 import BeautifulSoup
import json
import requests

#1-37

headers = {
	"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
	"Accept":"*/*"
}


def get_data_file(headers):

	result_list = []
	offset = 1
	img_count = 0
	total = 0
	user_count = 365

	while True:
		url = f"https://worldoftanks.ru/tmsis/api/v1/tournament/teams/?filter[tournament_id]=24055&page[size]=10&page[number]={offset}&filter[status]=confirmed"
		response = requests.get(url=url, headers=headers)
		data = response.json()

		
		for item in data:
			if data.get("status") == "ok":
				users = data["data"]["results"]

				for user in users:
					result_list.append(
						{
						"team title" : user.get("title"),
						"nickname": user["players"][0].get("nickname"),
						"contacts": user["extra_data"].get("contacts")
						}
					)
					user_count = user_count - 1
			else:
				with open("result.json", "w") as jsonfile:
					json.dump(result_list, jsonfile, indent=4, ensure_ascii=False)
				return f"[INFO] Work finished"

		print(f"[+] Processed {offset}. {user_count} left to download")
		offset+=1
		

def main():
	get_data_file(headers=headers)




if __name__ == "__main__":
	main()