from datetime import datetime
from bs4 import BeautifulSoup
import requests, pathlib, re

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
            #article_soup = soup.find('article')
            article_text = ""

            article_text_p = soup.find_all('p')
            #article_text_p = article_soup.find_all('p')
            for p in article_text_p:
                
                #text analyser
                t = 0
                watch_list = [
                    "subscribing",
                    "Subscribing", 
                    "subscribe",
                    "Subscribe",
                    "subscription",
                    "Subscription",
                    "register now",
                    "Newsletter",
                    "newsletter",
                    "Newsletters",
                    "newsletters",
                    "mailinglist",
                    "Previous image",
                    "Next image",
                    "Previous item",
                    "Next item",
                    "Save",
                    "Follow us",
                    "Sign in",
                    "Cancel",
                    "cancel",
                    "Cookie",
                    "cookie",
                    "Cookies",
                    "cookies",
                    "Email",
                    "email"
                    ]

                for w in watch_list:
                    if p.get_text().find(w) != -1:
                        t = t+1
                
                #if len(p.get_text()) < 25:
                    #t = t+1

                #look for link (menu, ads, etc)
                if p.find_parents('a'):
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
    
    def date_mdy(self, soup):
        alphabet_soup = soup
        datex = re.findall("[A-Za-z]+\s[0-9]+,?\s[0-9]+", alphabet_soup)
        return datex

    def date_dmy(self, soup):
        alphabet_soup = soup
        datex = re.findall("[0-9]+\s[A-Za-z]+,?\s[0-9]+", alphabet_soup)
        return datex

    def date_slash(self, soup):
        alphabet_soup = soup
        datex = re.findall("[0-9]+\\/[0-9]+\\/[0-9]+", alphabet_soup)
        return datex

    def date_dash(self, soup):
        alphabet_soup = soup
        datex = re.findall("[0-9]+-[0-9]+-[0-9]+", alphabet_soup)
        return datex

    def date_without_year(self, soup):
        alphabet_soup = soup
        datex = re.match("(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s[0-9]+", alphabet_soup)
        if datex != None:
             array_date = datex.group().split(" ")
        else:
            array_date = []
        return array_date

    def extract_date(self,date_val,type,month_dict):
        fulltime = str(date_val)
        fulltime = fulltime.replace(",","")
        array_date = fulltime.split(" ")

        if type == 0:
            month_value = array_date[0].lower()
            if month_value.isalpha():
                for m,n in month_dict.items():
                    #if month_value == m:
                    if m.find(month_value) != -1:
                        month = n
            else:
                month = month_value
            
            days_format = int(array_date[1]) if int(array_date[1]) > 10 else int('00')+int(array_date[1])
            published_date = array_date[2]+"-"+month+"-"+str(days_format)
        elif type == 1:
            month_value = array_date[1].lower()
            if month_value.isalpha():
                for m,n in month_dict.items():
                    #if month_value == m:
                    if m.find(month_value) != -1:
                        month = n
            else:
                month = month_value
                
            days_format = int(array_date[0]) if int(array_date[0]) > 10 else int('00')+int(array_date[0])
            published_date = array_date[2]+"-"+month+"-"+str(days_format)
        elif type == 2:
            dash_date_array = date_val[0].split("/")
            published_date = dash_date_array[2]+"-"+dash_date_array[1]+"-"+dash_date_array[0] 
        elif type == 3:
            published_date = str(date_val[0])
        elif type == 4:
            month_value = array_date[0].lower()
            if month_value.isalpha():
                for m,n in month_dict.items():
                    #if month_value == m:
                    if m.find(month_value) != -1:
                        month = n
            else:
                month = month_value
            ct = datetime.datetime.now()
            today = ct.date()
            year = today.strftime("%Y")
            days_format = int(array_date[1]) if int(array_date[1]) > 10 else int('00')+int(array_date[1])
            published_date = year+"-"+month+"-"+str(days_format)
        else:
            pass

        return published_date


    def date(self, soup):
        month_dict = {
            "january":   "01",
            "febuary":   "02",
            "march":     "03",
            "april":     "04",
            "may":       "05",
            "june":      "06",
            "july":      "07",
            "august":    "08",
            "september": "09",
            "october":   "10",
            "november":  "11",
            "december":  "12"
        }

        published_date = "0000-00-00"
        
        try:
            if soup.find("article").find("time"):
                #print("Time in article tag exist")
                time = soup.find("article").find("time")
                #print(time)
                for k,v in time.attrs.items():
                    if k == "datetime":
                        fulltime = time['datetime'].split("T")
                        article_date = fulltime[0].split("-")
                        published_date = article_date[0]+"-"+article_date[1]+"-"+article_date[2]
                        break
                    elif k == "content":
                        special_characters = [',','/','.','-']
                        fulltime = time['content'].strip()
                        fulltime = ''.join(filter(lambda i:i not in special_characters, fulltime))
                        fulltime = fulltime.split(" ")

                        month_value = fulltime[0].lower()

                        if month_value.isalpha():
                            for m,n in month_dict.items():
                                #if month_value == m:
                                if m.find(month_value) != -1:
                                    month = n
                        else:
                            month = month_value

                        #article_date = [fulltime[2], month, fulltime[1]]
                        published_date = fulltime[2]+"-"+month+"-"+fulltime[1]
                        break
                    else:
                        #print(time.attrs)
                        published_date = "0000-00-00"
                #print(published_date)
                return published_date

            elif soup.find("time"):
                #print("Time tag exist")
                time = soup.find("time")
                #print(time)
                for k,v in time.attrs.items():
                    if k == "datetime":
                        fulltime = time['datetime'].split("T")
                        article_date = fulltime[0].split("-")
                        published_date = article_date[0]+"-"+article_date[1]+"-"+article_date[2]
                        break
                    elif k == "content":
                        special_characters = [',','/','.','-']
                        fulltime = time['content'].strip()
                        fulltime = ''.join(filter(lambda i:i not in special_characters, fulltime))
                        fulltime = fulltime.split(" ")

                        month_value = fulltime[0].lower()

                        if month_value.isalpha():
                            for m,n in month_dict.items():
                                #if month_value == m:
                                if m.find(month_value) != -1:
                                    month = n
                        else:
                            month = month_value

                        #article_date = [fulltime[2], month, fulltime[1]]
                        published_date = fulltime[2]+"-"+month+"-"+fulltime[1]
                        break
                    else:
                        #print(time.attrs)
                        published_date = "0000-00-00"
                #print(published_date)
                return published_date
            else:
                if soup.find("article"):
                    soup_date = str(soup.find("article"))
                else:
                    soup_date = str(soup.find("body"))
                
                #soup_date = str(soup.find("body"))

                search_date = self.date_mdy(soup_date) # Aaa+ 00, 0000
                rev_text_date = self.date_dmy(soup_date) # 00 Aaa+, 0000
                slash_date = self.date_slash(soup_date) # 00/00/0000
                dash_date = self.date_dash(soup_date) # 00-00-0000
                noyear_date = self.date_without_year(soup_date) # Aaa 00

                """
                print(search_date[0])
                sd = self.extract_date(search_date[0], 0, month_dict)
                print("Search "+ sd)

                print(rev_text_date[0])
                rd = self.extract_date(rev_text_date[0], 1, month_dict)
                print("rd "+ rd)

                print(slash_date[0])
                sd = self.extract_date(slash_date[0], 2, month_dict)
                print("sd "+ sd)

                print(dash_date[0])
                dd = self.extract_date(dash_date[0], 3, month_dict)
                print("Dash "+ dd)

                print(noyear_date[0])
                nyd = self.extract_date(noyear_date[0], 4, month_dict)
                print("nyd "+ nyd)
                """
                if len(search_date) > 0:
                    published_date = self.extract_date(search_date[0], 0, month_dict)
                    #print("Pub "+published_date)
                elif len(rev_text_date) > 0:
                    published_date = self.extract_date(rev_text_date[0], 1, month_dict)
                    #print("Pub "+published_date)
                elif len(slash_date) > 0:
                    published_date = self.extract_date(slash_date[0], 2, month_dict) 
                    #print("Pub "+published_date)
                elif len(dash_date) > 0:
                    published_date = self.extract_date(dash_date[0], 3, month_dict)
                    #print("Pub "+published_date)
                elif len(noyear_date) > 0:
                    published_date = self.extract_date(noyear_date[0], 4, month_dict)
                    #print("Pub "+published_date)
                else:
                    published_date = "0000-00-00"
                    #print("Pub "+published_date)

                #print("Final "+published_date)
                
        except Exception as e:
            #print("No date available")
            #print(e)
            #published_date = "0000-00-00"
            pass
        
        return published_date

    def regextime(self, soup, month_dict, mode):

        if mode == 'article':
            search_date = soup.find('article').findAll(text=re.compile('[A-Za-z]+\s[0-9]+,?\s[0-9]+')) # Aaa+ 00, 0000
            rev_text_date = soup.find('article').findAll(text=re.compile('[0-9]+\s[A-Za-z]+,?\s[0-9]+')) # 00 Aaa+, 0000
            dash_date = soup.find('article').findAll(text=re.compile('[0-9]+\\/[0-9]+\\/[0-9]+')) # 00/00/0000
        else:
            search_date = soup.findAll(text=re.compile('[A-Za-z]+\s[0-9]+,?\s[0-9]+')) # Aaa+ 00, 0000
            rev_text_date = soup.findAll(text=re.compile('[0-9]+\s[A-Za-z]+,?\s[0-9]+')) # 00 Aaa+, 0000
            dash_date = soup.findAll(text=re.compile('[0-9]+\\/[0-9]+\\/[0-9]+')) # 00/00/0000

        if len(search_date) > 0:
            fulltime = search_date[0]
            fulltime = fulltime.replace(",","")
            array_date = fulltime.split(" ")
            month_value = array_date[0].lower()

            if month_value.isalpha():
                for m,n in month_dict.items():
                    #if month_value == m:
                    if m.find(month_value) != -1:
                        month = n
            else:
                month = month_value

            published_date = array_date[2]+"-"+month+"-"+array_date[1]
            #print(published_date)
        elif len(rev_text_date) > 0:
            fulltime = rev_text_date[0]
            fulltime = fulltime.replace(",","")
            array_date = fulltime.split(" ")
            month_value = array_date[1].lower()

            if month_value.isalpha():
                for m,n in month_dict.items():
                    #if month_value == m:
                    if m.find(month_value) != -1:
                        month = n
            else:
                month = month_value

            published_date = array_date[2]+"-"+month+"-"+array_date[0]
            #print(published_date)
        elif len(dash_date) > 0:
            dash_date_array = dash_date.split("/")
            published_date = dash_date_array[2]+"-"+dash_date_array[1]+"-"+dash_date_array[0] 
            #print(published_date)
        else:
            pass

        return published_date
    
    
        