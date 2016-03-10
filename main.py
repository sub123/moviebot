import mysql_interact,cache

def intodb(path):
    movie_list=cache.cache()
    movie_list.getfiles(path)
    movie_list.store()

def fromdb():
    pass

path=raw_input("Enter path to directory:")
intodb(path)
