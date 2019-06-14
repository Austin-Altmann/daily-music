#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import random

# Genres
# Genres and their subgenres are from https://rateyourmusic.com/genres

Ambient = ["Ambient Dub","Dark Ambient","Space Ambient","Tribal Ambient"]

Blues = ["Acoustic Blues","Boogie Woogie","Electric Blues","Hill Country Blues","Jump-Blues","New Orleans Blues","Piano Blues","Soul Blues","Vaudeville Blues"]

Classical = ["Arabic Classical Music","Brazilian Classical Music","East Asian Classical Music","Latin Classical Music","Modern Classical","Persian Classical Music","Pibroch","Shashmaqam","South Asian Classical Music","Southeast Asian Classical Music","Turkish Classical Music","Western Classical Music"]

Country = ["Alt-Country","Americana","Contemporary Country","Country & Irish","Country Pop","Honky Tonk","Progressive Country","Traditional Country","Western Swing"]

Dance = ["Alternative Dance","Dance-Pop","Dance-Punk","Disco","Electronic Dance Music"]

Electronic = ["Acid Croft","Ambient Dub","Bit Music","Bitpop","Downtempo","Dungeon Synth","Electroacoustic","Electro-Industrial","Electronic Dance Music","Electropop","Folktronica","Glitch","Glitch Hop","Glitch Pop","Grime","Horror Synth","IDM","Illbient","Indietronica","Latin Electronic","Microsound","Minimal Wave","Nightcore","Nu Jazz","Progressive Electronic","Psybient","Synthpop","Synth Punk","Synthwave","Vaporwave","Witch House"]

Experimental = ["Drone","Electroacoustic","Free Improvisation","Futurism","Glitch","Indeterminacy","Industrial","Noise","Plunderphonics","Reductionism","Sound Collage","Sound Poetry","Tape Music","Turntable Music"]

Folk = ["Contemporary Folk","Traditional Folk Music"]

Hip_hop = ["Abstract Hip Hop","Arabesque Rap","Bongo Flava","Bounce","Chopped and Screwed","Christian Hip Hop","Cloud Rap","Comedy Rap","Conscious Hip Hop","Country Rap","Crunk","Dirty South","Disco Rap","East Coast Hip Hop","Emo Rap","Experimental Hip Hop","French Hip Hop","Genge","G-Funk","Hardcore Hip Hop","Hiplife","Hyphy","Instrumental Hip Hop","Japanese Hip Hop","Jazz Rap","Latin Rap","Miami Bass","Mobb Music","Nerdcore","Political Hip Hop","Pop Rap","Snap","Southern Hip Hop","Trap Rap","Turntablism","UK Hip Hop","West Coast Hip Hop"]

Industrial = ["Industrial","Post-Industrial","Power Noise"]

Jazz = ["Acid Jazz","Afro-Jazz","Arabic Jazz","Avant-Garde Jazz","Bebop","Big Band","British Dance Band","Bulawayo Jazz","Cape Jazz","Cartoon Music","Chamber Jazz","Cool Jazz","Dark Jazz","Dixieland","ECM Style Jazz","Ethio-Jazz","Flamenco Jazz","Gypsy Jazz","Jazz-Funk","Jazz Fusion","Jazz Poetry","Latin Jazz","Marabi","Modal Jazz","New Orleans Brass Band","Samba-Jazz","Smooth Jazz","Soul Jazz","Stride","Swing","Third Stream","Vocal Jazz"]

Metal = ["Alternative Metal","Avant-Garde Metal","Black Metal","Death Metal","Doom Metal","Drone Metal","Folk Metal","Gothic Metal","Grindcore","Groove Metal","Heavy Metal","Industrial Metal","Melodic Metalcore","Metalcore","Neoclassical Metal","Post-Metal","Power Metal","Progressive Metal","Sludge Metal","Speed Metal","Stoner Metal","Symphonic Metal","Thrash Metal","Trance Metal","Viking Metal"]

Musical_theater_and_entertainment = ["Cabaret","Cuplé","Dutch Cabaret","Kabarett","Kanto","Murga","Music Hall","Revue","Show Tunes","Vaudeville"]

New_age = ["Andean New Age","Celtic New Age","Neoclassical New Age"]

Pop = ["Adult Contemporary","Ambient Pop","Arabic Pop","Art Pop","Balkan Pop-Folk","Baroque Pop","Bitpop","Blue-Eyed Soul","Boy Band","Brill Building","Bubblegum","Cambodian Pop","CCM","Classical Crossover","Country Pop","C-Pop","Dance-Pop","Dangdut","Dansbandsmusik","Dansktop","Easy Listening","Electropop","Europop","Flamenco Pop","Folk Pop","French Pop","Girl Group","Glitch Pop","Indian Pop","Indie Pop","Italo Pop","Jazz Pop","J-Pop","K-Pop","Latin Pop","Nederpop","New Romantic","Palingsound","Persian Pop","Pop Ghazal","Pop Raï","Pop Rock","Pop Soul","Pop Sunda","Progressive Pop","Psychedelic Pop","Rabiz","Rigsar","Rumba catalana","Russian Chanson","Schlager","Sertanejo universitário","Shibuya-kei","Sophisti-Pop","Sunshine Pop","Synthpop","Teen Pop","Traditional Pop","Turkish Pop","V-Pop","Yé-yé"]

Psychedelia = ["Neo-Psychedelia","Psychedelic Folk","Psychedelic Pop","Psychedelic Rock","Psychedelic Soul"]

Punk = ["Art Punk","Digital Hardcore","Emo","Post-Hardcore","Post-Punk","Proto-Punk","Punk Rock","Synth Punk"]

R_and_b = ["Boogie","Contemporary R&B","Doo-Wop","Funk","New Orleans R&B","Rhythm & Blues","Soul"]

Regional = ["African Music","Ancient Music","Arabic Music","Balkan Music","Brazilian Music","Caribbean Music","Caucasian Music","Chanson","Christian Liturgical Music","Country","East Asian Music","Greek Music","Hispanic Music","Islamic Modal Music","Jewish Music","Philippine Music","Polynesian Music","Polyphonic Chant","Portuguese Music","Prehistoric Music","Romanian Music","Russian Music","Seychelles & Mascarene Islands Music","South Asian Music","Southeast Asian Music","Tibetan Traditional Music","Traditional Folk Music","Turkic-Mongolic Traditional Music","West Asian Music"]

Rock = ["Acoustic Rock","Afro-Rock","Alternative Rock","Andean Rock","AOR","Art Punk","Art Rock","Blues Rock","British Rhythm & Blues","Christian Rock","Comedy Rock","Country Rock","Dark Cabaret","Deutschrock","Emo","Experimental Rock","Folk Rock","Funk Rock","Garage Rock","Glam Rock","Hard Rock","Heartland Rock","Industrial Rock","Jam Band","Jazz-Rock","Latin Rock","Math Rock","Metal","Mod","New Wave","Noise Rock","Pop Rock","Post-Hardcore","Post-Punk","Post-Rock","Progressive Rock","Proto-Punk","Psychedelic Rock","Pub Rock","Punk Rock","Rap Rock","Rock & Roll","Rock Opera","Rock urbano español","Roots Rock","Southern Rock","Sufi Rock","Surf Music","Symphonic Rock","Zamrock","Zolo"]

Singer_songwriter = ["Bard Music","Canzone d'autore","Chanson à texte","Liedermacher","Música de intervenção","Nueva canción","Poezja śpiewana"]

Ska = ["2 Tone","Jamaican Ska","Spouge","Third Wave Ska"]


genres = {'ambient': Ambient\
, 'blues' : Blues\
, 'classical' : Classical\
, 'country' : Country\
, 'dance' : Dance\
, 'electronic' : Electronic\
, 'experimental' : Experimental\
, 'folk' : Folk\
, 'hip hop' : Hip_hop\
, 'jazz' : Jazz\
, 'metal' : Metal\
, 'musical theater and entertainment' : Musical_theater_and_entertainment\
, 'new age' : New_age\
, 'pop' : Pop\
, 'psychedelia' : Psychedelia\
, 'punk' : Punk\
, 'r&b' : R_and_b\
, 'regional' : Regional\
, 'rock' : Rock\
, 'singer songwriter' : Singer_songwriter\
, 'ska' : Ska}

# File handling

def track_subgenre( subgenre ):
	with open("listened.txt",'a',encoding = 'utf-8') as file:
		if not subgenre_tracked(subgenre):
			file.write(str(subgenre) + "\n")

def clear_subgenres():
	with open("listened.txt", 'w'): pass

def subgenre_tracked( subgenre ):
	try:
		with open("listened.txt",'r') as file:
			data = file.readlines()

		for line in data:
			if str(subgenre) in line:
				return True
		return False
	except:
		# File not found
		return False

# Helpers

def all_tracked( dictionary ):
	try:
		with open("listened.txt",'r') as file:
			data = file.readlines()
		file_length = len(data)

		if file_length == total_subgenres(dictionary):
			return True
		else:
			return False
	except:
		# File not found
		return False
	
def total_subgenres( dictionary ):
	total = 0
	for key in dictionary:
		for item in dictionary[key]:
			total += 1
	return total


# Selection logic

def get_subgenre(dictionary, key=None):
	if key is None:
		key = random.choice(list(dictionary.keys()))
	else:
		if key not in dictionary:
			raise SystemExit('Error: Key not in dictionary')
	item = random.choice(dictionary[key])

	return item


# User input

def main():
	parser = argparse.ArgumentParser(description='Select a a subgenre of music')
	parser.add_argument('-n', help='Do not track the selected subgenre in a txt file. (default: track)', action='store_false')
	parser.add_argument('-r', '--repeat', help='Allow tracked subgenres to be chosen again. (default: do not repeat)', action='store_true')
	parser.add_argument('-c', '--clear', help='Clear the previously tracked subgenres. (default: do not clear)',action='store_true')
	parser.add_argument('-g', help='Choose a specific genre. (default: random)', nargs=1)

	args = parser.parse_args()

	track = args.n
	repeat = args.repeat
	clear = args.clear
	genre = args.g[0]

	dictionary = genres

	if clear:
		clear_subgenres()
		return

	subgenre = get_subgenre(dictionary, genre)

	if not repeat:
		while subgenre_tracked(subgenre):
			if all_tracked(dictionary):
				print("All subgenres have been returned. Please clear the tracking or allow repeats.")
				return
			subgenre = get_subgenre(dictionary)

	if track:
		track_subgenre(subgenre)

	print(subgenre)


if __name__ == "__main__":
    main()

