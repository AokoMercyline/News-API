import os
class Config:
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig
}













# class Config:
#     API_KEY = ''
    
# class DevConfig(Config):
#     pass

# class ProdCOnfig(Config):
#     pass