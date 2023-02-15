def extractDomainFromURL(url):
    url = url.replace("http://", "")
    url = url.replace("https://", "")
    url = url.replace("www.", "")
    
    domain1 = url.split(".")[0]
    url = url.split(".")[1]
    domain2 = url.split("/")[0]
    return (domain1 +"."+ domain2)

def printDomainName(list):
    for i in range(len(list)):
        print(extractDomainFromURL(list[i]), end = "\n")

list = ["https://heroku.com/repo", "https://github.com/repository", "https://facebook.com/feed", "www.google.com", "http://instagram.in/chat/reply", "https://twitter.us/tweet"]
printDomainName(list)
