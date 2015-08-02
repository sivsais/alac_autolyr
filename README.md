Auto alac lyrics
Auto-Alac-Lyrics-Tagger
======================

This program will automatically search for the **Lyrics** of the song online then download the lyrics for the song and add then embed *Lyrics* to the *m4a* file via *mutagen* Tagger. All songs lyrics fetched in one go!

### Instructions
* If You have `pip` installed 
  * Type `pip install -r requirements.txt` to install all the dependecies
* If you don't have `pip` installed
  * The file requires *eyed3* and *BeautifulSoup* modules to work , so first install those dependencies
    * `$ sudo apt-get install pip` 
    * `$ sudo pip install mutagen`
    * `$ sudo pip install BeautifulSoup`
* Download the archive and extract the `.py` file wherever you have your song collections.
* Open the terminal in that directory
* Type `$ python alac_autolyr.py [-R] <file or directory name>`
* Wait for it to complete

####Side Note:
1. It currently works with English Songs only 
2. Requires *Python 2.7.8* with the module dependecies installed
3. It currently searches for songs lyrics based on the song name and artist, which placed in ID3 tags.
