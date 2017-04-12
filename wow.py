from urllib.request import urlopen
import json
import sys

WoW_api = 'z6abfbjjhqccvejttjtxu9hw5m7w6fbc'

def guild_search(x, y):
	api_key = WoW_api
	url = 'https://us.api.battle.net/wow/guild/'
	x = x.replace(' ', '%20')
	y = y.replace(' ', '%20')
	final_url = url + y + "/" + x + "?fields=members&locale=en_US&apikey=" + WoW_api
	json_obj = urlopen(final_url)
	data = json.load(json_obj)
	
	print(" -----------------------------------------------------------------------")
	print("|Guild members will be displayed by their alias followed by their realm.|")
	print("|If no specifications are inserted, all members will be listed in no    |")
	print("|particular order. Please be aware that (depending on the size of the   |")
	print("|guild) the entire length of the list may be undiserable.               |")
	print(" -----------------------------------------------------------------------")
	
	alphabetical = input("Would you like to parse the list alphabetically? [y/n]")
	
	if alphabetical == 'y':
		letter = input("Please enter a letter to jump to: ")
		for item in data['members']:
			player_result = item['character']['name']
			if player_result.startswith(letter.upper()):
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
		

print('\nWelcome to Guild Management Tool 1.0\n')
guild = input('Enter name of guild: ')
realmg = input('Enter name of realm: ')

guild_search(guild, realmg)

print("")		
name, realmp = input('Please choose a guild member to lookup (followed by player realm): ').split()

print('-----------------------------------------------------------------------')
player_query(name, realmp)
print('-----------------------------------------------------------------------')