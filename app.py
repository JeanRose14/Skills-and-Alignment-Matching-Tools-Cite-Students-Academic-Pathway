from flask import Flask
from flask_mysqldb import MySQL
from controllers.controllers import app_routes

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root' 
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask_db'

mysql = MySQL(app)

app_routes(app, mysql)

if __name__ == '__main__':
    app.run(debug=True)