import json
import os

new = []
title = "team title"
nickname = "nickname"
place = "place"
contact = "contacts"

def get_contact(nick):
	with open("result.json") as json1:
		users = json.load(json1)
		
		finder_dict = {user.get(nickname):user.get(contact) for user in users}
		
		return finder_dict[nick]

def create_dir():
    dir = os.path.join(os.getcwd(), 'data')
    if not os.path.exists(dir):
        os.mkdir(dir)

def record(lst):
	create_dir()
	with open("data/result_union.json","w") as wjson:
		json.dump(lst, wjson, indent=4, ensure_ascii=False)


def main():
	
	new_json = []
	with open("result_V.json") as json2: 
		result_2 = json.load(json2)

		for item in result_2:
			name = item.get(nickname)
			new_json.append(
				{
				place:item.get(place),
				title: item.get(title),
				nickname:name,
				contact:get_contact(name)
				})
			
		record(new_json)
		print("Reformation has successfully completed!")


if __name__ == "__main__":
	main()