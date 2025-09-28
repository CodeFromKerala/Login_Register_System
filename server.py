from flask import Flask, render_template, redirect, request
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(user="root", password="241007", host="localhost", database="LoginSystem")

if conn.is_connected() == False:
	quit()

cur = conn.cursor()

@app.route('/')
def home_page():
	return render_template('./home_page.html')

@app.route('/login')
def login():
	return render_template('./login.html')

@app.route('/landing', methods=['POST'])
def landing():
	username = request.form['username']
	if username != "":
		password = request.form['password']
		cur.execute(f'select password from Users where username="{username}"')
		data = cur.fetchall()
		for i in data:
			print(i)
		if data[0][0] == password:
			return render_template("./landing.html", username=username)
	return redirect('/')

# Add Functionality To Landing Page -> Example : A note storing page

@app.route('/registered', methods=['POST'])
def registered():
	username = request.form['username']
	password = request.form['password']
	email = request.form['email']
	cur.execute(f"insert into Users(username, password, email) values('{username}', '{password}', '{email}')")
	conn.commit()
	return render_template("./registered.html", username=username)

@app.route('/register')
def register():
	return render_template("./register.html")

@app.route('/achutty')
def achutty():
	return render_template("./achutty.html")


app.run('0.0.0.0', 5000, debug=True)
