from flask import Flask ,render_template, request
import sqlite3 as sql

app=Flask(__name__)

# Showing Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Showing Add Product Page
@app.route('/Product_Add')
def Product_Add():
    return render_template('productadd.html')

# Insert Product in Database
@app.route('/Insert_Product',methods=['POST','GET'])
def Insert_Product():
	if request.method == 'POST':
		try:
			p_name=request.form['p_name']
			p_brand=request.form['p_brand']
			r_price=request.form['r_price']
			o_price=request.form['o_price']
			p_currency=request.form['p_currency']
			cl1=request.form['cl1']
			cl2=request.form['cl2']
			cl3=request.form['cl3']
			cl4=request.form['cl4']
			p_image=request.form['p_image']

			with sql.connect('GDDatabase.db') as con:
				cur =con.cursor()
				cur.execute("INSERT INTO Greendeck (Name,Brand_Name,Regular_Price,Offer_Price,Currency,CL1,CL2,CL3,CL4,Image_Url) VALUES (?,?,?,?,?,?,?,?,?,?)",(p_name,p_brand,r_price,o_price,p_currency,cl1,cl2,cl3,cl4,p_image))
				msg='Product Has Been Successfully Added'
		except:
			con.rollback()
			msg='Product Has Not Added Due To Some Error'

		finally:
		    return render_template("productmessage.html",msg=msg)
		    con.close()

# Showing Product Update Page

@app.route('/Product_Update')
def Product_Update():
	con = sql.connect('GDDatabase.db')
	con.row_factory = sql.Row
	cur = con.cursor()
	cur.execute('select * from Greendeck')
	rows = cur.fetchall()
	return render_template('productupdate.html',rows=rows)

# Edit Product Page

@app.route('/Product_Update1/<int:product_id>')
def Product_Update1(product_id):
	con = sql.connect('GDDatabase.db')
	con.row_factory = sql.Row
	cur = con.cursor()
	cur.execute('select * from Greendeck where P_ID = ?',(product_id,))
	rows = cur.fetchall()
	return render_template('productedit.html',rows = rows)

# Inserting Updated Data in Database

@app.route('/Product_Update2/<int:product_id>',methods=['POST','GET'])
def Product_Update2(product_id):
	if request.method == 'POST':
		try:
			p_name=request.form['p_name']
			p_brand=request.form['p_brand']
			r_price=request.form['r_price']
			o_price=request.form['o_price']
			p_currency=request.form['p_currency']
			cl1=request.form['cl1']
			cl2=request.form['cl2']
			cl3=request.form['cl3']
			cl4=request.form['cl4']
			p_image=request.form['p_image']

			with sql.connect('GDDatabase.db') as con:
				cur =con.cursor()
				cur.execute("UPDATE Greendeck SET Name=?,Brand_Name=?,Regular_Price=?,Offer_Price=?,Currency=?,CL1=?,CL2=?,CL3=?,CL4=?,Image_Url=? WHERE P_ID=?",(p_name,p_brand,r_price,o_price,p_currency,cl1,cl2,cl3,cl4,p_image,product_id))
				msg='Product Has Been Successfully Updated'
		except:
			con.rollback()
			msg='Product Has Not Updated Due To Some Error'

		finally:
		    return render_template("productmessage.html",msg=msg)
		    con.close()

# Delete Product Page

@app.route('/Delete_Show')
def Delete_Show():
	con = sql.connect('GDDatabase.db')
	con.row_factory = sql.Row
	cur = con.cursor()
	cur.execute('select * from Greendeck')
	rows = cur.fetchall()
	return render_template('productdelete.html',rows = rows)

# Product Delete Page 

@app.route('/Product_Delete/<int:product_id>',methods=['POST','GET'])
def Product_Delete(product_id):
	try:
		with sql.connect('GDDatabase.db') as con:
			cur =con.cursor()
			cur.execute("DELETE FROM Greendeck WHERE P_Id=?",(product_id,))
			msg='Product Has Been Successfully Delete'
	except:
		con.rollback()
		msg='Product Has Not Deleted Due To Some Error'

	finally:
		return render_template("productmessage.html",msg=msg)
		con.close()


# Showing Product Details

@app.route('/Product_List')
def Product_List():
	con = sql.connect('GDDatabase.db')
	con.row_factory = sql.Row
	cur = con.cursor()
	cur.execute('select * from Greendeck')
	rows = cur.fetchall()
	return render_template('productdetails.html',rows = rows)

#add student record in database

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/adddata',methods=['POST'])
def adddata():
	if request.method == 'POST':
		try:
			file1 = request.files['CJfile']
			rows = csv.reader(file1)
			print(rows)
			msg='Successfully File Data Added to Database'
			with sql.connect('database.db') as con:
				cur =con.cursor()
				cur.executemany("INSERT INTO students VALUES (?,?,?,?)",rows)
				
		except:
			con.rollback()
			msg='File Data Not Added to Database'

		finally:
		    return render_template("result.html",msg=msg)
		    con.close()

if __name__ == '__main__':
 	app.run(debug=True,host="0.0.0.0", port=8000)
 	