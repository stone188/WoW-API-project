from urllib.request import urlopen
import json
import sys
import os

WoW_api = 'z6abfbjjhqccvejttjtxu9hw5m7w6fbc'
Logs_api = '46ed538fbf48dfc33349db5d26eb5441'

def main_menu():
	print(" ----------------------------------------------------- ")
	print("|1. Check current guild ranking on raid encounters    |")
	print("|2. View list of members                              |")
	print("|3. Pull member for query / assign to raid group)     |")
	print("|4. Compare member rankings                           |")
	print("|5. View raid groups                                  |")
	print("|6. View calendar events                              |")
	print(" ----------------------------------------------------- ")
	menu_option = input("\nWhat would you like to do: ")
	return menu_option
	
def player_menu():
	print(" ----------------------------- ")
	print("|1. Player's rank and spec    |")
	print("|2. Check gear                |")
	print("|3. Check raid readiness      |")
	print("|4. Recent raid stats         |")
	print("|5. Recent pvp stats          |")
	print(" ----------------------------- ")
	menu_option = input("\nWhat would you like to do: ")
	
	return menu_option
	
def rank_menu():
	print("\nThis option only supports legion raid The Nighthold\n")
	print(" ------------------- ")
	print("|1. Skorpyron       |")
	print("|2. Krosus          |")
	print("|3. C. Anomaly      |")
	print("|4. Trilliax        |")
	print("|5. Star Augur E.   |")
	print("|6. Spellblade A.   |")
	print("|7. HB Tel'arn      |")
	print("|8. Tichondrius     |")
	print("|9. GM Elisande     |")
	print("|10. Gul'dan        |")
	print(" ------------------- ")
	menu_option = input("\nWhich encounter would you like to view: ")
	
	return menu_option
	
def difficulty_menu():
	print(" ")
	print(" -------------- ")
	print("|1. Normal     |")
	print("|2. Heroic     |")
	print("|3. Mythic     |")
	print(" -------------- ")
	menu_option = input("\nWhich difficulty: ")
	
	return menu_option
	
def role_menu():
	print(" ")
	print(" -------------- ")
	print("|1. Tank       |")
	print("|2. Heals      |")
	print("|3. DPS        |")
	print(" -------------- ")
	menu_option = input("\nWhich role type would you like to query: ")
	
	return menu_option
	
def continue_loop():
	proceed = input("\nWould you like to continue[y] or quit[n]?")
	
	if proceed.lower() == 'y':
		return True
	
	elif proceed.lower() == 'n':
		return False
		
	else:
		print("ERROR: invalid selection.\nQuitting...")
		return False
	
def guild_search(x, y):
	api_key = WoW_api
	url = 'https://us.api.battle.net/wow/guild/'
	x = x.replace(' ', '%20')
	y = y.replace(' ', '%20')
	final_url = url + y + "/" + x + "?fields=members&locale=en_US&apikey=" + WoW_api
	json_obj = urlopen(final_url)
	data = json.load(json_obj)
	
	return data

def player_search(x, y):
	data = guild_search(x, y)
	
	print(" -----------------------------------------------------------------------")
	print("|Guild members will be displayed by their alias followed by their realm.|")
	print("|If no specifications are inserted, all members will be listed in no    |")
	print("|particular order. Please be aware that (depending on the size of the   |")
	print("|guild) the entire length of the list may be undiserable.               |")
	print(" -----------------------------------------------------------------------")
	
	menu_option = input(" ------------------------------------------------- "
						 "\n|1. Specify player search by alphabetical catagory|" 
						 "\n|2. Specify player search by lvl                 |"
						 "\n|3. Specify player search by class                |"
						 "\n|4. No specifications                             |"
						 "\n ------------------------------------------------- \n")
	
	if menu_option == '1':
		letter = input("\nPlease enter a letter to jump to: ")
		for item in data['members']:
			player_result = item['character']['name']
			if player_result.startswith(letter.upper()):
				print(item['character']['name'] + " " + item['character']['realm'])
					
	elif menu_option == '2':
		lvl = input("\nPlease specify an lvl: ")
		for item in data['members']:
			player_lvl = item['character']['level']
			if player_lvl == int(lvl):
				print(item['character']['name'] + " " + item['character']['realm'])
				
	elif menu_option == '3':
		print("\nPlease choose a class type: ")
		class_type = input(" ---------------- "
						   "\n|1. Warrior      |"
						   "\n|2. Paladin      |"
						   "\n|3. Hunter       |"
						   "\n|4. Rogue        |"
						   "\n|5. Priest       |"
						   "\n|6. Death Knight |"
						   "\n|7. Shaman       |"
						   "\n|8. Mage         |"
						   "\n|9. Warlock      |"
						   "\n|10. Monk        |"
						   "\n|11. Druid       |"
						   "\n ---------------- \n")
		
		for item in data['members']:
			player_class = item['character']['class']
			if player_class == int(class_type):
				print(item['character']['name'] + " " + item['character']['realm'])
				
	else:
		for item in data['members']:
			print(item['character']['name'] + " " + item['character']['realm'])
		
def player_query(p, q):
	player_class = ""
	player_gender = ""
	player_level = ""
	player_race = ""
	api_key = WoW_api
	url = 'https://us.api.battle.net/wow/character/'
	player = p
	realm = q
	final_url = url + realm + "/" + player + "?locale=en_US&apikey=" + WoW_api
	json_obj = urlopen(final_url)
	data = json.load(json_obj)
	code1 = data['class']
	code2 = data['gender']
	code3 = data['race']
	player_level = str(data['level'])
	
	if code1 == 1:
		player_class = 'Warrior'
	
	elif code1 == 2:
		player_class = 'Paladin'
		
	elif code1 == 3:
		player_class = 'Hunter'
	
	elif code1 == 4:
		player_class = 'Rogue'
		
	elif code1 == 5:
		player_class = 'Priest'
		
	elif code1 == 6:
		player_class = 'Death Knight'
	
	elif code1 == 7:
		player_class = 'Shaman'
	
	elif code1 == 8:
		player_class = 'Mage'
	
	elif code1 == 9:
		player_class = 'Warlock'
		
	elif code1 == 10:
		player_class = 'Monk'
		
	else:
		player_class = 'Druid'
						
	if code2 == 0:
		player_gender = 'Male'
		
	else:
		player_gender = 'Female'
					
	if code3 == 1:
		player_race = 'Human'
		
	elif code3 == 2:
		player_race = 'Orc'
	
	elif code3 == 3:
		player_race = 'Dwarf'
	
	elif code3 == 4:
		player_race = 'Nightelf'
		
	elif code3 == 5:
		player_race = 'Undead'
		
	elif code3 == 6:
		player_race = 'Tauren'
	
	elif code3 == 7:
		player_race = 'Gnome'
		
	elif code3 == 8:
		player_race = 'Troll'
		
	elif code3 == 10:
		player_race = 'Blood Elf'
			
	else:
		player_race = 'Draenei'
		
	print('Player : ' + player + '\nLevel: ' + player_level + '\nGender: ' + player_gender + '\nRace: ' + player_race + '\nClass: ' + player_class)
		
def guild_rank(x, y):
	api_key = Logs_api
	region = "US"
	limit = "5000"
	url = "https://www.warcraftlogs.com:443/v1/rankings/encounter/"

	x = x.replace(' ', '%20')
	y = y.replace(' ', '%20')
	difficulty = ""
	role = ""
	encounter = ""
	i = 0
	
	rank_menu_selection = rank_menu()
	if rank_menu_selection == "1":
		encounter = "1849"
		
	elif rank_menu_selection == "2":
		encounter = "1842"
		
	elif rank_menu_selection == "3":
		encounter = "1865"
		
	elif rank_menu_selection == "4":
		encounter = "1867"
		
	elif rank_menu_selection == "5":
		encounter = "1863"
		
	elif rank_menu_selection == "6":
		encounter = "1871"
		
	elif rank_menu_selection == "7":
		encounter = "1886"
		
	elif rank_menu_selection == "8":
		encounter = "1862"
		
	elif rank_menu_selection == "9":
		encounter = "1872"
		
	else:
		encounter = "1866"
		
	difficulty_menu_selection = difficulty_menu()
	if difficulty_menu_selection == "1":
		difficulty = "3"
	
	elif difficulty_menu_selection == "2":
		difficulty = "4"
	
	else:
		difficulty = "5"
	
	role_menu_selection = role_menu()
	if role_menu_selection == "1":
		role = "krsi"
	
	elif role_menu_selection == "2":
		role = "hps"
		
	else:
		role = "dps"
		
	final_url = url + encounter + "?metric=" + role + "&difficulty=" + difficulty + "&limit=" + limit + "&guild=" + x + "&server=" + y + "&region=" + region + "&api_key=" + api_key
	json_obj = urlopen(final_url)
	data = json.load(json_obj)
	
	for item in data['rankings']:
		i += 1
		print(str(i) + ". " +  item['name'] + " :: Rank:" + str(item['rank']))
	
print('\nWelcome to Guild Management Tool 1.0\n')
proceed = True
guild = input('Enter name of guild (exactly as it appears in game): ')
realmg = input('Enter name of realm (exactly as it appears in game): ')

while proceed:
	os.system('cls')
	main_menu_select = main_menu()
	if main_menu_select == "1":
		guild_rank(guild, realmg)
		proceed = continue_loop()

	elif main_menu_select == "2":
		player_search(guild, realmg)
		proceed = continue_loop()
	
	elif main_menu_select == "3":
		name, realmp = input('Please choose a guild member to lookup (followed by player realm): ').split()

		print('-----------------------------------------------------------------------')
		player_query(name, realmp)
		print('-----------------------------------------------------------------------')
	
		player_menu_select = player_menu
		#if(player_menu_select == 1):
		