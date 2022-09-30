import mysql.connector


class Database:

    config = ("localhost", "root", '', 'botdiscord')

    def __init__(self):
        self.db = self.connect(*self.config)


    def connect(self, host, user, passw, database):
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=passw,
            database=database
        )
        if mydb:
            return mydb
        else:
            print("Erro ao conectar ao banco de dadods: Tente novamente!")


    def consult(self, opt):
        query = f"SELECT * FROM {opt}"
        cn = self.db
        cur = cn.cursor()
        cur.execute(query)
        return cur.fetchall()

    def selectCommand(self,consult, opt):
        for i in consult:
            if i[1] == opt:
                return i[2]

    def CreateUser(self, *args):
        query = f"INSERT INTO user(name,id,points) VALUE ({args[0]},{args[1]}, 0)"
        cn = self.db
        cur = cn.cursor()
        cur.execute(query)
        print("Usuário adicionado ao banco de dados!")

    def AttPoints(self, point, player):
        query = f"UPDATE user SET points={point} WHERE name={player}"
        cn = self.db
        cur = cn.cursor()
        cur.execute(query)
        print("Pontuação atualizada!")


# command = '$hello'
#
# query = f'SELECT * FROM commands'
#
# db = Database()
#
# consult = db.consult(query)
#
# teste = db.selectCommand(consult,command)
#
# print(teste)






