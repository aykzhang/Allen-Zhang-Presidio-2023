'''
Allen Zhang

Presidio

Problem statement: Develop a program that accepts a topic as a string input from the user, searches the internet for information about it, and answers any questions regarding the topic.

- Try to use your imagination to make the program more interesting and useful. 

- Feel free to use the languages and technologies with which you feel most comfortable. 

- Incorporate the standards and best practices you are familiar with. 

- Document the code (add comments as appropriate) 

- Provide instructions to run the code. 
'''
import wikipedia
import googlesearch

#Function used to search Wikipedia for a given topic
def wikipediaSearch(topic):
    print("==========================")
    print("Here are some related Wikipedia articles for " + topic)
    #Uses wikipedia Library to search for the top 5 results of the topic
    searchList = wikipedia.search(topic, results = 5, suggestion = False)
    for search in searchList:
        try:
            #Get searched term WikipediaPage object
            page = wikipedia.page(search, auto_suggest=False)
            #Print all related info
            print("==========================")
            print("Title: " + page.title)
            print("URL: " + page.url)
            print("Summary: \n" + page.summary)
            print("")
        except wikipedia.DisambiguationError as e:
            #Searched page was a Disambiguation Page, continue
            pass

#Function used to search Google for a given topic
def googleSearch(topic):
    print("==========================")
    print("Here are some links according to a Google search regarding " + topic)
    prev = []
    #Uses googlesearch Library to get the top Google searches regarding the user input
    googleSearches = googlesearch.search(topic, advanced=True)
    for search in googleSearches:
        #Check to see if there is a duplicate search
        if search.url in prev:
            continue
        #Print all related info
        print("==========================")
        print("Title: " + search.title)
        print("URL: " + search.url)
        print("Description: \n" + search.description)
        print("")
        prev.append(search.url)

#Function to start the search process
def startSearch():
    print("==========================")
    print("Hello, welcome to a janky search, using Wikipedia and Google")

    #Get search type
    searchChoice = input("Please input which type of search you would like to use (1 for Google, 2 for Wikipedia, 3 for both): ")
    while(searchChoice not in ["1","2","3"]):
        print("Please input a number from 1 to 3")
        searchChoice = input("Please input which type of search you would like to use (1 for Google, 2 for Wikipedia, 3 for both): ")

    #Get search topic
    topic = input("Please input what you want to search: ")

    #Get search results
    if(searchChoice == "1"):
        googleSearch(topic)
    if(searchChoice == "2"):
        wikipediaSearch(topic)
    if(searchChoice == "3"):
        googleSearch(topic)
        wikipediaSearch(topic)

    #Determine if user still wants to search
    again = input("Would you like to search again? (y/n): ")

    while(again not in ["y","n"]):
        print("Please input either y or n")
        again = input("Would you like to search again? (y/n): ")

    if(again == "y"):
        startSearch()

    if(again == "n"):
        print("Thank you for using my janky search")
        exit()


def main():
    startSearch()

if __name__ == '__main__':
    main()



