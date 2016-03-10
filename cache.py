import os,urllib2,sys,json
import MySQLdb as mysql
movies={}
class cache:
    def getfiles(self,path):
        global movies
        for root,directories,filenames in os.walk(path):
            for directory in directories:
                self.getfiles(os.path.join(root,directory))
            for filename in filenames:
                if ".mp4" in filename or ".mkv" in filename:
                    movies[filename]=os.path.join(root,filename)

    def fetch(self,movie):
        tmp="+"
        movie=tmp.join(movie.split(" "))
        url="http://www.omdbapi.com/?t="+movie+"&y=&plot=short&r=json"
        #print url
        content=urllib2.urlopen(url)
        return content.read()

    def store(self):
        global movies
        try:
            db=mysql.connect(host="localhost",user="root",passwd="icui4cu",db="movies")
            cur=db.cursor()
        except:
           print "error in db connection"
           sys.exit(1)
        for mov in list(movies):
            movie=mov.split("[bootstrap]")[0]
            tmp=" "
            movie=tmp.join(movie.split("."))
            movie_data=self.fetch(movie)
            movie_data=json.loads(movie_data)
            try:
                cur.execute("insert into movies_list (Title,Genre,IMDB,Runtime,Year,path) values('%s','%s','%s','%s','%s','%s')"%(movie_data['Title'],movie_data['Genre'],movie_data['imdbRating'],movie_data['Runtime'],movie_data['Year'],movies[mov]))
                db.commit()
            except:
                print "could not cache "+movie
#movies_list=cache()
#movies_list.getfiles('/home/bootstrap/DC/Movies')
#movies_list.store()
#movies_list.fetch("imitation game")
#movies_list.getfiles('/home/bootstrap/DC/Movies')
#print movies
