#import mysql.connector as sql

class DevelopmentConfig():
    DEBUG=True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '12345678'
    MYSQL_DB = 'dna_meli'

config = {
    'development' : DevelopmentConfig
}

