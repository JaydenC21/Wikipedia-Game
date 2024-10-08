from queue import Queue
import wikipediaapi
import time

user_agent = "Wikipedia-Game (ch9597ja0331@pusd.us)"
wiki = wikipediaapi.Wikipedia(user_agent, "en")

def fetchLinks(page):
    linksList = []
    links = page.links
    for title in links.keys():
        linksList.append(title)
    return linksList

def wikipediaGameSolver(startPage, targetPage):
    print("Searching...")
    startTime = time.time()

    queue = Queue()
    visited = set()
    parent = {}

    queue.put(startPage.title)
    visited.add(startPage.title)
    while not queue.empty():
        currentPageTitle = queue.get()
        if currentPageTitle == targetPage.title:
            break

        currentPage = wiki.page(currentPageTitle)
        links = fetchLinks(currentPage)
        for link in links:
            if link not in visited:
                queue.put(link)
                visited.add(link)
                parent[link] = currentPageTitle
    path = []
    pageTitle = targetPage.title
    while pageTitle != startPage.title:
        path.append(pageTitle)
        pageTitle = parent[pageTitle]
    
    path.append(startPage.title)
    path.reverse()
    endTime = time.time()
    print("Solved in ", endTime - startTime, " seconds.")
    return path

startPage = wiki.page("Pasadena High School (California)")
targetPage = wiki.page("World War II")
path = wikipediaGameSolver(startPage, targetPage)
print(path)