from flask import Flask,render_template,request
import mysql.connector
conn = mysql.connector.connect(host='localhost',user='root',password='',database='bbms')
mycursor=conn.cursor()
#create a flask application
app = Flask(__name__)

#Define the route

@app.route('/')
def hello():
    return render_template('first.html')
@app.route('/admin/')
def admin():
    return render_template('adminlogin.html')

@app.route('/admindashboard/',methods=['post'])
def admindashboard():
    USERNAME=request.form['USERNAME']
    PASSWORD=request.form['PASSWORD']
    query="SELECT * FROM login WHERE username = %s AND password = %s"
    values=USERNAME,PASSWORD
    mycursor.execute(query,values)
    login=mycursor.fetchall()
    if login:
        msg = 'Logged in successfully!'
        return render_template('admindashboard.html',msg = msg)
    else:
        msg = 'Incorrect Username or Password!'
    return render_template('adminlogin.html',msg=msg)
@app.route('/donor/')
def donor():
    return render_template('donorlogin.html')

@app.route('/donordashboard/',methods=['post'])
def donordashboard():
    USERNAME=request.form['USERNAME']
    PASSWORD=request.form['PASSWORD']
    query="SELECT * FROM donor_registration WHERE username = %s AND password = %s"
    values=USERNAME,PASSWORD
    mycursor.execute(query,values)
    donor_registration=mycursor.fetchall()
    if donor_registration:
        msg = 'Logged in successfully!'
        return render_template('donordashboard.html',msg = msg)
    else:
        msg = 'Incorrect Username or Password!'
    return render_template('donorlogin.html',msg=msg)
@app.route('/donorregister/')
def donorregister():
    return render_template('donorregistration.html')
@app.route('/read/',methods=['post'])
def read():
    fullname = request.form['fullname']
    USERNAME = request.form['USERNAME']
    fathername = request.form['fathername']
    mothername = request.form['mothername']
    DOB = request.form['DOB']
    GENDER = request.form['GENDER']
    AGE = request.form['AGE']
    bloodgroup = request.form['bloodgroup']
    ADDRESS = request.form['ADDRESS']
    CITY = request.form['CITY']
    lastdonatedate = request.form['lastdonatedate']
    EMAIL = request.form['EMAIL']
    mobileno = request.form['mobileno']
    PASSWORD = request.form['PASSWORD']
    confirmpassword = request.form['confirmpassword']
    query = "INSERT INTO donor_registration(full_name,username,father_name,mother_name,dob,gender,age,blood_group,address,city,last_donate_date,email,mobile_no,password,confirm_password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    data = (fullname,USERNAME,fathername,mothername,DOB,GENDER,AGE,bloodgroup,ADDRESS,CITY,lastdonatedate,EMAIL,mobileno,PASSWORD,confirmpassword)
    mycursor.execute(query,data)
    conn.commit()
    return render_template('donorregistration.html',msgdata='Registration Successful!')
@app.route('/patient/')
def patient():
    return render_template('patientlogin.html')
@app.route('/patientdashboard/',methods=['post'])
def patientdashboard():
    USERNAME=request.form['USERNAME']
    PASSWORD=request.form['PASSWORD']
    query="SELECT * FROM patient_registration WHERE username = %s AND password = %s"
    values=USERNAME,PASSWORD
    mycursor.execute(query,values)
    patient_registration=mycursor.fetchall()
    if patient_registration:
        msg = 'Logged in successfully!'
        return render_template('patientdashboard.html',msg = msg)
    else:
        msg = 'Incorrect Username or Password!'
    return render_template('patientlogin.html',msg=msg)
@app.route('/patientregister/')
def patientregister():
    return render_template('patientregistration.html')
@app.route('/add/',methods=['post'])
def add():
    fullname = request.form['fullname']
    USERNAME = request.form['USERNAME']
    fathername = request.form['fathername']
    mothername = request.form['mothername']
    DOB = request.form['DOB']
    GENDER = request.form['GENDER']
    AGE = request.form['AGE']
    bloodgroup = request.form['bloodgroup']
    DISEASE = request.form['DISEASE']
    ADDRESS = request.form['ADDRESS']
    CITY = request.form['CITY']
    EMAIL = request.form['EMAIL']
    mobileno = request.form['mobileno']
    PASSWORD = request.form['PASSWORD']
    confirmpassword = request.form['confirmpassword']
    query = "INSERT INTO patient_registration(full_name,username,father_name,mother_name,dob,gender,age,blood_group,disease,address,city,email,mobile_no,password,confirm_password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    data = (fullname,USERNAME,fathername,mothername,DOB,GENDER,AGE,bloodgroup,DISEASE,ADDRESS,CITY,EMAIL,mobileno,PASSWORD,confirmpassword)
    mycursor.execute(query,data)
    conn.commit()
    return render_template('patientregistration.html',msgdata='Registration Successful!')
@app.route('/donordetails/')
def donordetails():
    query="SELECT full_name,username,father_name,mother_name,dob,gender,age,blood_group,address,city,last_donate_date,email,mobile_no,password FROM donor_registration"
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('donordetails.html',sqldata=data)
@app.route('/patientdetails/')
def patientdetails():
    query="SELECT * FROM patient_registration"
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('patientdetails.html',sqldata=data)
@app.route('/donateblood/')
def donateblood():
    return render_template('donateblood.html')
@app.route('/donate/',methods=['post'])
def donate():
    bloodgroup = request.form['bloodgroup']
    UNIT = request.form['UNIT']
    DISEASE = request.form['DISEASE']
    AGE = request.form['AGE']
    DATE = request.form['DATE']
    query = "INSERT INTO donate_blood(blood_group,unit,disease,age,date) VALUES (%s,%s,%s,%s,%s)"
    data = (bloodgroup,UNIT,DISEASE,AGE,DATE)
    mycursor.execute(query,data)
    conn.commit()
    return render_template('donateblood.html',msgdata='Donation Successful!')
@app.route('/donationhistory/')
def donationhistory():
    query="SELECT * FROM donate_blood"
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('donationhistory.html',sqldata=data)
@app.route('/bloodrequest/')
def bloodrequest():
    return render_template('bloodrequest.html')
@app.route('/blood/',methods=['post'])
def blood():
    patientname = request.form['patientname']
    patientage = request.form['patientage']
    REASON = request.form['REASON']
    bloodgroup = request.form['bloodgroup']
    UNIT = request.form['UNIT']
    DATE = request.form['DATE']
    query = "INSERT INTO blood_request() VALUES (%s,%s,%s,%s,%s,%s)"
    data = (patientname,patientage,REASON,bloodgroup,UNIT,DATE)
    return render_template('bloodrequest.html',msgdata='Request Successful!')
@app.route('/bloodhistory/')
def bloodhistory():
    query="SELECT * FROM blood_request"
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('bloodhistory.html',sqldata=data)
@app.route('/donorsearch/')
def donorsearch():
    return render_template('donorsearch.html')
@app.route('/donorsearchresult/',methods=['post'])
def donorsearchresult():
    CITY = request.form['CITY']
    bloodgroup = request.form['bloodgroup']
    query = "SELECT full_name,dob,gender,blood_group,address,city,mobile_no FROM donor_registration WHERE city=%s AND blood_group=%s"
    data=(CITY,bloodgroup)
    mycursor.execute(query,data)
    data=mycursor.fetchall()
    return render_template('donorsearchresult.html',sqldata=data)
@app.route('/donations/')
def donations():
    query="SELECT * FROM donate_blood"
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('donations.html',sqldata=data)
@app.route('/adminrequests/')
def adminrequests():
    query="SELECT * FROM blood_request"
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('adminrequests.html',sqldata=data)
@app.route('/edit/')
def edit():
    return render_template('editdonor.html')
@app.route('/update/',methods=['post'])
def update():
    fullname = request.form['fullname']
    USERNAME = request.form['USERNAME']
    fathername = request.form['fathername']
    mothername = request.form['mothername']
    DOB = request.form['DOB']
    GENDER = request.form['GENDER']
    AGE = request.form['AGE']
    bloodgroup = request.form['bloodgroup']
    ADDRESS = request.form['ADDRESS']
    CITY = request.form['CITY']
    lastdonatedate = request.form['lastdonatedate']
    EMAIL = request.form['EMAIL']
    mobileno = request.form['mobileno']
    PASSWORD = request.form['PASSWORD']
    confirmpassword = request.form['confirmpassword']
    query="UPDATE donor_registration SET full_name=%s,username=%s,father_name=%s,mother_name=%s,dob=%s,gender=%s,age=%s,blood_group=%s,address=%s,city=%s,last_donate_date=%s,email=%s,mobile_no=%s,password=%s,confirm_password=%s"
    data = (fullname,USERNAME,fathername,mothername,DOB,GENDER,AGE,bloodgroup,ADDRESS,CITY,lastdonatedate,EMAIL,mobileno,PASSWORD,confirmpassword)
    mycursor.execute(query,data)
    conn.commit()
    return render_template('editdonor.html',msgdata='Donor Updated!')
@app.route('/home/')
def home():
    return render_template('first.html')
@app.route('/change/')
def change():
    return render_template('editpatient.html')
@app.route('/alter/',methods=['post'])
def alter():
    fullname = request.form['fullname']
    USERNAME = request.form['USERNAME']
    fathername = request.form['fathername']
    mothername = request.form['mothername']
    DOB = request.form['DOB']
    GENDER = request.form['GENDER']
    AGE = request.form['AGE']
    bloodgroup = request.form['bloodgroup']
    DISEASE = request.form['DISEASE']
    ADDRESS = request.form['ADDRESS']
    CITY = request.form['CITY']
    EMAIL = request.form['EMAIL']
    mobileno = request.form['mobileno']
    PASSWORD = request.form['PASSWORD']
    confirmpassword = request.form['confirmpassword']
    query="UPDATE patient_registration SET full_name=%s,username=%s,father_name=%s,mother_name=%s,dob=%s,gender=%s,age=%s,blood_group=%s,disease=%s,address=%s,city=%s,email=%s,mobile_no=%s,password=%s,confirm_password=%s"
    data = (fullname,USERNAME,fathername,mothername,DOB,GENDER,AGE,bloodgroup,DISEASE,ADDRESS,CITY,EMAIL,mobileno,PASSWORD,confirmpassword)
    mycursor.execute(query,data)
    conn.commit()
    return render_template('editpatient.html',msgdata='Patient Updated!')
@app.route('/delete/')
def delete():
    return render_template('deletedonor.html')
@app.route('/eliminate/',methods=['post'])
def eliminate():
    fullname = request.form['fullname']
    query="DELETE FROM donor_registration WHERE full_name=%s"
    data=[(fullname)]
    mycursor.execute(query,data)
    conn.commit()
    return render_template('deletedonor.html',msgdata='Donor Deleted!')
@app.route('/drop/')
def drop():
    return render_template('deletepatient.html')
@app.route('/end/',methods=['post'])
def end():
    fullname = request.form['fullname']
    query="DELETE FROM patient_registration WHERE full_name=%s"
    data=[(fullname)]
    mycursor.execute(query,data)
    conn.commit()
    return render_template('deletepatient.html',msgdata='Patient Deleted!')
    





    
    #Run the flask app
if __name__=='__main__':
    app.run(debug = True)