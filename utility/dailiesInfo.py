import string
import re

def gatherInformation(tString):
    returnList = []
    
    list = string.split(tString, ".")
    
    showExtension = list[len(list)-1]
    
    dateIndex = -1

    for idx,l in enumerate(list):
        matchCheck = re.search("201[56789]", l)
        if matchCheck != None:
            dateIndex = idx
            break
            
    if dateIndex == -1:
        return None

    
    showYear = list[dateIndex]
    
    dateList = list[dateIndex:dateIndex+3]
    
    showDate = '.'.join(dateList)
    
    nameList = list[:dateIndex]
    
    showName = ' '.join(nameList).title()

    returnList.append(showName)
    returnList.append(showYear)
    returnList.append(showDate)
    returnList.append(showExtension)
    return returnList