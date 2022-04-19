from ast import arg
from Search import Search
from Articles import Articles
from termcolor import colored
import requests, sys, shutil, json, time, datetime, pathlib, os, argparse

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

def console_output(website, subject, header, text_len, img, date):
    print('------------------------------------------------------')
    print("{} - {}".format(website,subject))
    print(r)
    print("Date: {}".format(date))
    print(colored("Title - {} ".format(header),"cyan"))
    print(colored("Article lenght - {}".format(text_len),"yellow"))
    print(colored("{} images found".format(len(img)),"magenta"))
    print(colored("Articles save successfully!","green"))
    print('------------------------------------------------------')

def console_reject(r):
    print('------------------------------------------------------')
    print (colored("{}".format(r),"yellow"))
    print (colored("This page don't look like an article ... i'm skipping it", "yellow"))
    print('------------------------------------------------------')

# Add argument listener for the search mode.
search_mode = argparse.ArgumentParser(description="Search mode")
search_mode.add_argument('-ns', '--nostrict', nargs='?', const=1, type=int, help="Search in nostrict mode")
search_mode.add_argument('-as', '--allsite', nargs='?', const=1, type=int, help="Ignore the website list and perform a search only with the subjects list")
search_mode.add_argument('-d', '--debug', nargs='?', const=1, type=int, help="Prevent search result from being saved")
search_mode.add_argument('-dp', '--depth', nargs='?', const=1, type=int, help="Number of page")
search_mode.add_argument('-bn', '--breakingnews', nargs='?', const=1, type=int, help="Switch the search url to news section")
args = search_mode.parse_args()


start = datetime.datetime.now()
print(colored("Webcrawler starting at {} ...".format(start),"green"))
if(args.nostrict == 1):
    print(colored("- No strict mode","yellow"))
else:
    print(colored("- Strict mode","yellow"))
print("Press CTRL-C to exit.")

path = "result"
if not os.path.exists(path):
    #os.makedirs('my_folder')
    os.mkdir(path)

existing_articles = load_article()

# load website and subject lists
website = get_file("website.txt")
subject = get_file("subject.txt")

debug_date = 0

if args.allsite == None:
    for s in subject:
        for w in website:
            look_up = Search(w,s, args.nostrict, args.allsite, args.depth, args.breakingnews)
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
                            article_date = page.date(article)

                            if article_date == "0000-00-00":
                                debug_date = debug_date + 1

                            header_count = len(header)
                            article_count = len(article)
                            text_count = len(text)
                            save_search = args.debug

                            if header_count != 0 and text_count > 200 and len(img) > 0 and save_search == None:

                                folder_term = s.replace(" ","_")
                                path_term = os.path.join(path,folder_term)
                                if args.breakingnews == None:
                                    title_folder = clean_title(header)
                                else:
                                    title_folder = "news_"+clean_title(header)

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
                                    time.sleep(.7)
                                            
                                if text:
                                    text = text.strip()
                                    #with open(path_article+'/Bilder/'+'Text.txt', 'w') as f:
                                    with open(path_article+'/Text.txt', 'w') as f:
                                        f.write(text)
                                    time.sleep(.7)
                                
                                if len(text) != 0:
                                    with open(path_article+'/Lenght.txt', 'w') as f:
                                        f.write(str(text_count))
                                    time.sleep(.7)
                                
                                if r:
                                    #with open(path_article+'/Bilder/'+'Link.txt', 'w') as f:
                                    with open(path_article+'/Link.txt', 'w') as f:
                                        f.write(r)
                                    time.sleep(.7)
                                
                                if article_date:
                                    #with open(path_article+'/Bilder/'+'Link.txt', 'w') as f:
                                    with open(path_article+'/'+article_date+'.txt', 'w') as f:
                                        f.write(article_date)
                                    time.sleep(.7)
                                
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
                                    imgt = len(img)
                                    for c,i in enumerate(img):
                                        path_img = path_article+'/img/'+i[1] 
                                        save_img(i[0], path_img)           
                                        #print(colored("Saving img{} of {} ".format(c,imgt),"green"))


                                console_output(w,s,header,text_count,img,article_date)
                                save_article_title(r)
                                time.sleep(.7)
                            elif header_count != 0 and text_count > 200 and len(img) > 0 and save_search == 1:
                                console_output(w,s,header,text_count,img,article_date)
                                time.sleep(.7)
        
                        except Exception as e:
                            console_reject(r)
                    else:
                        print(colored("Article already exist, skipping ...","red"))
            else:
                print(colored("No result found for {} on website {}".format(s,w),"red"))
else:
    for s in subject:
        look_up = Search("",s, args.nostrict, args.allsite, args.depth, args.breakingnews)
        result = look_up.get_results()
        site_name = ""

        if result:
            for r in result:
                if not is_article_exist(r, existing_articles):
                    try:
                        page = Articles(r)
                        article = page.article()
                        header = page.title(article).strip()
                        text = page.text(article).strip()
                        img = page.image(article,r)
                        article_date = page.date(article)

                        if article_date == "0000-00-00":
                            debug_date = debug_date + 1

                        header_count = len(header)
                        article_count = len(article)
                        text_count = len(text)
                        save_search = args.debug

                        if header_count != 0 and text_count > 200 and len(img) > 0 and save_search == None:

                            folder_term = s.replace(" ","_")
                            path_term = os.path.join(path,folder_term)

                            if args.breakingnews == None:
                                title_folder = clean_title(header)
                            else:
                                title_folder = "news_"+clean_title(header)

                            if not os.path.exists(path_term):
                                #os.makedirs('my_folder')
                                os.mkdir(path_term)

                            link = r.split("/")
                            #print(link)
                            site_name = link[2].replace("www.","")
                            path_site = os.path.join(path_term, site_name)        
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
                                time.sleep(.7)
                                        
                            if text:
                                text = text.strip()
                                #with open(path_article+'/Bilder/'+'Text.txt', 'w') as f:
                                with open(path_article+'/Text.txt', 'w') as f:
                                    f.write(text)
                                time.sleep(.7)
                            
                            if len(text) != 0:
                                with open(path_article+'/Lenght.txt', 'w') as f:
                                    f.write(str(text_count))
                                time.sleep(.7)
                            
                            if r:
                                #with open(path_article+'/Bilder/'+'Link.txt', 'w') as f:
                                with open(path_article+'/Link.txt', 'w') as f:
                                    f.write(r)
                                time.sleep(.7)
                            
                            if article_date:
                                #with open(path_article+'/Bilder/'+'Link.txt', 'w') as f:
                                with open(path_article+'/'+article_date+'.txt', 'w') as f:
                                    f.write(article_date)
                                time.sleep(.7)
                            
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
                                imgt = len(img)
                                for c,i in enumerate(img):
                                    path_img = path_article+'/img/'+i[1] 
                                    save_img(i[0], path_img)           
                                    #print(colored("Saving img{} of {} ".format(c,imgt),"green"))


                            console_output(site_name,s,header,text_count,img,article_date)
                            save_article_title(r)
                            time.sleep(.7)
                        elif header_count != 0 and text_count > 200 and len(img) > 0 and save_search == 1:
                            link = r.split("/")
                            site_name = link[2].replace("www.","")
                            console_output(site_name,s,header,text_count,img,article_date)
                            time.sleep(.7)

                    except Exception as e:
                        console_reject(r)
                else:
                    print(colored("Article already exist, skipping ...","red"))
        else:
            print(colored("No result found for {} on website {}".format(s,site_name),"red"))


end = datetime.datetime.now() - start       
print(colored("Web search is over!","green"))
print(colored("Program time {}".format(end),"green"))
print(colored("{} date missing".format(debug_date),"green"))



