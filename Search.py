from bs4 import BeautifulSoup
import requests


class Search:

    def __init__(self, site, subject, mode, allsite, depth, breaking_news):
        self.site = site
        self.subject = subject
        self.mode = mode
        self.allsite = allsite
        self.depth = depth
        self.breaking_news = breaking_news

    def get_results(self):
        urls = []
        page = 1
        
        if self.breaking_news == None:
            steps = 7
        else:
            steps = 10
        
        if self.depth == None:
            dp = 3
        else:
            dp = self.depth

        #search_url = "https://ca.search.yahoo.com/search;_ylt=AwrJ7KMAVrhg8V8AVHvrFAx.;_ylc=X1MDMjExNDcyMTAwMwRfcgMyBGZyA3lmcC10BGdwcmlkA3BMM0VLOEtFVHNpUVVESU5waUh5eUEEbl9yc2x0AzAEbl9zdWdnAzIEb3JpZ2luA2NhLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzY2BHF1ZXJ5A3NpdGUlM0FpbnRlcmVzdGluZ2VuZ2luZWVyaW5nLmNvbSUyMCUyMmhlaXNlbmJlcmclMjB1bmNlcnRhaW50eSUyMHByaW5jaXBsZSUyMgR0X3N0bXADMTYyMjY5MzQyNA--?p=site%3A"+self.site+"+%22"+self.subject+"%22&fr2=sb-top&fr=yfp-t&fp=1&b=1"
        
        for p in range(dp):
            if self.mode == 1:
                subject_term = self.subject.replace(" ","+")
                if self.allsite == 1:
                    if self.breaking_news == None:
                        search_url = "https://ca.search.yahoo.com/search;_ylt=AwrJ7KMAVrhg8V8AVHvrFAx.;_ylc=X1MDMjExNDcyMTAwMwRfcgMyBGZyA3lmcC10BGdwcmlkA3BMM0VLOEtFVHNpUVVESU5waUh5eUEEbl9yc2x0AzAEbl9zdWdnAzIEb3JpZ2luA2NhLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzY2BHF1ZXJ5A3NpdGUlM0FpbnRlcmVzdGluZ2VuZ2luZWVyaW5nLmNvbSUyMCUyMmhlaXNlbmJlcmclMjB1bmNlcnRhaW50eSUyMHByaW5jaXBsZSUyMgR0X3N0bXADMTYyMjY5MzQyNA--?p="+subject_term+"&fr2=sb-top&fr=yfp-t&fp=1&b="+str(page)
                    else:
                        #search_url = "https://news.search.yahoo.com/search;_ylt=AwrJ7KMAVrhg8V8AVHvrFAx.;_ylc=X1MDMjExNDcyMTAwMwRfcgMyBGZyA3lmcC10BGdwcmlkA3BMM0VLOEtFVHNpUVVESU5waUh5eUEEbl9yc2x0AzAEbl9zdWdnAzIEb3JpZ2luA2NhLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzY2BHF1ZXJ5A3NpdGUlM0FpbnRlcmVzdGluZ2VuZ2luZWVyaW5nLmNvbSUyMCUyMmhlaXNlbmJlcmclMjB1bmNlcnRhaW50eSUyMHByaW5jaXBsZSUyMgR0X3N0bXADMTYyMjY5MzQyNA--?p="+subject_term+"&fr2=sb-top&fr=yfp-t&fp=1&b="+str(page)
                        search_url = "https://news.search.yahoo.com/search;_ylt=AwrC1C7ZHl9iX0oAPQDQtDMD;_ylu=Y29sbwNiZjEEcG9zAzEEdnRpZAMEc2VjA3BhZ2luYXRpb24-?p="+subject_term+"&pz=10&fr=yfp-t&fr2=piv-web&bct=0&b="+str(page)+"&pz=10&bct=0&xargs=0"
                else:
                    if self.breaking_news == None:
                        search_url = "https://ca.search.yahoo.com/search;_ylt=AwrJ7KMAVrhg8V8AVHvrFAx.;_ylc=X1MDMjExNDcyMTAwMwRfcgMyBGZyA3lmcC10BGdwcmlkA3BMM0VLOEtFVHNpUVVESU5waUh5eUEEbl9yc2x0AzAEbl9zdWdnAzIEb3JpZ2luA2NhLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzY2BHF1ZXJ5A3NpdGUlM0FpbnRlcmVzdGluZ2VuZ2luZWVyaW5nLmNvbSUyMCUyMmhlaXNlbmJlcmclMjB1bmNlcnRhaW50eSUyMHByaW5jaXBsZSUyMgR0X3N0bXADMTYyMjY5MzQyNA--?p=site%3A"+self.site+"+"+subject_term+"&fr2=sb-top&fr=yfp-t&fp=1&b="+str(page)
                    else:
                        #search_url = "https://news.search.yahoo.com/search;_ylt=AwrJ7KMAVrhg8V8AVHvrFAx.;_ylc=X1MDMjExNDcyMTAwMwRfcgMyBGZyA3lmcC10BGdwcmlkA3BMM0VLOEtFVHNpUVVESU5waUh5eUEEbl9yc2x0AzAEbl9zdWdnAzIEb3JpZ2luA2NhLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzY2BHF1ZXJ5A3NpdGUlM0FpbnRlcmVzdGluZ2VuZ2luZWVyaW5nLmNvbSUyMCUyMmhlaXNlbmJlcmclMjB1bmNlcnRhaW50eSUyMHByaW5jaXBsZSUyMgR0X3N0bXADMTYyMjY5MzQyNA--?p=site%3A"+self.site+"+"+subject_term+"&fr2=sb-top&fr=yfp-t&fp=1&b="+str(page)
                        search_url = "https://news.search.yahoo.com/search;_ylt=AwrC1C7ZHl9iX0oAPQDQtDMD;_ylu=Y29sbwNiZjEEcG9zAzEEdnRpZAMEc2VjA3BhZ2luYXRpb24-?p=site%3A"+self.site+"+"+subject_term+"&pz=10&fr=yfp-t&fr2=piv-web&bct=0&b="+str(page)+"&pz=10&bct=0&xargs=0"
                    
                #search_url = "https://ca.search.yahoo.com/search;_ylt=AwrJ7KMAVrhg8V8AVHvrFAx.;_ylc=X1MDMjExNDcyMTAwMwRfcgMyBGZyA3lmcC10BGdwcmlkA3BMM0VLOEtFVHNpUVVESU5waUh5eUEEbl9yc2x0AzAEbl9zdWdnAzIEb3JpZ2luA2NhLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzY2BHF1ZXJ5A3NpdGUlM0FpbnRlcmVzdGluZ2VuZ2luZWVyaW5nLmNvbSUyMCUyMmhlaXNlbmJlcmclMjB1bmNlcnRhaW50eSUyMHByaW5jaXBsZSUyMgR0X3N0bXADMTYyMjY5MzQyNA--?p=site%3A"+self.site+"+"+subject_term+"&fr2=sb-top&fr=yfp-t&fp=1"
            else:
                if self.allsite == 1:
                    if self.breaking_news == None:
                        search_url = "https://ca.search.yahoo.com/search;_ylt=AwrJ7KMAVrhg8V8AVHvrFAx.;_ylc=X1MDMjExNDcyMTAwMwRfcgMyBGZyA3lmcC10BGdwcmlkA3BMM0VLOEtFVHNpUVVESU5waUh5eUEEbl9yc2x0AzAEbl9zdWdnAzIEb3JpZ2luA2NhLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzY2BHF1ZXJ5A3NpdGUlM0FpbnRlcmVzdGluZ2VuZ2luZWVyaW5nLmNvbSUyMCUyMmhlaXNlbmJlcmclMjB1bmNlcnRhaW50eSUyMHByaW5jaXBsZSUyMgR0X3N0bXADMTYyMjY5MzQyNA--?p=%22"+self.subject+"%22&fr2=sb-top&fr=yfp-t&fp=1&b="+str(page)
                    else:
                        #search_url = "https://news.search.yahoo.com/search;_ylt=AwrJ7KMAVrhg8V8AVHvrFAx.;_ylc=X1MDMjExNDcyMTAwMwRfcgMyBGZyA3lmcC10BGdwcmlkA3BMM0VLOEtFVHNpUVVESU5waUh5eUEEbl9yc2x0AzAEbl9zdWdnAzIEb3JpZ2luA2NhLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzY2BHF1ZXJ5A3NpdGUlM0FpbnRlcmVzdGluZ2VuZ2luZWVyaW5nLmNvbSUyMCUyMmhlaXNlbmJlcmclMjB1bmNlcnRhaW50eSUyMHByaW5jaXBsZSUyMgR0X3N0bXADMTYyMjY5MzQyNA--?p=%22"+self.subject+"%22&fr2=sb-top&fr=yfp-t&fp=1&b="+str(page)
                        search_url = "https://news.search.yahoo.com/search;_ylt=AwrC1C7ZHl9iX0oAPQDQtDMD;_ylu=Y29sbwNiZjEEcG9zAzEEdnRpZAMEc2VjA3BhZ2luYXRpb24-?p=%22"+self.subject+"%22&pz=10&fr=yfp-t&fr2=piv-web&bct=0&b="+str(page)+"&pz=10&bct=0&xargs=0"
                else:
                    if self.breaking_news == None:
                        search_url = "https://ca.search.yahoo.com/search;_ylt=AwrJ7KMAVrhg8V8AVHvrFAx.;_ylc=X1MDMjExNDcyMTAwMwRfcgMyBGZyA3lmcC10BGdwcmlkA3BMM0VLOEtFVHNpUVVESU5waUh5eUEEbl9yc2x0AzAEbl9zdWdnAzIEb3JpZ2luA2NhLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzY2BHF1ZXJ5A3NpdGUlM0FpbnRlcmVzdGluZ2VuZ2luZWVyaW5nLmNvbSUyMCUyMmhlaXNlbmJlcmclMjB1bmNlcnRhaW50eSUyMHByaW5jaXBsZSUyMgR0X3N0bXADMTYyMjY5MzQyNA--?p=site%3A"+self.site+"+%22"+self.subject+"%22&fr2=sb-top&fr=yfp-t&fp=1&b="+str(page)
                    else:
                        #search_url = "https://news.search.yahoo.com/search;_ylt=AwrJ7KMAVrhg8V8AVHvrFAx.;_ylc=X1MDMjExNDcyMTAwMwRfcgMyBGZyA3lmcC10BGdwcmlkA3BMM0VLOEtFVHNpUVVESU5waUh5eUEEbl9yc2x0AzAEbl9zdWdnAzIEb3JpZ2luA2NhLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzY2BHF1ZXJ5A3NpdGUlM0FpbnRlcmVzdGluZ2VuZ2luZWVyaW5nLmNvbSUyMCUyMmhlaXNlbmJlcmclMjB1bmNlcnRhaW50eSUyMHByaW5jaXBsZSUyMgR0X3N0bXADMTYyMjY5MzQyNA--?p=site%3A"+self.site+"+%22"+self.subject+"%22&fr2=sb-top&fr=yfp-t&fp=1&b="+str(page)
                        search_url = "https://news.search.yahoo.com/search;_ylt=AwrC1C7ZHl9iX0oAPQDQtDMD;_ylu=Y29sbwNiZjEEcG9zAzEEdnRpZAMEc2VjA3BhZ2luYXRpb24-?p=site%3A"+self.site+"+%22"+self.subject+"%22&pz=10&fr=yfp-t&fr2=piv-web&bct=0&b="+str(page)+"&pz=10&bct=0&xargs=0"
                    
                
                #search_url = "https://ca.search.yahoo.com/search;_ylt=AwrJ7KMAVrhg8V8AVHvrFAx.;_ylc=X1MDMjExNDcyMTAwMwRfcgMyBGZyA3lmcC10BGdwcmlkA3BMM0VLOEtFVHNpUVVESU5waUh5eUEEbl9yc2x0AzAEbl9zdWdnAzIEb3JpZ2luA2NhLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzY2BHF1ZXJ5A3NpdGUlM0FpbnRlcmVzdGluZ2VuZ2luZWVyaW5nLmNvbSUyMCUyMmhlaXNlbmJlcmclMjB1bmNlcnRhaW50eSUyMHByaW5jaXBsZSUyMgR0X3N0bXADMTYyMjY5MzQyNA--?p=site%3A"+self.site+"+%22"+self.subject+"%22&fr2=sb-top&fr=yfp-t&fp=1"
            
            website = requests.get(search_url)
            soup = BeautifulSoup(website.content, 'html.parser')

            #print(soup.prettify())
            #break

            if self.breaking_news == None:
                result = soup.find('div', {"id":"web"})
            else:
                result = soup.find('div', {"id":"main"})

            li = result.find_all('li')
            #print(result)
            for l in li:
                a = l.find('a')
                
                if a:
                    if a.get_text() != "Cached":
                        if a.get_text() != "Yahoo Search Help Center":
                            if a['href'].find("images.") == -1:
                                if a['href'].find(".pdf") == -1:
                                    if a['href'].find(".stm") == -1:
                                        if a['href'].find(".video") == -1:
                                            urls.append(a['href'])
                                            
                
            page = page + steps
        
        """
        if self.mode == 1:
            subject_term = self.subject.replace(" ","+")
            if self.allsite == 1:
                search_url = "https://ca.search.yahoo.com/search;_ylt=AwrJ7KMAVrhg8V8AVHvrFAx.;_ylc=X1MDMjExNDcyMTAwMwRfcgMyBGZyA3lmcC10BGdwcmlkA3BMM0VLOEtFVHNpUVVESU5waUh5eUEEbl9yc2x0AzAEbl9zdWdnAzIEb3JpZ2luA2NhLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzY2BHF1ZXJ5A3NpdGUlM0FpbnRlcmVzdGluZ2VuZ2luZWVyaW5nLmNvbSUyMCUyMmhlaXNlbmJlcmclMjB1bmNlcnRhaW50eSUyMHByaW5jaXBsZSUyMgR0X3N0bXADMTYyMjY5MzQyNA--?p="+subject_term+"&fr2=sb-top&fr=yfp-t&fp=1"
            else:
                search_url = "https://ca.search.yahoo.com/search;_ylt=AwrJ7KMAVrhg8V8AVHvrFAx.;_ylc=X1MDMjExNDcyMTAwMwRfcgMyBGZyA3lmcC10BGdwcmlkA3BMM0VLOEtFVHNpUVVESU5waUh5eUEEbl9yc2x0AzAEbl9zdWdnAzIEb3JpZ2luA2NhLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzY2BHF1ZXJ5A3NpdGUlM0FpbnRlcmVzdGluZ2VuZ2luZWVyaW5nLmNvbSUyMCUyMmhlaXNlbmJlcmclMjB1bmNlcnRhaW50eSUyMHByaW5jaXBsZSUyMgR0X3N0bXADMTYyMjY5MzQyNA--?p=site%3A"+self.site+"+"+subject_term+"&fr2=sb-top&fr=yfp-t&fp=1"
                
            #search_url = "https://ca.search.yahoo.com/search;_ylt=AwrJ7KMAVrhg8V8AVHvrFAx.;_ylc=X1MDMjExNDcyMTAwMwRfcgMyBGZyA3lmcC10BGdwcmlkA3BMM0VLOEtFVHNpUVVESU5waUh5eUEEbl9yc2x0AzAEbl9zdWdnAzIEb3JpZ2luA2NhLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzY2BHF1ZXJ5A3NpdGUlM0FpbnRlcmVzdGluZ2VuZ2luZWVyaW5nLmNvbSUyMCUyMmhlaXNlbmJlcmclMjB1bmNlcnRhaW50eSUyMHByaW5jaXBsZSUyMgR0X3N0bXADMTYyMjY5MzQyNA--?p=site%3A"+self.site+"+"+subject_term+"&fr2=sb-top&fr=yfp-t&fp=1"
        else:
            if self.allsite == 1:
                search_url = "https://ca.search.yahoo.com/search;_ylt=AwrJ7KMAVrhg8V8AVHvrFAx.;_ylc=X1MDMjExNDcyMTAwMwRfcgMyBGZyA3lmcC10BGdwcmlkA3BMM0VLOEtFVHNpUVVESU5waUh5eUEEbl9yc2x0AzAEbl9zdWdnAzIEb3JpZ2luA2NhLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzY2BHF1ZXJ5A3NpdGUlM0FpbnRlcmVzdGluZ2VuZ2luZWVyaW5nLmNvbSUyMCUyMmhlaXNlbmJlcmclMjB1bmNlcnRhaW50eSUyMHByaW5jaXBsZSUyMgR0X3N0bXADMTYyMjY5MzQyNA--?p=%22"+self.subject+"%22&fr2=sb-top&fr=yfp-t&fp=1"
            else:
                search_url = "https://ca.search.yahoo.com/search;_ylt=AwrJ7KMAVrhg8V8AVHvrFAx.;_ylc=X1MDMjExNDcyMTAwMwRfcgMyBGZyA3lmcC10BGdwcmlkA3BMM0VLOEtFVHNpUVVESU5waUh5eUEEbl9yc2x0AzAEbl9zdWdnAzIEb3JpZ2luA2NhLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzY2BHF1ZXJ5A3NpdGUlM0FpbnRlcmVzdGluZ2VuZ2luZWVyaW5nLmNvbSUyMCUyMmhlaXNlbmJlcmclMjB1bmNlcnRhaW50eSUyMHByaW5jaXBsZSUyMgR0X3N0bXADMTYyMjY5MzQyNA--?p=site%3A"+self.site+"+%22"+self.subject+"%22&fr2=sb-top&fr=yfp-t&fp=1"
                pass
            
            #search_url = "https://ca.search.yahoo.com/search;_ylt=AwrJ7KMAVrhg8V8AVHvrFAx.;_ylc=X1MDMjExNDcyMTAwMwRfcgMyBGZyA3lmcC10BGdwcmlkA3BMM0VLOEtFVHNpUVVESU5waUh5eUEEbl9yc2x0AzAEbl9zdWdnAzIEb3JpZ2luA2NhLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzY2BHF1ZXJ5A3NpdGUlM0FpbnRlcmVzdGluZ2VuZ2luZWVyaW5nLmNvbSUyMCUyMmhlaXNlbmJlcmclMjB1bmNlcnRhaW50eSUyMHByaW5jaXBsZSUyMgR0X3N0bXADMTYyMjY5MzQyNA--?p=site%3A"+self.site+"+%22"+self.subject+"%22&fr2=sb-top&fr=yfp-t&fp=1"
        
        website = requests.get(search_url)
        soup = BeautifulSoup(website.content, 'html.parser')

        result = soup.find('div', {"id":"web"})
        li = result.find_all('li')

        for l in li:
            a = l.find('a')
            if a:
                if a.get_text() != "Cached":
                    if a.get_text() != "Yahoo Search Help Center":
                        if a['href'].find("images.") == -1:
                            if a['href'].find(".pdf") == -1:
                                if a['href'].find(".stm") == -1:
                                    if a['href'].find(".video") == -1:
                                        urls.append(a['href'])
        """

        return urls



