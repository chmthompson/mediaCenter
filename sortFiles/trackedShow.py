import urllib.request
import xml.etree.ElementTree as ET
from sortFiles.models import TVShow

class trackedShow(TVShow):


    APIKEY = '43A5AC6A92833C2A'

    @staticmethod
    def GetAllShows():
        
        shows = ['test','test2','test3']
        xmlData = ET.parse(urllib.request.urlopen('http://thetvdb.com/api/Updates.php?type=none')).getroot()
        servertime = xmlData[0].text

        return shows
    
    @staticmethod
    def GetAllTrackedShows():
        return TVShow.objects.all()
    
    def __init__(self):
        pass
    
    def Add(self, showName, seriesNumber, episodeNumber):
        show = TVShow()
        show.CurrentSeries = seriesNumber
        show.ShowName = showName
        show.CurrentEpisode = episodeNumber
        show.save()
        
        return show.id
        