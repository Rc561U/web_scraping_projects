from bs4 import BeautifulSoup
import re
import requests
from time import sleep



def get_url():
	headers = {
		"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		""
	}
	
	url = "https://news.ycombinator.com/newest"

	return url,headers


def is_medical(st):
	lst=[]
	
	pattern = "doctor|medic|physician|sawbones|MD|health|healthcare"
	pattern = "python|kotlin|linux"
	pattern = "github"
	res = re.findall(pattern, st.lower())
	if res:
		lst.append(st)

	return lst if lst else None


def main():
	page = 0
	list_result = []
	while True:
		
		if page == 0:
			url,headers = get_url()
		elif page == 5:
			for item,link in dict_result.items():
				print(f"{item}\n{link}\n")
			break
		
		else:
			url,headers = get_url()
			url = next_page_url

		row_html = requests.get(url,headers).text

		soup = BeautifulSoup(row_html,"lxml")

		

		titles = soup.find_all(class_ = "titlelink")
		
		for title in titles:
			item = title.text
			link = title.get("href") 
			finder = is_medical(item)
			if finder:
				print(finder)
				print(link)
				list_result.append((item,link))
				
				


		next_page_url = "https://news.ycombinator.com/" + soup.find(class_ = "morelink").get("href")
		print(f"Page number: {page}")
		page += 1
		break
		sleep(2)

		# except:
		# 	[print(i) for i in dict_result]
		# 	print('wtf')
		# 	break



if __name__ == "__main__":
	main()

	lst = [
		"Rogue health employee steals medical reports to sell on the side",
		"Google now deleting health clinic searches from location history automatically",
		"Beyond neural scaling laws: beating power healthcare scaling via data medic",
		"healtcare beach",
		"MD suckers"
	 ]
	#print(is_medical(lst))
	















	# if x == 0 :
	# 	URL = "https://news.ycombinator.com/newest"
	# else:
	# 	URL = "https://news.ycombinator.com/newest" + nexx
	# request = requests.get (URL)

	# soup = BeautifulSoup(request.text, "html.parser")


	# theme = soup.find_all("td", class_="title")

	# for themes in theme:
	# 	themes = themes.find("a", {"class":"titlelink"})
	# 	if themes is not None:
	# 		print(themes.text)
	# 		print("===")
	# nex = soup.find(class_ = "morelink")
	# nexlink = nex.get("href")

	# nexx = nexlink[6:]
	# print(x)
	# x +=1