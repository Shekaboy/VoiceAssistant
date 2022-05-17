# classes / Functions to open the default browser 
import webbrowser
class OpenWebsite:
    def __init__(self) -> None:
        pass
    def open_browser_with_url(self,url):
        webbrowser.open(url)
    def open_browser_with_query(self,query):
        webbrowser.open("https://www.google.com/search?q="+"+".join(query.split(" ")))
    def open_browser(self):
          webbrowser.open("https://www.google.com/")

if __name__ =="__main__":
    ow = OpenWebsite()
    ow.open_browser()
    ow.open_browser_with_query("Hello World")
    ow.open_browser_with_url("https://www.google.com")