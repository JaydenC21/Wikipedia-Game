import wikipediaapi
import time

user_agent = "Wikipedia-Game (ch9597ja0331@pusd.us)"
wiki = wikipediaapi.Wikipedia(user_agent, "en")

startPage = wiki.page("Pasadena High School (California)")
targetPage = wiki.page("Rose Parade")

def fetchLinks(page):
    linksList = []
    links = page.links
    for title in links.keys():
        linksList.append(title)
    return linksList

def wikipediaGameSolver(startPage, targetPage):
    links = fetchLinks(startPage)
    for link in links:
        if link == targetPage.title:
            print("Target acquired: " + link)
            break

wikipediaGameSolver(startPage, targetPage)