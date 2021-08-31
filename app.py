from Search import Search
from Articles import Articles
from termcolor import colored
import requests, sys, shutil, json, time, datetime, pathlib, os

def get_time():
    now = datetime.datetime.now()
    timename = now.strftime("%Y%m%d")+"-"+now.strftime("%H%M%S%f")
    return timename

def save_img(url, path):
    r = requests.get(url)
    
    with open(path, "wb") as f:
        f.write(r.content)
    #print("Img save : "+path)

def get_file(filename):
    content = []
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            for l in f:
                if l.find("\n") != -1:
                    l = l[:-1].strip()
                content.append(l)
    else:
        content.append("File "+filename +" doesn't exist")
        #with open(filename, 'w') as f:
            #f.write('')
    return content

def save_article_title(url):
    with open('article_list.txt', 'a') as f:
        f.write(url+'\n')

def is_article_exist(url,urls):
    if url in urls:
        return True
    return False
    
def load_article():
    url = []
    if os.path.exists('article_list.txt'):
        with open('article_list.txt', 'r') as f:
            for l in f:
                l = l[:-1].strip()
                url.append(l)
    else:
        url.append("File doesn't exist")
        with open('article_list.txt', 'w') as f:
            f.write('')
    return url

def clean_title(title):
    t = title.replace(" ","-")
    t = t.replace("'","")
    t = t.replace("\"","")
    t = t.replace(",","")
    t = t.replace(".","")
    return t.lower()

def console_output(website, subject, header, text_len, img):
    print('------------------------------------------------------')
    print("{} - {}".format(w,s))
    print(r)
    print(colored("Title - {} ".format(header),"cyan"))
    print(colored("Article lenght - {}".format(text_len),"yellow"))
    print(colored("{} images found".format(len(img)),"magenta"))
    print(colored("Articles save successfully!","green"))
    print('------------------------------------------------------')

start = datetime.datetime.now()
print(colored("Webcrawler starting at {} ...".format(start),"green"))

path = "result"
if not os.path.exists(path):
    #os.makedirs('my_folder')
    os.mkdir(path)

existing_articles = load_article()

# load website and subject lists
website = get_file("website.txt")
subject = get_file("subject.txt")

for s in subject:
    for w in website:
        look_up = Search(w,s)
        result = look_up.get_results()

        if result:
            for r in result:
                if not is_article_exist(r, existing_articles):
                    try:
                        page = Articles(r)
                        article = page.article()
                        header = page.title(article).strip()
                        text = page.text(article).strip()
                        img = page.image(article,r)

                        header_count = len(header)
                        article_count = len(article)
                        text_count = len(text)

                        if header_count != 0:

                            folder_term = s.replace(" ","_")
                            path_term = os.path.join(path,folder_term)
                            title_folder = clean_title(header)

                            if not os.path.exists(path_term):
                                #os.makedirs('my_folder')
                                os.mkdir(path_term)

                            path_site = os.path.join(path_term, w)        
                            if not os.path.exists(path_site):
                                #os.makedirs('my_folder')
                                os.mkdir(path_site)

                            #path_article = os.path.join(path_site,get_time())
                            path_article = os.path.join(path_site,title_folder)
                            os.mkdir(path_article)
                            #os.mkdir(path_article+'/Bilder')

                            if header:
                                #with open(path_article+'/Bilder/'+'Headline.txt', 'w') as f:
                                with open(path_article+'/Headline.txt', 'w') as f:
                                    f.write(header)
                                time.sleep(.5)
                                        
                            if text:
                                text = text.strip()
                                #with open(path_article+'/Bilder/'+'Text.txt', 'w') as f:
                                with open(path_article+'/Text.txt', 'w') as f:
                                    f.write(text)
                                time.sleep(.5)
                            
                            if r:
                                #with open(path_article+'/Bilder/'+'Link.txt', 'w') as f:
                                with open(path_article+'/Link.txt', 'w') as f:
                                    f.write(r)
                                time.sleep(.5)
                            
                            # single img
                            """
                            if img:
                                os.mkdir(path_article+'/Bilder/img')
                                path_img = path_article+'/Bilder/img/'+img[1] 
                                save_img(img[0], path_img)
                            """
                            # multiple img
                            if img:
                                os.mkdir(path_article+'/img')
                                if len(img) > 1:
                                    os.mkdir(path_article+'/img/extra')
                                for c,i in enumerate(img):
                                    if c == 0:
                                        path_img = path_article+'/img/'+i[1] 
                                        save_img(i[0], path_img)
                                    else:
                                        path_img = path_article+'/img/extra/'+i[1] 
                                        save_img(i[0], path_img)

                            console_output(w,s,header,text_count,img)
                            save_article_title(r)
                            time.sleep(.5)
                    except Exception as e:
                        print ('analyzing ...')
                else:
                    print(colored("Article already exist, skipping ...","red"))
        else:
            print(colored("No result found for {} on website {}".format(s,w),"red"))

end = datetime.datetime.now() - start       
print(colored("Web search is over!","green"))
print(colored("Program time {}".format(end),"green"))



