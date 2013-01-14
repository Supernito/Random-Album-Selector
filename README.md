You need python (http://www.python.org/download/releases/) 
and eyed3 python library (http://eyed3.nicfit.net/)
Run it as a usual python program.
If it's the first time or you want to refresh the list of 
albums run the program with the parameter 'list'

python chooser.py list

otherway run it without parameters

python chooser.py

When running the program to make a list it will ask for 
the path where your music library is. Write it without
quotes and without slash at the end. For example, this is mine:

Write the path of your music library: /home/nito/Escritorio/Mi música

This will create a file albums.list with all of the albums which
you have 4 or more songs in your library according the tags.
You can change this default number easily changing the variable
MIN_SONGS in the source code.

List file is a normal text file, if you want to edit it manually 
for some strange reason, you can do it.


