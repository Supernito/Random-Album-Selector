#! /usr/bin/python2
# -*- coding: utf-8 -*-
 
#    random album selector
#    Copyright (C) 2012  Juan "Nito" Pou  juanpou@ono.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

MIN_SONGS=4

import eyeD3, re, os, random
from os.path import dirname
from sys import argv

#LISTER
if len(argv)>1:
	if argv[1]=="list":
		PATH=raw_input("Write the path of your music library: ")
		if dirname(argv[0]):
			file_path=dirname(argv[0])+"/albums.list"
		else:
			file_path="./albums.list"
		dstfile= open(file_path,"w")
		albumlist=[]
		occurrences=[]
		rootdir = PATH
		for root, subFolders, files in os.walk(rootdir):
			for file in files:
				song=os.path.join(root,file)
				if re.match (".+\.mp3$|.+\.mp4$|.+\.wma$",song):
					tag = eyeD3.Tag()
					try: #tag.link(song) may thorw an exception due to encoding issues
						tag.link(song)
						dststring=tag.getArtist()+" - "+tag.getAlbum()
						dststring=dststring.encode('utf8')
						if dststring in albumlist:
							occurrences[albumlist.index(dststring)]+=1
						elif dststring not in albumlist and tag.getArtist() and tag.getAlbum():
							albumlist.append(dststring)
							occurrences.append(1)
					except:
						continue #keep going :D
		for album in albumlist:
			if occurrences[albumlist.index(album)]>=MIN_SONGS:
				dstfile.write(album)
				dstfile.write("\n")
#SELECTOR
albumlist=[]
if dirname(argv[0]):
	file_path=dirname(argv[0])+"/albums.list"
else:
	file_path="./albums.list"
dstfile= open(file_path,"r")
for album in dstfile:
	albumlist.append(album)
print (random.choice(albumlist))

