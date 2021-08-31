from bs4 import BeautifulSoup
import requests, pathlib

class Articles:
    
    def __init__(self,url):
        self.url = url

    def text_analyse(self,text):
        t = 0
        watch_list = ["subscribing"]
        for w in watch_list:
            if text.find(w) != -1:
                t = t+1
        return t       


    def article(self):
        article_site = requests.get(self.url)
        article_soup = BeautifulSoup(article_site.content, 'html.parser')
        return article_soup
    
    def text(self, soup):
        if soup.find('article'):
            #print(colored(article_soup.find('article').get_text(),"yellow"))
            #article_text = article_soup.find('article').get_text()
            article_text = ""

            article_text_p = soup.find_all('p')
            for p in article_text_p:
                
                #t = self.text_analyse(p.get_text.strip())
                
                #look for link (menu, ads, etc)
                link = p.find_all('a')
                """
                for l in link:
                    print(l.get_text())
                """
                
                #text analyser
                t = 0
                watch_list = [
                    "subscribing", 
                    "subscribe",
                    "register now"
                    ]

                for w in watch_list:
                    if p.get_text().find(w) != -1:
                        t = t+1
                

                if t == 0:
                    article_text = article_text + p.get_text().strip() + "\n\n"
            return article_text
        
    def title(self, soup):
        if soup.find('article').find('h1'):
            return soup.find('article').find('h1').get_text()
        elif soup.find('h1'):
            return soup.find('h1').get_text()
        elif soup.find('article').find('h2'):
            return soup.find('article').find('h2').get_text()
        else:
            return ""

    def image(self, soup, website):

        article_img = ""
        img_list = []
        
        # multiple img
        if soup.find('article').find('img'):
            ilist = soup.find('article').find_all('img')
            for i in ilist:
                ilink = i['src']
                #print(ilink)
                img_link = ilink.rsplit("?")
                if img_link[0].find("base64") == -1:
                    if img_link[0].find("&") == -1:
                        if img_link[0].find("http") > -1:
                            ilink = img_link[0]
                        elif img_link[0].find("https") > -1:
                            ilink = img_link[0]
                        else:
                            ilink = "http://"+website+img_link[0]
                    else:
                        ilink = img_link[0]

                    img_filename = ilink.split("/")[-1]  
                    img_list.append([ilink, img_filename])

        return img_list
        
        # single img
        """
        if soup.find('article').find('img'):
            article_img = soup.find('article').find('img')['src']
        
        if article_img:
            img_link = article_img.rsplit("?")
            if img_link[0].find("base64") == -1:
                if img_link[0].find("&") == -1:
                    if img_link[0].find("http") > -1:
                        article_img = img_link[0]
                    elif img_link[0].find("https") > -1:
                        article_img = img_link[0]
                    else:
                        article_img = "http://"+website+img_link[0]
                else:
                    article_img = img_link[0]

                img_filename = article_img.split("/")[-1]  
            return [article_img, img_filename]
        """

    def url():
        pass
    
