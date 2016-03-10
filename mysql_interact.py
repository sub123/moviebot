import subprocess
import MySQLdb as mysql
class mysql_interface:
    def fetch(self,flag):
        db=mysql.connect(host="localhost",user="root",passwd="icui4cu",db="movies")
        cur=db.cursor()
        if flag=="-i":
            query="select Title,IMDB from movies_list order by IMDB desc;"
        elif flag=="-r":
            query="select Title,Runtime from movies_list order by Runtime desc;"
        elif flag=="-ir" or flag=="-ri":
            query="select Title,IMDB,Runtime from movies_list order by IMDB desc;"
        try:
            cur.execute(query)
            output=cur.fetchall()
            db.close()
            return output
            '''for row in output:
                if flag=="-i":
                    print "Title: %s IMDB: %s" %(row[0],row[1])
                if flag=="-r":
                    print "Title: %s Runtime: %s" %(row[0],row[1])
                if flag=="-ir" or flag=="-ri":
                    print "Title: %s IMDB: %s Runtime:%s" %(row[0],row[1],row[2])'''
        except:
            db.close()
            print("could not fetch from db")
    def search(self,movie):
        db=mysql.connect(host="localhost",user="root",passwd="icui4cu",db="movies")
        cur=db.cursor()
        movie="%"+movie+"%"
        query="select * from movies_list where Title like '%s';" %(movie)
        cur.execute(query)
        output=cur.fetchall()
        db.close()
        return output
    def play(self,movie):
        output=self.search(movie)
        if len(output)>1:
            print "Found following movies:"
            i=1
            for row in output:
                print (str)(i)+"  Title:%s" %(row[0])
                i=i+1
            serial=input('Enter Serial Number to play:')
            subprocess.call(["vlc",output[serial-1][5]])
        elif len(output)==0:
            print "movie not found in cache"
        else:
            subprocess.call(["vlc",output[0][5]])
result=mysql_interface()
result.fetch("-ir")
#result.search("potter")
#result.play("harry")
