from bs4 import BeautifulSoup
import requests


class Search:

    def __init__(self, site, subject, mode):
        self.site = site
        self.subject = subject
        self.mode = mode

    def get_results(self):
        urls = []
        #search_url = "https://ca.search.yahoo.com/search;_ylt=AwrJ7KMAVrhg8V8AVHvrFAx.;_ylc=X1MDMjExNDcyMTAwMwRfcgMyBGZyA3lmcC10BGdwcmlkA3BMM0VLOEtFVHNpUVVESU5waUh5eUEEbl9yc2x0AzAEbl9zdWdnAzIEb3JpZ2luA2NhLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzY2BHF1ZXJ5A3NpdGUlM0FpbnRlcmVzdGluZ2VuZ2luZWVyaW5nLmNvbSUyMCUyMmhlaXNlbmJlcmclMjB1bmNlcnRhaW50eSUyMHByaW5jaXBsZSUyMgR0X3N0bXADMTYyMjY5MzQyNA--?p=site%3A"+self.site+"+%22"+self.subject+"%22&fr2=sb-top&fr=yfp-t&fp=1"
        
        if(self.mode == 1):
            subject_term = self.subject.replace(" ","+")
            search_url = "https://ca.search.yahoo.com/search;_ylt=AwrJ7KMAVrhg8V8AVHvrFAx.;_ylc=X1MDMjExNDcyMTAwMwRfcgMyBGZyA3lmcC10BGdwcmlkA3BMM0VLOEtFVHNpUVVESU5waUh5eUEEbl9yc2x0AzAEbl9zdWdnAzIEb3JpZ2luA2NhLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzY2BHF1ZXJ5A3NpdGUlM0FpbnRlcmVzdGluZ2VuZ2luZWVyaW5nLmNvbSUyMCUyMmhlaXNlbmJlcmclMjB1bmNlcnRhaW50eSUyMHByaW5jaXBsZSUyMgR0X3N0bXADMTYyMjY5MzQyNA--?p=site%3A"+self.site+"+"+subject_term+"&fr2=sb-top&fr=yfp-t&fp=1"
        else:
            search_url = "https://ca.search.yahoo.com/search;_ylt=AwrJ7KMAVrhg8V8AVHvrFAx.;_ylc=X1MDMjExNDcyMTAwMwRfcgMyBGZyA3lmcC10BGdwcmlkA3BMM0VLOEtFVHNpUVVESU5waUh5eUEEbl9yc2x0AzAEbl9zdWdnAzIEb3JpZ2luA2NhLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzY2BHF1ZXJ5A3NpdGUlM0FpbnRlcmVzdGluZ2VuZ2luZWVyaW5nLmNvbSUyMCUyMmhlaXNlbmJlcmclMjB1bmNlcnRhaW50eSUyMHByaW5jaXBsZSUyMgR0X3N0bXADMTYyMjY5MzQyNA--?p=site%3A"+self.site+"+%22"+self.subject+"%22&fr2=sb-top&fr=yfp-t&fp=1"
        
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
                                    urls.append(a['href'])
        return urls



