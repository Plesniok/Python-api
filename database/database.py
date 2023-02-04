import psycopg2

DATABASE_HOST='localhost';
DATABASE_USER='postgres';
DATABASE_PASSWORD='passwd123';
DATABASE_NAME='test_database';

class DatabaseConnection:
    def __init__(self, DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME):
        self.conn = psycopg2.connect(
            dbname=DATABASE_NAME,
            user=DATABASE_USER,
            host=DATABASE_HOST,
            password=DATABASE_PASSWORD
        )

    def runMigrations(self):
        cur = self.conn.cursor()
        cur.execute("CREATE SEQUENCE your_seq;CREATE TABLE public.users(id int default nextval('your_seq'::regclass),name character varying(255) NOT NULL,last_ame character varying(255) NOT NULL,phone integer,car character varying(255),PRIMARY KEY (id));ALTER TABLE IF EXISTS public.users OWNER to postgres;")
        res = cur.fetchone()[0]
        cur.close()
        return res

    def getAllUsers(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM public.users")
        res = cur.fetchall()
        cur.close()
        dictRes = []
        # for i in res:
        #     dictRes
        return res
    
    def getByName(self, reqData):
        cur = self.conn.cursor()
        print(reqData)
        cur.execute("SELECT * FROM public.users WHERE name = %s AND last_name = %s;", (reqData["name"], reqData["last_name"]))
        res = cur.fetchall()
        cur.close()
        dictRes = []
        for i in res:
            print(i)
        return res

    def addUser(self, reqData):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM public.users WHERE name = %s AND last_name = %s;", (reqData["name"], reqData["last_name"]))
            if_user_exist = cur.fetchall()
            print(if_user_exist)
            if(len(if_user_exist) > 0):
                return {"errorMessage": "User already exists"}
            cur.execute("INSERT INTO public.users(name, last_name, phone, car)VALUES (%s, %s, %s, %s);", (reqData["name"], reqData["last_name"], reqData["phone"], reqData["car"]))

            self.conn.commit()
            print("cur.fetchall()")
            cur.close()
            return True
        except:
            print("err`12321321")
            return {"errorMessage": "Database error"}
    
    def addRelation(self, reqData):
        # try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM public.relations WHERE name = %s AND last_name = %s AND friend_name = %s AND friend_last_name = %s;", (reqData["name"], reqData["last_name"], reqData["friend_name"], reqData["friend_last_name"]))
            ifRelationExist = cur.fetchall()
            print(ifRelationExist)
            if(len(ifRelationExist) > 0):
                return {"errorMessage": "Relation already exists"}
            cur.execute("INSERT INTO public.relations(name, last_name, friend_name, friend_last_name)VALUES (%s, %s, %s, %s);", (reqData["name"], reqData["last_name"], reqData["friend_name"], reqData["friend_last_name"]))

            self.conn.commit()
            cur.close()
            return True
        # except:
        #     print("err`12321321")
        #     return {"errorMessage": "Database error"}
    def getRelationsByName(self, reqData):
        cur = self.conn.cursor()
        print(reqData)
        cur.execute("SELECT  friend_name,friend_last_name FROM public.relations WHERE name = %s AND last_name = %s;", (reqData["name"], reqData["last_name"]))
        res = cur.fetchall()
        cur.close()
        dictRes = []
        return res
