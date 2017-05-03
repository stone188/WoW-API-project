from urllib.request import urlopen
from pprint import pprint
import json
import sys
import os

WoW_api = 'z6abfbjjhqccvejttjtxu9hw5m7w6fbc'
Logs_api = '46ed538fbf48dfc33349db5d26eb5441'

def importLists(g1, g2, g3, g4):
	for line in open("raid.txt", "r"):
		g1_in, g2_in, g3_in, g4_in = line.strip().split(',')
		g1.append(g1_in)
		g2.append(g2_in)
		g3.append(g3_in)
		g4.append(g4_in)
		
def exportLists(g1, g2, g3, g4):
	with open("raid.txt", "w") as f:
		f.writelines(map("{},{},{}\n".format, g1, g2, g3, g4))
		
def mainMenu():
	os.system('cls')
	print(" ----------------------------------------------------- ")
	print("|1. Check current guild ranking on raid encounters    |")
	print("|2. View list of members                              |")
	print("|3. Pull member for query / assign to raid group)     |")
	print("|4. View raid groups                                  |")
	print("|5. View calendar events                              |")
	print(" ----------------------------------------------------- ")
	menu_option = input("\nWhat would you like to do: ")
	return menu_option
	
def playerMenu():
	os.system('cls')
	print(" ----------------------------- ")
	print("|1. Check gear / add to group |")
	print("|2. Recent raid stats         |")
	print("|3. Recent pvp stats          |")
	print(" ----------------------------- ")
	menu_option = input("\nWhat would you like to do: ")
	
	return menu_option
	
def rankMenu():
	os.system('cls')
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
	
def difficultyMenu():
	os.system('cls')
	print(" -------------- ")
	print("|1. Normal     |")
	print("|2. Heroic     |")
	print("|3. Mythic     |")
	print(" -------------- ")
	menu_option = input("\nWhich difficulty: ")
	
	return menu_option
	
def roleMenu():
	os.system('cls')
	print(" -------------- ")
	print("|1. Tank       |")
	print("|2. Heals      |")
	print("|3. DPS        |")
	print(" -------------- ")
	menu_option = input("\nWhich role type would you like to query: ")
	
	return menu_option
	
def raidGroupMenu():
	os.system('cls')
	print(" -----------------|")
	print("|1. RG1           |")
	print("|2. RG2           |")
	print("|3. RG3           |")
	print("|4. RG4 (PVP)     |")
	print(" -----------------|")
	menu_option = input("\nWhich group would you like to view: ")
	
	return menu_option
	
def continueLoop():
	proceed = input("\nWould you like to continue[y] or quit[n]?")
	
	if proceed.lower() == 'y':
		return True
	
	elif proceed.lower() == 'n':
		return False
		
	else:
		print("ERROR: invalid selection.\nQuitting...")
		return False
	
def guildSearch(x, y):
	api_key = WoW_api
	url = 'https://us.api.battle.net/wow/guild/'
	x = x.replace(' ', '%20')
	y = y.replace(' ', '%20')
	final_url = url + y + "/" + x + "?fields=members&locale=en_US&apikey=" + WoW_api
	json_obj = urlopen(final_url)
	data = json.load(json_obj)
	
	return data
	
def wowlogsSearch(x, y, difficulty, role, encounter, parses, reports):
	api_key = Logs_api
	region = "US"
	limit = "5000"
	rank_q = "rankings/encounter/"
	parse_q = "parses/character/"
	reports_q = "reports/guild/"
	url = "https://www.warcraftlogs.com:443/v1/"
	x = x.replace(' ', '%20')
	y = y.replace(' ', '%20')
	if(parses == 1 and role != "none" and reports == 0) :
		final_url = url + parse_q + x + "/" + y + "/" + region + "?encounter=" + encounter + "&metric=" + role + "&api_key=" + api_key
		
	elif(role != "none" and parses != 1 and reports == 0):
		final_url = url + rank_q + encounter + "?metric=" + role + "&difficulty=" + difficulty + "&limit=" + limit + "&guild=" + x + "&server=" + y + "&region=" + region + "&api_key=" + api_key
	
	elif(role == "none" and parses != 1 and reports == 0):
		final_url = url + rank_q + encounter + "?difficulty=" + difficulty + "&limit=" + limit + "&guild=" + x + "&server=" + y + "&region=" + region + "&api_key=" + api_key
	
	elif(role == "none" and encounter == "none" and difficulty ==  "none" and parses == 0 and reports == 1):
		final_url = url + reports_q + x + "/" + y + "/" + region + "?api_key=" + api_key
	
	else:
		print("OPERATION FAILURE: URL not found")
		
	json_obj = urlopen(final_url)
	data = json.load(json_obj)
	
	return data

def playerSearch(x, y):
	data = guildSearch(x, y)
	
	print(" -----------------------------------------------------------------------")
	print("|Guild members will be displayed by their alias followed by their realm.|")
	print("|If no specifications are inserted, all members will be listed in no    |")
	print("|particular order. Please be aware that (depending on the size of the   |")
	print("|guild) the entire length of the list may be undiserable.               |")
	print(" -----------------------------------------------------------------------")
	
	menu_option = input(" -------------------------------------------------- "
						 "\n|1. Specify player search by alphabetical catagory |" 
						 "\n|2. Specify player search by lvl                   |"
						 "\n|3. Specify player search by class                 |"
						 "\n|4. Specify player by ilvl                         |"
						 "\n|5. No specifications                              |"
						 "\n --------------------------------------------------\n")
	
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
				
	elif menu_option == '4':
		data = wowlogsSearch(x, y, "4", "none", "1849", 0, 0)
		
		lower_bound, upper_bound = input('Please type a lower followed by an upper bound (ex. 896 905): ').split()
		for item in data['rankings']:
			if int(upper_bound) >= item['itemLevel'] >= int(lower_bound):
				print(item['name'] + " ilvl: " + str(item['itemLevel']))
				
	else:
		for item in data['members']:
			print(item['character']['name'] + " " + item['character']['realm'])
			
def playerQuery(p, r, f):
	api_key = WoW_api
	url = 'https://us.api.battle.net/wow/character/'
	player = p
	realm = r
	field = f
	
	if field == "none":
		final_url = url + realm + "/" + player + "?locale=en_US&apikey=" + WoW_api
		
	else:
		final_url = url +realm + "/" + player + "?fields=" + field + "&locale=en_US&apikey=" + WoW_api
	
	json_obj = urlopen(final_url)
	data = json.load(json_obj)	
	return data
		
	
def getEncoutner():
	encounter = ""
	
	rank_menu_selection = rankMenu()
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
	
	return encounter
	
def getDifficulty():
	difficulty = ""
	
	difficulty_menu_selection = difficultyMenu()
	if difficulty_menu_selection == "1":
		difficulty = "3"
	
	elif difficulty_menu_selection == "2":
		difficulty = "4"
	
	else:
		difficulty = "5"
	
	return difficulty
	
def getRole():
	role = ""
	
	role_menu_selection = roleMenu()
	if role_menu_selection == "1":
		role = "krsi"
	
	elif role_menu_selection == "2":
		role = "hps"
		
	else:
		role = "dps"
	
	return role
	
def guildRank(x, y):
	i = 0
	encounter = getEncoutner()
	difficulty = getDifficulty()
	role = getRole()
	
	data = wowlogsSearch(x, y, difficulty, role, encounter, 0, 0)
	
	for item in data['rankings']:
		i += 1
		print(str(i) + ". " +  item['name'] + " :: Rank:" + str(item['rank']))
		
def addToRaidGroup():
	add_prompt = input("***Would you like to add this member to a raid group? [0 (none), 1, 2, 3, 4]***")
	return add_prompt
	
def printPlayer(p, r):
	os.system('cls')
	player_class = ""
	player_gender = ""
	player_level = ""
	player_race = ""
	
	data = playerQuery(p, r, "none")
	player = p
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
					
def printGear(p,r):
	print("\n")
	data = playerQuery(p, r, "items")
			
	ilvl = data['items']['averageItemLevelEquipped']
	head = data['items']['head']['name']
	head_ilvl = data['items']['head']['itemLevel']
			
	neck = data['items']['neck']['name']
	neck_ilvl = data['items']['neck']['itemLevel']
			
	shoulder = data['items']['shoulder']['name']
	shoulder_ilvl = data['items']['shoulder']['itemLevel']
			
	back = data['items']['back']['name']
	back_ilvl = data['items']['back']['itemLevel']
			
	chest = data['items']['chest']['name']
	chest_ilvl = data['items']['chest']['itemLevel']
			
	wrist = data['items']['wrist']['name']
	wrist_ilvl = data['items']['wrist']['itemLevel']
			
	hands = data['items']['hands']['name']
	hands_ilvl = data['items']['hands']['itemLevel']
			
	waist = data['items']['waist']['name']
	waist_ilvl = data['items']['waist']['itemLevel']
			
	legs = data['items']['legs']['name']
	legs_ilvl = data['items']['legs']['itemLevel']
			
	feet = data['items']['feet']['name']
	feet_ilvl = data['items']['feet']['itemLevel']
			
	finger1 = data['items']['finger1']['name']
	finger1_ilvl = data['items']['finger1']['itemLevel']
			
	finger2 = data['items']['finger2']['name']
	finger2_ilvl = data['items']['finger2']['itemLevel']
			
	trinket1 = data['items']['trinket1']['name']
	trinket1_ilvl = data['items']['trinket1']['itemLevel']
			
	trinket2 = data['items']['trinket2']['name']
	trinket2_ilvl = data['items']['trinket2']['itemLevel']
			
	weapon = data['items']['mainHand']['name']
	weapon_ilvl = data['items']['mainHand']['itemLevel']
	
	print("Head: " + head + " | " + str(head_ilvl))
	print("Neck: " + neck + " | " + str(neck_ilvl))
	print("Shoulders: " + shoulder + " | " + str(shoulder_ilvl))
	print("Back: " + back + " | " + str(back_ilvl))
	print("Chest: " + chest + " | " + str(chest_ilvl))
	print("Wrists: " + wrist + " | " + str(wrist_ilvl))
	print("Hands: " + hands + " | " + str(hands_ilvl))
	print("Waist: " + waist + " | " + str(waist_ilvl))
	print("Legs: " + legs + " | " + str(legs_ilvl))
	print("Feet: " + feet + " | " + str(feet_ilvl))
	print("Finger 1: " + finger1 + " | " + str(finger1_ilvl))
	print("Finger 2: " + finger2 + " | " + str(finger2_ilvl))
	print("Trinket 1: " + trinket1 + " | " + str(trinket1_ilvl))
	print("Trinket 2: " + trinket2 + " | " + str(trinket2_ilvl))
	print("Weapon: " + weapon + " | " + str(weapon_ilvl) +  "\nGear equipped average: " + str(ilvl))
	
def printRaidStat(x, y):
	print("\n")
	encounter = getEncoutner()
	difficulty = getDifficulty()
	role = getRole()
	
	data = wowlogsSearch(x, y, difficulty, role, encounter, 1, 0)
	boss = data[0]['name']
	for item in data [0]['specs']:
		spec = item['spec']
		
	for item in data[0]['specs']:
		for value in item['data']:
			measure = value['persecondamount']
			parse = value['percent']
			rank = value['rank']
	
	print("\nBoss: " + boss + "\n")
	print("Spec: " +  spec)
	print("DPS/HPS: " + str(measure))
	print("Parse percentile: " + str(parse))
	print("Approx. rank: " +  str(rank))
	
def printPVPStats(x, y):
	data = playerQuery(x, y, "pvp")
	
	twos = data['pvp']['brackets']['ARENA_BRACKET_2v2']['rating']
	threes = data['pvp']['brackets']['ARENA_BRACKET_3v3']['rating']
	RBG = data['pvp']['brackets']['ARENA_BRACKET_RBG']['rating']
	h_kills = data['totalHonorableKills']
	
	print("\nArena 2v2 Rating: " + str(twos))
	print("Arena 3v3 Rating: " + str(threes))
	print("RBG Rating: " + str(RBG))
	print("Lifetime HKs: " + str(h_kills) + "\n")
	
def printCalander(x, y):
	data = wowlogsSearch(x, y, "none", "none", "none", 0, 1)
	
	for item in data:
		print("Event: " + item['title'] + "\nOwner: " + item['owner'])
	
	
	
	
			
print('\nWelcome to Guild Management Tool 1.0\n')
proceed = True
RG1 = []
RG2 = []
RG3 = []
RG4 = []
importLists(RG1, RG2, RG3, RG4)
guild = input('Enter name of guild (exactly as it appears in game): ')
realmg = input('Enter name of realm (exactly as it appears in game): ')

while proceed:
	os.system('cls')
	main_menu_select = mainMenu()
	if main_menu_select == "1":
		guildRank(guild, realmg)
		proceed = continueLoop()

	elif main_menu_select == "2":
		playerSearch(guild, realmg)
		proceed = continueLoop()
	
	elif main_menu_select == "3":
		name, realmp = input('Please choose a guild member to lookup followed by their realm (ex. esosj Malorne): ').split()

		print('-----------------------------------------------------------------------')
		printPlayer(name, realmp)
		print("\n")
	
		player_menu_select = playerMenu()
		if player_menu_select == '1':
			printGear(name, realmp)
			
			add = addToRaidGroup()
			if add != '0':
				role = input("What role does this member have?")
				
			if add == '1':
				RG1.append([name, role])
				
			elif add == '2':
				RG2.append([name, role])
				
			elif add == '3':
				RG3.append([name, role])
				
			else:
				print("ERROR: Incorrect value, operation aborted")

			proceed = continueLoop()
			
		elif player_menu_select == '2':
			printRaidStat(name, realmp)
			proceed = continueLoop()
			
		elif player_menu_select == '3':
			printPVPStats(name, realmp)
			
			add2 = input("Would you like to add this member to PVP Raid Group 4? [y/n]")
			role2 = input("What role does this member have?")
			if add2 == 'y':
				RG4.append([name, role2])
				exportLists(RG1, RG2, RG3, RG4)
				
			proceed = continueLoop()
			
		else:
			print("ERROR: Incorrect value, operation aborted")
			proceed = continueLoop()
			
	elif main_menu_select == '4':
		raid_group_select = raidGroupMenu()
		
		if raid_group_select == '1':
			pprint(RG1)
			
		elif raid_group_select == '2':
			pprint(RG2)
			
		elif raid_group_select == '3':
			pprint(RG3)
			
		elif raid_group_select == '4':
			pprint(RG4)
			
		else:
			print("ERROR: Incorrect value, operation aborted")
			
		exportLists(RG1, RG2, RG3, RG4)
		proceed = continueLoop()
		
	elif main_menu_select == '5':
		printCalander(guild, realmg)
		proceed = continueLoop()
		
	else:
		print("ERROR: Incorrect value, operatoin aborted")
		proceed = continueLoop()