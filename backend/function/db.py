import sqlite3, string, random, os


#DO WITH POOL CONNECTION

#Create a simple table in db
def createSimpleTable():

    if not os.path.exists("./database.db"):
        open("./database.db", "w")
        con=sqlite3.connect("./database.db")

        cursor= con.cursor()

        table= "Create table URLS(id, link, shortURL);"

        cursor.execute(table)

        con.commit()
        con.close()

        print("Database is created")

#Save an id, a link and the characters of the shortURL
def saveURL(id,url):
    if len(checkDB(url))>0:
        return

    con=sqlite3.connect("./database.db")

    cursor= con.cursor()

    query= "insert into URLS values(?,?,?);"

    shortURL=generateShortURL()

    cursor.execute(query,(id,url,shortURL))

    con.commit()
    con.close()
    
##If it uses shortURL --> isShort is true, in other case False,
#  and depending on the case, a different data is obtained from db
def readDB(url,isShort):
    con=sqlite3.connect("./database.db")

    cursor= con.cursor()

    if isShort== True:
        query='Select shortURL from URLS where link=?;'

        res= cursor.execute(query,(url,))
        data= res.fetchall()[0][0]
    else:
        query='Select link from URLS where shortURL=?;'
        res= cursor.execute(query,(url,))
        data= res.fetchall()

    con.close()

    return data

#Create randoms letters for the ShortURL
def generateShortURL():
    letters= string.ascii_letters

    shortURL= ''.join(random.choice(letters) for i in range(10))

    return shortURL

#Check if the link is already in th db
def checkDB(url):
    con=sqlite3.connect("./database.db")

    cursor= con.cursor()

    query='Select link from URLS where link=?'

    res=cursor.execute(query,(url,))
    data=res.fetchall()

    con.close()

    return data
 
   

    
