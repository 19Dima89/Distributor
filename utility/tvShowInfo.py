import string
import re

def gatherInformation(tString):
    returnList = []
    
    list = string.split(tString, ".")
    
    showExtension = list[len(list)-1]
    
    seasonEpisodeIndex = -1

    for idx,l in enumerate(list):
        matchCheck = re.search("[Ss][0-9][0-9][Ee][0-9][0-9]", l)
        if matchCheck != None:
            seasonEpisodeIndex = idx
            break
        
        matchCheck = re.search("[Ss][0-9][0-9][Ee][0-9][0-9][Ee][0-9][0-9]", l)
        if matchCheck != None:
            seasonEpisodeIndex = idx
            break
            
    if seasonEpisodeIndex == -1:
        return None
    
    showSeasonAndEpisode=list[seasonEpisodeIndex]
            
    nameList = list[:seasonEpisodeIndex]

    showName = ' '.join(nameList).title()

    if list[seasonEpisodeIndex][1] == "0":
        showSeason = list[seasonEpisodeIndex][2]
    else:
        showSeason = list[seasonEpisodeIndex][1:3]

    returnList.append(showName)
    returnList.append(showSeason)
    returnList.append(showExtension)
    returnList.append(showSeasonAndEpisode)
    return returnList