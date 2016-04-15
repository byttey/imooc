'''
Created on 2016Äê4ÔÂ15ÈÕ

@author: Bytterin
'''
from baike_spider import url_manager, html_downloader, html_outputer, html_parser
from itertools import count

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UlrManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    
    def craw(self, root_url):
        self.urls.add_new_url(root_url)
        try:
            while self.urls.has_new_url():
                count = 1
                new_url = root_url
    #             print 'craw %d : %s' % ()
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                count += 1
                
                if count == 100:
                    break;
        except:
            print "craw faild"
        self.outputer.output_html()
            
            
    
    
        
if __name__ == "__main__":
#     http://tieba.baidu.com/f?kw=%E6%8A%8A%E6%98%8E%E5%A4%A9%E7%BB%99%E4%BD%A0&ie=utf-8
    root_url = "http://tieba.baidu.com/f?kw=%E6%8A%8A%E6%98%8E%E5%A4%A9%E7%BB%99%E4%BD%A0&ie=utf-8"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

