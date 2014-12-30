import taglib
import magic
from os import path
from os import listdir

class mp3Collection:

    def __init__(self, directoryName):
        self.DirectoryName = directoryName
        self.Album = ''
        self.Year = ''
        
    def existsInCollection(self):
        return path.exists(self.convertSpacesToUnderscore(self.DirectoryName))
    
    def convertSpacesToUnderscore(self, title):
        return title.replace(' ','_')
    
    @staticmethod
    def isMusicDirectory(directoryName):
        songList = listdir(directoryName)
        isMusic = False
        
        for song in songList:
            if (str(magic.from_file(directoryName + '/' + song, mime=True)).find("audio") != -1):
                isMusic = True
                break

        return isMusic
    
    @staticmethod
    def getMusicFromDirectory(directoryName):
        musicList = []
        
        for i in listdir(directoryName):
            
            if (path.isdir(directoryName + '/' + i)):
                if (mp3Collection.isMusicDirectory(directoryName + '/' + i)):
                    musicList.append(i)
                
        return musicList
                