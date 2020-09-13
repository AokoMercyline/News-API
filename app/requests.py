from newsapi import NewsApiClient
# from ..config import 

class NewsRequests:
    API_KEY = '1c6caded5f054d598bf505ff7f0491a6'
    n = NewsApiClient(api_key=API_KEY)
    
    def get_top_headlines(self,**kwargs):
        return self.n.get_top_headlines(**kwargs)
    
    def get_everything(self,**kwargs):
        return self.n.get_everything(**kwargs)
    
    def get_sources(self,**kwargs):
        return self.n.get_sources(**kwargs)