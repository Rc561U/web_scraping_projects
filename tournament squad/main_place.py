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
	user_count = 1
	user_left = 365

	while True:
		url = f"https://worldoftanks.ru/tmsis/api/v1/tournament/teams/?filter[tournament_id]=24055&page[size]=10&page[number]={offset}&filter[status]=confirmed"
		url = f"https://worldoftanks.ru/tmsis/api/v1/tournament/24055/standings/?page[size]=8&page[number]={offset}"
		response = requests.get(url=url, headers=headers)
		data = response.json()

		
		for item in data:
			if data.get("status") == "ok":
				users = data["data"]["results"]

				for user in users:
					result_list.append(
						{
						"place" : user_count,
						"team title" : user["team_data"].get("title"),
						"nickname": user["team_data"]["owner"].get("nickname")
						}
					)
					user_count = user_count + 1
					user_left -= user_count
			else:
				with open("result_victory.json", "w") as jsonfile:
					json.dump(result_list, jsonfile, indent=4, ensure_ascii=False)
				return f"[INFO] Work finished"

		print(f"[+] Processed {offset}. {user_left} left to download")
		offset+=1
		

def main():
	get_data_file(headers=headers)




if __name__ == "__main__":
	main()