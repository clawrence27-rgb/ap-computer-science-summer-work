
import requests # for getting website
import time #reapting the code
import bs4 #for getting webiste
import os # playing sound
#aiden showed me this thought it was cool
current = 311





def check_ufc_odds(url,tag, class_name): #function that parsing and gets the odds by adding to a new empty list

    that_url = url
    response = requests.get(that_url) # webpage
    html_data = response.text #  content
    parsed_data = bs4.BeautifulSoup(html_data, 'html.parser') # parses
    #find all the elements
    odds_element = parsed_data.find_all(tag, {'class':class_name})


    if odds_element: # this if stament has a empty function that gets a code appened by going through a loop of the elemnt and adds it ot
        odds_list = [] #empty list that holds odds
        for i in odds_element:
            odds_list.append(i.get_text()) # this loops appends to the odds_list
        return odds_list


def print_nice(my_list): #this takes the code and only prints the number i want insted of the whole string
    # Nicely prints a list of items
    for item in my_list:
        print(item)

url = f"https://www.ufc.com/event/ufc-{current}" #the url we are using

list_of_tags = 'span'
class_name = 'c-listing-fight__odds-amount' #what im trying to find

#put ths into a function
while True: # while true is always true bc true = true
    index = 1 #holds the fighter so it increases everytime and reset at the end
    odds = check_ufc_odds(url, list_of_tags, class_name)
    if odds:
        for odds in odds:
            print(f'Fighter {index}: {odds}') #prints the code with a f string so it update the fighter by one and the odds in the list
            index += 1 #updates fighter number
        print("END OF LIST") #just to see where the list ends
        #This see if the odds from the loop before is the not the same as the odds now it will play a sound

    time.sleep(2025) #repeats twenty twentyfve seonds learned from google


#fix this
previous_odds = 0 # placeholder
while check_ufc_odds(url, list_of_tags, class_name) != previous_odds:
    previous_odds = 0  # placeholder
    os.system("afplay sound.mp3") #took from google last class
    previous_odds = odds





