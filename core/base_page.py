
class BasePage:
    #Parent of all page objects.
    #contains generic methods for interaction and logging
    def __init__(self,page: page):
        self.page=page

    def navigate(self,url:str)->None :
        print(f"INFO:Navigating to {url}")
        self.page.goto(url)    

    def click(self,selector:str)->:
        # wait for element tobe visible and enabled before clicking
        print(f"INFO: Clicking on element {selector}") 

    def fill_text(self,selector:str,text:str)->None:
        # wait for element to be visible and enabled and clear before filling text
        print(f"INFO: Filling text {text} into element {selector}")
        self.page.fill(selector,text)

    def get_text(self,selector:str)->str:
        # wait for an element to be visible before getting text
        print(f"INFO: Getting text from element {selector}")
        return self.page.text_content(selector)

    def wait_for_url(self,url_fragment:str)->None:
        # wait for url to contain the specified fragment
        print(f"**/{url_fragment}")            

