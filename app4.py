from flask import Flask, render_template, request

import sqlite3 as sql

from peewee import *

DATABASE = SqliteDatabase('plane1.sqlite')

app = Flask(__name__)


@app.route('/')
def homepage():
	return render_template('homepage.html')

@app.route('/a')
def a():
	return render_template('Canada.html', methods=['POST', 'GET'])

@app.route('/addrec',methods=['POST', 'GET'])
def addrec():
	if request.method=='POST':
		try:
			dest=request.form['dest']
			d1=request.form['d1']
			m1=request.form['m1']
			d2=request.form['d2']
			m2=request.form['m2']
			time=request.form['time']
			trip=request.form['trip']
			ct=request.form['ct']
			at=request.form['at']
			clas=request.form['clas']
			sex=request.form['sex']
			age=request.form['age']
			name=request.form['name']
			sur=request.form['sur']
			phone=request.form['phone']
			phone2=request.form['phone2']
			pnum=request.form['pnum']
			email=request.form['email']
			address=request.form['address']
			od=request.form['od']
			with sql.connect("plane1.sqlite") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO planes (dest,d1,m1,d2,m2,time,trip,ct,at,clas,sex,age,name,sur,phone,phone2,pnum,email,address,od) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(dest,d1,m1,d2,m2,time,trip,ct,at,clas,sex,age,name,sur,phone,phone2,pnum,email,address,od) )
				con.commit()
				msg= "Your tickets have been successfully reserved for booking. U will be notified in 10 minutes of your invoice number and availability of sits. Payment can be done only after recieving invoice number via phone sms and email(with a duration of 30mins to pay). Please use the merchant code (31644) for paying your tickets and complete the booking process. Enter the confirmation cord the textbox provided and your tickets will be mailed to you in a period of 5 mins. You can also use your passport and invoice number for check in.  "
		except:
				con.rollback()
				msg= "error in insert operation"
		finally:
				return render_template("result.html",msg=msg)
				con.close()

@app.route('/b')
def b():
	return render_template('England.html', methods=['POST', 'GET'])

@app.route('/addrec2',methods=['POST', 'GET'])
def addrec2():
	if request.method=='POST':
		try:
			dest=request.form['dest']
			d1=request.form['d1']
			m1=request.form['m1']
			d2=request.form['d2']
			m2=request.form['m2']
			time=request.form['time']
			trip=request.form['trip']
			ct=request.form['ct']
			at=request.form['at']
			clas=request.form['clas']
			sex=request.form['sex']
			age=request.form['age']
			name=request.form['name']
			sur=request.form['sur']
			phone=request.form['phone']
			phone2=request.form['phone2']
			pnum=request.form['pnum']
			email=request.form['email']
			address=request.form['address']
			od=request.form['od']
			with sql.connect("plane1.sqlite") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO planes (dest,d1,m1,d2,m2,time,trip,ct,at,clas,sex,age,name,sur,phone,phone2,pnum,email,address,od) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(dest,d1,m1,d2,m2,time,trip,ct,at,clas,sex,age,name,sur,phone,phone2,pnum,email,address,od) )
				con.commit()
				msg= "Your tickets have been successfully reserved for booking. U will be notified in 10 minutes of your invoice number and availability of sits. Payment can be done only after recieving invoice number via phone sms and email(with a duration of 30mins to pay). Please use the merchant code (31644) for paying your tickets and complete the booking process. Enter the confirmation cord the textbox provided and your tickets will be mailed to you in a period of 5 mins. You can also use your passport and invoice number for check in.  "
		except:
				con.rollback()
				msg= "error in insert operation"
		finally:
				return render_template("result.html",msg=msg)
				con.close()

@app.route('/c')
def c():
	return render_template('South.html', methods=['POST', 'GET'])

@app.route('/addrec3',methods=['POST', 'GET'])
def addrec3():
	if request.method=='POST':
		try:
			dest=request.form['dest']
			d1=request.form['d1']
			m1=request.form['m1']
			d2=request.form['d2']
			m2=request.form['m2']
			time=request.form['time']
			trip=request.form['trip']
			ct=request.form['ct']
			at=request.form['at']
			clas=request.form['clas']
			sex=request.form['sex']
			age=request.form['age']
			name=request.form['name']
			sur=request.form['sur']
			phone=request.form['phone']
			phone2=request.form['phone2']
			pnum=request.form['pnum']
			email=request.form['email']
			address=request.form['address']
			od=request.form['od']
			with sql.connect("plane1.sqlite") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO planes (dest,d1,m1,d2,m2,time,trip,ct,at,clas,sex,age,name,sur,phone,phone2,pnum,email,address,od) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(dest,d1,m1,d2,m2,time,trip,ct,at,clas,sex,age,name,sur,phone,phone2,pnum,email,address,od) )
				con.commit()
				msg= "Your tickets have been successfully reserved for booking. U will be notified in 10 minutes of your invoice number and availability of sits. Payment can be done only after recieving invoice number via phone sms and email(with a duration of 30mins to pay). Please use the merchant code (31644) for paying your tickets and complete the booking process. Enter the confirmation cord the textbox provided and your tickets will be mailed to you in a period of 5 mins. You can also use your passport and invoice number for check in.  "
		except:
				con.rollback()
				msg= "error in insert operation"
		finally:
				return render_template("result.html",msg=msg)
				con.close()

@app.route('/d')
def d():
	return render_template('Bulawayo.html', methods=['POST', 'GET'])

@app.route('/addrec4',methods=['POST', 'GET'])
def addrec4():
	if request.method=='POST':
		try:
			dest=request.form['dest']
			d1=request.form['d1']
			m1=request.form['m1']
			d2=request.form['d2']
			m2=request.form['m2']
			time=request.form['time']
			trip=request.form['trip']
			ct=request.form['ct']
			at=request.form['at']
			clas=request.form['clas']
			sex=request.form['sex']
			age=request.form['age']
			name=request.form['name']
			sur=request.form['sur']
			phone=request.form['phone']
			phone2=request.form['phone2']
			pnum=request.form['pnum']
			email=request.form['email']
			address=request.form['address']
			od=request.form['od']
			with sql.connect("plane1.sqlite") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO planes (dest,d1,m1,d2,m2,time,trip,ct,at,clas,sex,age,name,sur,phone,phone2,pnum,email,address,od) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(dest,d1,m1,d2,m2,time,trip,ct,at,clas,sex,age,name,sur,phone,phone2,pnum,email,address,od) )
				con.commit()
				msg= "Your tickets have been successfully reserved for booking. U will be notified in 10 minutes of your invoice number and availability of sits. Payment can be done only after recieving invoice number via phone sms and email(with a duration of 30mins to pay). Please use the merchant code (31644) for paying your tickets and complete the booking process. Enter the confirmation cord the textbox provided and your tickets will be mailed to you in a period of 5 mins. You can also use your passport and invoice number for check in.  "
		except:
				con.rollback()
				msg= "error in insert operation"
		finally:
				return render_template("result.html",msg=msg)
				con.close()

@app.route('/e')
def e():
	return render_template('Vic.html', methods=['POST', 'GET'])

@app.route('/addrec5',methods=['POST', 'GET'])
def addrec5():
	if request.method=='POST':
		try:
			dest=request.form['dest']
			d1=request.form['d1']
			m1=request.form['m1']
			d2=request.form['d2']
			m2=request.form['m2']
			time=request.form['time']
			trip=request.form['trip']
			ct=request.form['ct']
			at=request.form['at']
			clas=request.form['clas']
			sex=request.form['sex']
			age=request.form['age']
			name=request.form['name']
			sur=request.form['sur']
			phone=request.form['phone']
			phone2=request.form['phone2']
			pnum=request.form['pnum']
			email=request.form['email']
			address=request.form['address']
			od=request.form['od']
			with sql.connect("plane1.sqlite") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO planes (dest,d1,m1,d2,m2,time,trip,ct,at,clas,sex,age,name,sur,phone,phone2,pnum,email,address,od) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(dest,d1,m1,d2,m2,time,trip,ct,at,clas,sex,age,name,sur,phone,phone2,pnum,email,address,od) )
				con.commit()
				msg= "Your tickets have been successfully reserved for booking. U will be notified in 10 minutes of your invoice number and availability of sits. Payment can be done only after recieving invoice number via phone sms and email(with a duration of 30mins to pay). Please use the merchant code (31644) for paying your tickets and complete the booking process. Enter the confirmation cord the textbox provided and your tickets will be mailed to you in a period of 5 mins. You can also use your passport and invoice number for check in.  "
		except:
				con.rollback()
				msg= "error in insert operation"
		finally:
				return render_template("result.html",msg=msg)
				con.close()

@app.route('/f')
def f():
	return render_template('Harare.html', methods=['POST', 'GET'])

@app.route('/addrec6',methods=['POST', 'GET'])
def addrec6():
	if request.method=='POST':
		try:
			dest=request.form['dest']
			d1=request.form['d1']
			m1=request.form['m1']
			d2=request.form['d2']
			m2=request.form['m2']
			time=request.form['time']
			trip=request.form['trip']
			ct=request.form['ct']
			at=request.form['at']
			clas=request.form['clas']
			sex=request.form['sex']
			age=request.form['age']
			name=request.form['name']
			sur=request.form['sur']
			phone=request.form['phone']
			phone2=request.form['phone2']
			pnum=request.form['pnum']
			email=request.form['email']
			address=request.form['address']
			od=request.form['od']
			with sql.connect("plane1.sqlite") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO planes (dest,d1,m1,d2,m2,time,trip,ct,at,clas,sex,age,name,sur,phone,phone2,pnum,email,address,od) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(dest,d1,m1,d2,m2,time,trip,ct,at,clas,sex,age,name,sur,phone,phone2,pnum,email,address,od) )
				con.commit()
				msg= "Your tickets have been successfully reserved for booking. U will be notified in 10 minutes of your invoice number and availability of sits. Payment can be done only after recieving invoice number via phone sms and email(with a duration of 30mins to pay). Please use the merchant code (31644) for paying your tickets and complete the booking process. Enter the confirmation cord the textbox provided and your tickets will be mailed to you in a period of 5 mins. You can also use your passport and invoice number for check in.  "
		except:
				con.rollback()
				msg= "error in insert operation"
		finally:
				return render_template("result.html",msg=msg)
				con.close()

@app.route('/g')
def g():
	return render_template('Dubai.html', methods=['POST', 'GET'])

@app.route('/addrec7',methods=['POST', 'GET'])
def addrec7():
	if request.method=='POST':
		try:
			dest=request.form['dest']
			d1=request.form['d1']
			m1=request.form['m1']
			d2=request.form['d2']
			m2=request.form['m2']
			time=request.form['time']
			trip=request.form['trip']
			ct=request.form['ct']
			at=request.form['at']
			clas=request.form['clas']
			sex=request.form['sex']
			age=request.form['age']
			name=request.form['name']
			sur=request.form['sur']
			phone=request.form['phone']
			phone2=request.form['phone2']
			pnum=request.form['pnum']
			email=request.form['email']
			address=request.form['address']
			od=request.form['od']
			with sql.connect("plane1.sqlite") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO planes (dest,d1,m1,d2,m2,time,trip,ct,at,clas,sex,age,name,sur,phone,phone2,pnum,email,address,od) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(dest,d1,m1,d2,m2,time,trip,ct,at,clas,sex,age,name,sur,phone,phone2,pnum,email,address,od) )
				con.commit()
				msg= "Your tickets have been successfully reserved for booking. U will be notified in 10 minutes of your invoice number and availability of sits. Payment can be done only after recieving invoice number via phone sms and email(with a duration of 30mins to pay). Please use the merchant code (31644) for paying your tickets and complete the booking process. Enter the confirmation cord the textbox provided and your tickets will be mailed to you in a period of 5 mins. You can also use your passport and invoice number for check in.  "
		except:
				con.rollback()
				msg= "error in insert operation"
		finally:
				return render_template("result.html",msg=msg)
				con.close()

@app.route('/h')
def h():
	return render_template('China.html', methods=['POST', 'GET'])

@app.route('/addrec8',methods=['POST', 'GET'])
def addrec8():
	if request.method=='POST':
		try:
			dest=request.form['dest']
			d1=request.form['d1']
			m1=request.form['m1']
			d2=request.form['d2']
			m2=request.form['m2']
			time=request.form['time']
			trip=request.form['trip']
			ct=request.form['ct']
			at=request.form['at']
			clas=request.form['clas']
			sex=request.form['sex']
			age=request.form['age']
			name=request.form['name']
			sur=request.form['sur']
			phone=request.form['phone']
			phone2=request.form['phone2']
			pnum=request.form['pnum']
			email=request.form['email']
			address=request.form['address']
			od=request.form['od']
			with sql.connect("plane1.sqlite") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO planes (dest,d1,m1,d2,m2,time,trip,ct,at,clas,sex,age,name,sur,phone,phone2,pnum,email,address,od) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(dest,d1,m1,d2,m2,time,trip,ct,at,clas,sex,age,name,sur,phone,phone2,pnum,email,address,od) )
				con.commit()
				msg= "Your tickets have been successfully reserved for booking. U will be notified in 10 minutes of your invoice number and availability of sits. Payment can be done only after recieving invoice number via phone sms and email(with a duration of 30mins to pay). Please use the merchant code (31644) for paying your tickets and complete the booking process. Enter the confirmation cord the textbox provided and your tickets will be mailed to you in a period of 5 mins. You can also use your passport and invoice number for check in.  "
		except:
				con.rollback()
				msg= "error in insert operation"
		finally:
				return render_template("result.html",msg=msg)
				con.close()

@app.route('/i')
def i():
	return render_template('France.html', methods=['POST', 'GET'])

@app.route('/addrec9',methods=['POST', 'GET'])
def addrec9():
	if request.method=='POST':
		try:
			dest=request.form['dest']
			d1=request.form['d1']
			m1=request.form['m1']
			d2=request.form['d2']
			m2=request.form['m2']
			time=request.form['time']
			trip=request.form['trip']
			ct=request.form['ct']
			at=request.form['at']
			clas=request.form['clas']
			sex=request.form['sex']
			age=request.form['age']
			name=request.form['name']
			sur=request.form['sur']
			phone=request.form['phone']
			phone2=request.form['phone2']
			pnum=request.form['pnum']
			email=request.form['email']
			address=request.form['address']
			od=request.form['od']
			with sql.connect("plane1.sqlite") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO planes (dest,d1,m1,d2,m2,time,trip,ct,at,clas,sex,age,name,sur,phone,phone2,pnum,email,address,od) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(dest,d1,m1,d2,m2,time,trip,ct,at,clas,sex,age,name,sur,phone,phone2,pnum,email,address,od) )
				con.commit()
				msg= "Your tickets have been successfully reserved for booking. U will be notified in 10 minutes of your invoice number and availability of sits. Payment can be done only after recieving invoice number via phone sms and email(with a duration of 30mins to pay). Please use the merchant code (31644) for paying your tickets and complete the booking process. Enter the confirmation cord the textbox provided and your tickets will be mailed to you in a period of 5 mins. You can also use your passport and invoice number for check in.  "
		except:
				con.rollback()
				msg= "error in insert operation"
		finally:
				return render_template("result.html",msg=msg)
				con.close()

@app.route('/j')
def j():
	return render_template('Germany.html', methods=['POST', 'GET'])

@app.route('/addrec10',methods=['POST', 'GET'])
def addrec10():
	if request.method=='POST':
		try:
			dest=request.form['dest']
			d1=request.form['d1']
			m1=request.form['m1']
			d2=request.form['d2']
			m2=request.form['m2']
			time=request.form['time']
			trip=request.form['trip']
			ct=request.form['ct']
			at=request.form['at']
			clas=request.form['clas']
			sex=request.form['sex']
			age=request.form['age']
			name=request.form['name']
			sur=request.form['sur']
			phone=request.form['phone']
			phone2=request.form['phone2']
			pnum=request.form['pnum']
			email=request.form['email']
			address=request.form['address']
			od=request.form['od']
			with sql.connect("plane1.sqlite") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO planes (dest,d1,m1,d2,m2,time,trip,ct,at,clas,sex,age,name,sur,phone,phone2,pnum,email,address,od) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(dest,d1,m1,d2,m2,time,trip,ct,at,clas,sex,age,name,sur,phone,phone2,pnum,email,address,od) )
				con.commit()
				msg= "Your tickets have been successfully reserved for booking. U will be notified in 10 minutes of your invoice number and availability of sits. Payment can be done only after recieving invoice number via phone sms and email(with a duration of 30mins to pay). Please use the merchant code (31644) for paying your tickets and complete the booking process. Enter the confirmation cord the textbox provided and your tickets will be mailed to you in a period of 5 mins. You can also use your passport and invoice number for check in.  "
		except:
				con.rollback()
				msg= "error in insert operation"
		finally:
				return render_template("result.html",msg=msg)
				con.close()


@app.route('/k')
def k():
	return render_template('result.html', methods=['POST', 'GET'])

@app.route('/addrec11',methods=['POST', 'GET'])
def addrec11():
	if request.method=='POST':
		try:
			PN=request.form['PN']
			CC=request.form['CC']
			with sql.connect("plane1.sqlite") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO planes5 (PN,CC) VALUES (?,?)",(PN,CC) )
				con.commit()
				msg= ""
		except:
				con.rollback()
				msg= "error in insert operation"
		finally:
				return render_template("result2.html",msg=msg)
				con.close()

@app.route('/z')
def z():
	return render_template('about.html')


@app.route('/l')
def l():
	return render_template('search.html')

app.run(debug=True, port=8070, host='127.0.0.1')