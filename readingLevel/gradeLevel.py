from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from math import log10, floor


#credit to AbigailB (https://stackoverflow.com/users/1798848/abigailb) 
def syllables(word):
    count = 0
    vowels = 'aeiouy'
    word = word.lower().strip(".:;?!")
    if word[0] in vowels:
        count += 1
    for index in range(1,len(word)):
        if word[index] in vowels and word[index-1] not in vowels:
            count += 1
    if word.endswith('e'):
        count -= 1
    if word.endswith('le'):
        count+=1
    if count == 0:
        count += 1
    return count

#credit to Paolo Moretti (https://stackoverflow.com/questions/13628791/how-do-i-check-whether-an-int-is-between-the-two-numbers) 
def round_to_1(x):
    return round(x, -int(floor(log10(abs(x)))))

#Assigns a School level to the Flesch reading score
def gradeLevel(score):
    if 0.0 <= score <= 30.0:
        grade = "College Graduate"
    elif 30.0 <= score <= 50.0:
        grade = "College"
    elif 50.0 <= score <= 60.0:
        grade = "10th to 12th Grade"
    elif 60.0 <= score <= 70.0:
        grade = "8th to 9th Grade"
    elif 70.0 <= score <= 80.0:
        grade = "7th Grade"
    elif 80.0 <= score <= 90.0:
        grade = "6th Grade"
    elif 90.0 <= score <= 100.0:
        grade = "5th Grade"
    else:
        grade = "Below 5th Grade"
    return grade

#site prompt, to be replaced by active tab browser address
#site = input("Enter the website to find out its reading level:")
#my_url = "{}".format(site)

#default site for testing
my_url = "https://en.wikipedia.org/wiki/Young_Thug"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#empty variables to be pushed w/ extracted, looped text
senNum = []
wordNum = []
syllNum = []

page_soup = soup(page_html, "html.parser")
page_soup.findAll("p")
paragraphs = page_soup.findAll("p")

#loop through every paragraph, do magic
for para in paragraphs:
    para = para.text.strip()
    if not para:
        continue
    paraSen = int(len(para.split('.')) - 1)
    paraWord = int(len(para.split()))
    paraSyll = syllables(para)
    intParaSen = int(paraSen)
    intParaWord = int(paraWord)
    intParaSyll = int(paraSyll)

    #append stripped values into empty variables
    senNum.append(intParaSen)
    wordNum.append(intParaWord)
    syllNum.append(intParaSyll)

#sums of all previously empty values
sumSenNum = sum(senNum)
sumWordNum = sum(wordNum)
sumSyllNum = sum(syllNum)

#averages for Flesch–Kincaid ease
avgWordsPerSen = sumWordNum/sumSenNum
avgSyllPerWord = sumSyllNum/sumWordNum
#print(avgWordsPerSen)
#print(avgSyllPerWord)

#final parts for Flesch–Kincaid ease
calcOne = avgWordsPerSen * 1.015
calcTwo = avgSyllPerWord * 84.6
finalCalc = 206.835 - calcOne - calcTwo
roundedFinalCalc = round_to_1(finalCalc)
finalGrade = gradeLevel(finalCalc)

print(finalCalc)
#print(roundedFinalCalc)
print(finalGrade)


