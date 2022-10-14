from peewee import MySQLDatabase

def DataBase(name, user, password, host, port):
    DB = MySQLDatabase(name, user=user, password=password, host=host, port=port)
    return DB

