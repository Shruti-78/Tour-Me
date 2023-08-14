from flask import Flask, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL
import mysql.connector
import os

mydb = mysql.connector.connect(host='localhost', username='root', password='Mysql@123', database='tip_trip')
cursor = mydb.cursor()
app = Flask(__name__)

picFolder = os.path.join('static', 'buitin')
app.config['UPLOAD_FOLDER'] = picFolder


@app.route('/')
def index():
    image_url = "/static/buitin/wall.png"
    # return redirect(url_for('location'))
    return render_template('index.html', image_url=image_url)


@app.route('/button_click')
def button_click():
    return redirect(url_for('accept'))


@app.route('/logout')
def logout():
    return redirect(url_for('home'))


@app.route('/display')
def display():
    cursor.execute("select* from customer")
    value = cursor.fetchall()  # cursor.close()
    return render_template('display.html', result=value)


@app.route('/accept', methods=['GET', 'POST'])
def accept():
    try:
        cursor2 = mydb.cursor()
        if request.method == "POST":
            query = "SELECT MAX(Cust_ID) FROM customer"
            cursor2.execute(query)
            # Fetch the result and store it in a Python variable
            result = cursor2.fetchone()[0]
            result = result + 1
            accept = request.form
            name = accept['Name']
            email = accept['mail']
            phone = accept['phno']
            aadhr = accept['aadhar']
            cursor2.execute("Insert into customer values (%s,%s,%s,%s,%s)", (result, name, email, phone, aadhr))
            mydb.commit()
            return render_template('show_id.html', result=result)
    except mysql.connector.errors.DatabaseError:
        return render_template('error_empty.html')

    return render_template('accept.html')


# @app.route('/show_id')
# def show_id():
#     return render_template('show_id.html')


@app.route('/location')
def location():
    return render_template('location.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        custid = request.form.get('custid')
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM customer WHERE Cust_ID = %s", (custid,))
        result = cursor.fetchone()
        cursor.close()

        if result is None:
            return render_template('no_cust.html')

        else:
            return render_template('location.html')

    return render_template('login.html')


@app.route('/kashmir')
def kashmir():
    q = ("select * from package where Places = 'Kashmir'")
    cursor.execute(q)
    resval = cursor.fetchall()
    return render_template('kashmir.html', result=resval)


@app.route('/view_kashmir')
def view_kashmir():
    q1 = ("select Sites from places where Place_name = 'Kashmir'")
    cursor.execute(q1)
    resval1 = cursor.fetchall()
    return render_template('view_kashmir.html', result=resval1)


@app.route('/goa')
def goa():
    q2 = ("select * from package where Places = 'Goa'")
    cursor.execute(q2)
    resval2 = cursor.fetchall()
    return render_template('goa.html', result=resval2)


@app.route('/view_goa')
def view_goa():
    q3 = ("select Sites from places where Place_name = 'GOA'")
    cursor.execute(q3)
    resval3 = cursor.fetchall()
    return render_template('view_goa.html', result=resval3)


@app.route('/rajasthan')
def rajasthan():
    q4 = ("select * from package where Places = 'Rajasthan'")
    cursor.execute(q4)
    resval4 = cursor.fetchall()
    return render_template('rajasthan.html', result=resval4)


@app.route('/view_rajasthan')
def view_rajasthan():
    q5 = ("select Sites from places where Place_name = 'Rajasthan'")
    cursor.execute(q5)
    resval5 = cursor.fetchall()
    return render_template('view_rajasthan.html', result=resval5)


@app.route('/andaman')
def andaman():
    q6 = ("select * from package where Places = 'Andaman & Nicobar'")
    cursor.execute(q6)
    resval6 = cursor.fetchall()
    return render_template('andaman.html', result=resval6)


@app.route('/view_andaman')
def view_andaman():
    q7 = ("select Sites from places where Place_name = 'Andaman & Nicobar'")
    cursor.execute(q7)
    resval7 = cursor.fetchall()
    return render_template('view_andaman.html', result=resval7)


@app.route('/uttarakhand')
def uttarakhand():
    q8 = ("select * from package where Places = 'Uttarakhand'")
    cursor.execute(q8)
    resval8 = cursor.fetchall()
    return render_template('uttarakhand.html', result=resval8)


@app.route('/view_uttarakhand')
def view_uttarakhand():
    q9 = ("select Sites from places where Place_name = 'Uttarakhand'")
    cursor.execute(q9)
    resval9 = cursor.fetchall()
    return render_template('view_uttarakhand.html', result=resval9)


@app.route('/manali')
def manali():
    q10 = ("select * from package where Places = 'Manali'")
    cursor.execute(q10)
    resval10 = cursor.fetchall()
    return render_template('manali.html', result=resval10)


@app.route('/view_manali')
def view_manali():
    q11 = ("select Sites from places where Place_name = 'Manali'")
    cursor.execute(q11)
    resval11 = cursor.fetchall()
    return render_template('view_manali.html', result=resval11)


@app.route('/karnataka')
def karnataka():
    q12 = ("select * from package where Places = 'Karnataka'")
    cursor.execute(q12)
    resval12 = cursor.fetchall()
    return render_template('karnataka.html', result=resval12)


@app.route('/view_karnataka')
def view_karnataka():
    q13 = ("select Sites from places where Place_name = 'Karnataka'")
    cursor.execute(q13)
    resval13 = cursor.fetchall()
    return render_template('view_karnataka.html', result=resval13)


@app.route('/bengal')
def bengal():
    q14 = ("select * from package where Places = 'West Bengal'")
    cursor.execute(q14)
    resval14 = cursor.fetchall()
    return render_template('bengal.html', result=resval14)


@app.route('/view_bengal')
def view_bengal():
    q15 = ("select Sites from places where Place_name = 'West Bengal'")
    cursor.execute(q15)
    resval15 = cursor.fetchall()
    return render_template('view_bengal.html', result=resval15)


@app.route('/tamil')
def tamil():
    q16 = ("select * from package where Places = 'Tamil Nadu'")
    cursor.execute(q16)
    resval16 = cursor.fetchall()
    return render_template('tamil.html', result=resval16)


@app.route('/view_tamil')
def view_tamil():
    q17 = "select Sites from places where Place_name = 'Tamil Nadu'"
    cursor.execute(q17)
    resval17 = cursor.fetchall()
    return render_template('view_tamil.html', result=resval17)


@app.route('/ooty')
def ooty():
    q18 = "select * from package where Places = 'Ooty'"
    cursor.execute(q18)
    resval18 = cursor.fetchall()
    return render_template('ooty.html', result=resval18)


@app.route('/view_ooty')
def view_ooty():
    q19 = "select Sites from places where Place_name = 'Ooty'"
    cursor.execute(q19)
    resval19 = cursor.fetchall()
    return render_template('view_ooty.html', result=resval19)


@app.route('/ashta')
def ashta():
   q20 = ("select * from package where Places = 'Ashtavinayak'")
   cursor.execute(q20)
   resval20 = cursor.fetchall()
   return render_template('ashta.html',result = resval20)


@app.route('/view_ashta')
def view_ashta():
   q21 = ("select Sites from places where Place_name = 'Ashtavinayak'")
   cursor.execute(q21)
   resval21 = cursor.fetchall()
   return render_template('view_ashta.html',result = resval21)


@app.route('/haridwar')
def haridwar():
   q22 = ("select * from package where Places = 'Haridwar'")
   cursor.execute(q22)
   resval22 = cursor.fetchall()
   return render_template('haridwar.html',result = resval22)


@app.route('/view_haridwar')
def view_haridwar():
   q23 = ("select Sites from places where Place_name = 'Haridwar'")
   cursor.execute(q23)
   resval23 = cursor.fetchall()
   return render_template('view_haridwar.html',result = resval23)


@app.route('/dham')
def dham():
   q24 = ("select * from package where Places = '4 dham'")
   cursor.execute(q24)
   resval24 = cursor.fetchall()
   return render_template('dham.html',result = resval24)


@app.route('/view_dham')
def view_dham():
   q25 = ("select Sites from places where Place_name = '4 dham'")
   cursor.execute(q25)
   resval25 = cursor.fetchall()
   return render_template('view_dham.html',result = resval25)


@app.route('/delhi')
def delhi():
   q26 = ("select * from package where Places = 'delhi'")
   cursor.execute(q26)
   resval26 = cursor.fetchall()
   return render_template('delhi.html',result = resval26)


@app.route('/view_delhi')
def view_delhi():
   q27 = ("select Sites from places where Place_name = 'delhi'")
   cursor.execute(q27)
   resval27 = cursor.fetchall()
   return render_template('view_delhi.html',result = resval27)


@app.route('/kerela')
def kerela():
   q28 = ("select * from package where Places = 'kerela'")
   cursor.execute(q28)
   resval28 = cursor.fetchall()
   return render_template('kerela.html',result = resval28)


@app.route('/view_kerela')
def view_kerela():
   q29 = ("select Sites from places where Place_name = 'kerela'")
   cursor.execute(q29)
   resval29 = cursor.fetchall()
   return render_template('view_kerela.html',result = resval29)


@app.route('/ladakh')
def ladakh():
   q30 = ("select * from package where Places = 'ladakh'")
   cursor.execute(q30)
   resval30 = cursor.fetchall()
   return render_template('ladakh.html',result = resval30)


@app.route('/view_ladakh')
def view_ladakh():
   q31 = ("select Sites from places where Place_name = 'ladakh'")
   cursor.execute(q31)
   resval31 = cursor.fetchall()
   return render_template('view_ladakh.html',result = resval31)


@app.route('/laksha')
def laksha():
   q32 = ("select * from package where Places = 'delhi'")
   cursor.execute(q32)
   resval32 = cursor.fetchall()
   return render_template('laksha.html',result = resval32)


@app.route('/view_laksha')
def view_laksha():
   q33 = ("select Sites from places where Place_name = 'delhi'")
   cursor.execute(q33)
   resval33 = cursor.fetchall()
   return render_template('view_laksha.html',result = resval33)


@app.route('/book_now', methods=['GET', 'POST'])
def book_now():
    cursor3 = mydb.cursor()
    try:
        if request.method == "POST":
            query = "SELECT MAX(Trip_ID) FROM my_trip"
            cursor3.execute(query)
            result1 = cursor3.fetchone()[0]
            result1 = result1 + 1
            accept = request.form
            p_id = accept['package_id']
            date_of_trip = accept['date']
            p_type = accept['pay_type']
            customer = accept['cust_id']
            cursor3.execute("Insert into my_trip values (%s,%s,%s,%s,%s)", (result1, date_of_trip, p_type, p_id, customer))
            mydb.commit()
            if result1 is None:
                return render_template('book_no.html')
            return redirect(url_for('trip_packed'))

    except mysql.connector.errors.IntegrityError:
        return render_template('book_no.html')
    except :
        if result1 is None:
            return render_template('book_no.html')

    return render_template('book_now.html')


@app.route('/trip_packed')
def trip_packed():
    try:
       cursor4 = mydb.cursor()
       cursor4.execute("SELECT MAX(Trip_ID) FROM my_trip")
       result2 = cursor4.fetchone()[0]
       cursor5 = mydb.cursor()
       cursor5.execute("SELECT Cid FROM my_trip WHERE Trip_ID = %s",(result2,))
       result3 = cursor5.fetchone()[0]
       cursor4.execute("select customer.Name , customer.Phno , package.PID , package.No_members , package.Ptype , places.Place_name , places.Sites , places.Duration , my_trip.DOTrip , my_trip.Pay_type , package.cost , trip_coordinator.C_Name , trip_coordinator.Phone_no from customer INNER JOIN my_trip ON customer.Cust_ID = my_trip.Cid INNER JOIN package ON package.PID = my_trip.Pid INNER JOIN places ON places.Place_name = package.Places INNER JOIN trip_coordinator where places.Trip_CID = trip_coordinator.TCID AND Cust_ID = %s",(result3,))
       resultval = cursor4.fetchone()
       print(resultval)
       return render_template('trip_packed.html',result = resultval)
    except mysql.connector.errors.IntegrityError:
        return render_template('book_no.html')
    return render_template('trip_packed.html', result=resultval)



@app.route('/home')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
