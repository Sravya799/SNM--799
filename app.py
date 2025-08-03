# from flask import Flask,request,render_template,url_for,redirect,flash,session
# from flask_session import Session
# from otp import genotp
# from stoken import entoken,dntoken
# from cmail import send_mail
# import mysql.connector
# from mysql.connector import(connection)
# mydb=connection.MySQLConnection(user="root",password="Admin",
# host="localhost",db='snmprjdb')
# app=Flask(__name__)
# app.config['SESSION_TYPE']='filesystem' #data data stored in file format
# Session(app)
# app.secret_key='codegnan@18'
# @app.route('/')
# def home():
#     return render_template('welcome.html')
# @app.route('/register',methods=['GET','POST'])
# def register():
#     if request.method=='POST':
#         print(request.form)
#         username=request.form['username']
#         email=request.form['email']
#         gender=request.form['gender']
#         password=request.form['password']
#         cursor=mydb.cursor()
#         cursor.execute('select count(*) from users where useremail=%s',
#         [email])
#         count_email=cursor.fetchone() #(1,)-fetchone(top most record), [(0,)]=fetchall
#         cursor.close()
#         if count_email[0]==0:
#             gotp=genotp() #function call
#             userdata={'username':username,'useremail':email,'userpassword':password,'usergender':gender,'stored_otp':gotp}
#             print(gotp)
#             subject='OTP verification for Simple Notes Management APP'
#             body=f'Use the given otp for otp verify : {gotp}'
#             send_mail(to=email,subject=subject,body=body)
#             flash(f'Otp has been sent to given mail {email}.')
#             return redirect(url_for('otpverify',udata=entoken(userdata)))
#         elif count_email[0]==1:
#             flash(f'{email} already existed')
        
#         # ap='qpgz dgry rzab vfmb'

#     return render_template('register.html')
# @app.route('/otpverify/<udata>',methods=['GET','POST'])
# def otpverify(udata):
#     if request.method=='POST':
#         user_otp=request.form['OTP']
#         try:
#             decrypted_userdata=dntoken(udata)
#             #returns userdata
#         except Exception as e:
#             print(f'Error is {e}')
#             flash('Can not Store your Details please reload te page')
#             return redirect(url_for('register')) 
#         else:  
#             if decrypted_userdata['stored_otp']==user_otp:
#                 cursor=mydb.cursor()#mysql cursor 
#                 cursor.execute('insert into users(username,useremail,password,gender) values(%s,%s,%s,%s)',[decrypted_userdata ['username'],decrypted_userdata['useremail'],decrypted_userdata['userpassword'],decrypted_userdata['usergender']])
#                 mydb.commit()
#                 cursor.close()
#                 flash('Details registered succesfully')
#                 return redirect(url_for('login'))
#             else:
#                 flash('OTP was wrong')
#                 return redirect(url_for('register'))
#     return render_template('otp.html')
# @app.route('/login',methods=['GET','POST'])
# def login():
#     if not session.get('user'):
#         if request.method=='POST':
#             uemail=request.form['useremail']
#             password=request.form['userpassword']
#             cursor=mydb.cursor(buffered=True)
#             cursor.execute('select count(useremail) from users where useremail=%s',[uemail])
#             count_useremail=cursor.fetchone()
#             print(count_useremail)
#             if count_useremail[0]==1:
#                 cursor.execute('select password from users where useremail=%s',[uemail])
#                 stored_password=cursor.fetchone()
#                 if stored_password[0]==password:
#                     session['user']=uemail
#                     return redirect(url_for('dashboard'))
#                 else:
#                     flash('password was wrong pls check')
#                     return redirect(url_for('login'))
            
#             elif count_useremail[0]==0:
#                 flash('Email not found pls register')
#                 return redirect(url_for('login'))
#         return render_template('login.html')
#     else:
#         return redirect(url_for('dashboard'))
# @app.route('/forgotpassword',methods=['GET','POST'])
# def forgotpassword():
#     if request.method=='POST':
#         useremail=request.form['useremail']
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('select count(useremail) from users where useremail=%s',[useremail])
#         count_useremail=cursor.fetchone()
#         if count_useremail[0]==1:
#             subject='Reset link for password update'
#             body=f"{url_for('newpassword',data=entoken(useremail),_external=True)}" 
#             send_mail(to=useremail,subject=subject,body=body)
#             flash('Reset link has been sent given email {useremail}')
#             return redirect(url_for('forgotpassword'))
#         elif count_useremail[0]==0:
#             flash('Email not found pls register')
#             return redirect(url_for('login'))

#     return render_template('forgot.html')
# @app.route('/newpassword/<data>',methods=['GET','POST'])
# def newpassword(data):
#     if request.method=='POST':
#         npassword=request.form['newPassword']
#         cpassword=request.form['confirmPassword']
#         try:
#             decrypt_email=dntoken(data)
#         except Exception as e:
#             print(e)
#             flash('Could not fetch newpassword update link')
#             return redirect(url_for('forgotpassword'))
#         else:
#             if  npassword==cpassword:
#                 cursor=mydb.cursor(buffered=True)
#                 cursor.execute('update users set password=%s where useremail=%s',[npassword,decrypt_email])
#                 mydb.commit()
#                 cursor.close()
#                 flash('Password updated successfully')
#                 return redirect(url_for('login'))
#             else:
#                 flash('password mismatch')

               
#     return render_template('newpassword.html')
# @app.route('/dashboard')
# def dashboard():
#     if session.get('user'):
#         print(session)
#         return render_template('dashboard.html')
#     else:
#         flash(f'pls login first')
#         return redirect(url_for('login'))
# @app.route('/addnotes',methods=['GET','POST'])
# def addnotes():
#     if request.method=='POST':
#         title=request.form['title']
#         description=request.form['description']
#         cursor=mydb.cursor(buffered=True)
#         cursor.execute('insert into notes(title,description,added_by)values(%s,%s,%s)',[title,description,session.get('user')])
#         mydb.commit()
#         cursor.close()
#         flash(f'{title} added successfully')
#         return redirect(url_for('dashboard'))
#     return render_template('addnotes.html')
#  else:
#       flash('pls login first') 
#     return redirect(url_for('login'))
# @app.route('/viewallnotes')
# def viewallnotes():
# #     cursor=mydb.cursor.fetchall()
# #     print(notes_data )
#    return render_template('viewallnotes.html',notes_data=notes_data)
# app.run(use_reloader=True,debug=True)








# # from flask import Flask,request,render_template,redirect,url_for,flash
# # from otp import genotp
# # from stoken import entoken,dntoken
# # from cmail import send_mail
# # import mysql.connector
# # mydb=mysql.connector.connect(user='root',password='Admin',host='localhost',db='snmprjdb')
# # app=Flask(__name__)
# # app.secret_key='codegnan@18'
# # @app.route('/')
# # def home():
# #     return render_template('welcome.html')
# # @app.route('/register',methods=['GET','POST'])
# # def register():
# #     if request.method=='POST':
# #         print(request.form)
# #         username=request.form['username']
# #         email=request.form['email']
# #         password=request.form['password']
# #         gender=request.form['gender']
# #         gotp=genotp()
# #         userdata={'username':username,'useremail':email,'password':password,'usergender':gender,'stored_otp':gotp}
# #         # ap='ktoq sofs govo zqhe'
# #         subject='OTP verification for Simple Notes Management App'
# #         body=f'Use the given otp for otp verification : {gotp}'
# #         send_mail(to=email,subject=subject,body=body)
# #         flash(f'OTP has been sent to given email {email}')
# #         return redirect(url_for('otpverify',udata=entoken(userdata)))
# #     return render_template('register.html')
# # @app.route('/otpverify/<udata>',methods=['GET','POST'])
# # def otpverify(udata):
# #     if request.method=='POST':
# #         user_otp=request.form['OTP']
# #         try:
# #             decrypted_otp=dntoken(udata)
# #         except Exception as e:
# #             print(f'Error is {e}')
# #             flash('Can not store your details pls reload the page')
# #             return redirect(url_for('register'))
# #         else:  
# #             if decrypted_userdata['stored_otp']==user_otp:
# #                 cursor=mydb.cursor()#mysql cursor 
# #                 cursor.execute('insert into users(username,useremail,password,gender) values(%s,%s,%s,%s)',
# #                 [decrypted_userdata ['username'],decrypted_userdata['useremail'],decrypted_userdata['userpassword'],
# #                 decrypted_userdata['usergender']])
# #                 mydb.commit()
# #                 cursor.close()
# #                 flash('Details registered succesfully')
# #                 return 'success'
# #             else:
# #                 return 'wrong otp'
# #     return render_template('otp.html')
# # app.run(use_reloader=True,debug=True)



from flask import Flask, request, render_template, url_for, redirect, flash, session,send_file
from flask_session import Session
from otp import genotp
from stoken import entoken, dntoken
from cmail import send_mail
import mysql.connector
from io import BytesIO
import re
import flask_excel as excel
from mimetypes import guess_type
from mysql.connector import (connection)

mydb = connection.MySQLConnection(user="root", password="Admin", host="localhost", db='snmprjdb')

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'  # data stored in file format
Session(app)
excel.init_excel(app)
app.secret_key = 'codegnan@18'


@app.route('/')
def home():
    return render_template('welcome.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        print(request.form)
        username = request.form['username']
        email = request.form['email']
        gender = request.form['gender']
        password = request.form['password']
        cursor = mydb.cursor()
        cursor.execute('select count(*) from users where useremail=%s', [email])
        count_email = cursor.fetchone()
        cursor.close()

        if count_email[0] == 0:
            gotp = genotp()
            userdata = {
                'username': username,
                'useremail': email,
                'userpassword': password,
                'usergender': gender,
                'stored_otp': gotp
            }
            print(gotp)
            subject = 'OTP verification for Simple Notes Management APP'
            body = f'Use the given otp for otp verify : {gotp}'
            send_mail(to=email, subject=subject, body=body)
            flash(f'Otp has been sent to given mail {email}.')
            return redirect(url_for('otpverify', udata=entoken(userdata)))
        elif count_email[0] == 1:
            flash(f'{email} already existed')

    return render_template('register.html')


@app.route('/otpverify/<udata>', methods=['GET', 'POST'])
def otpverify(udata):
    if request.method == 'POST':
        user_otp = request.form['OTP']
        try:
            decrypted_userdata = dntoken(udata)
        except Exception as e:
            print(f'Error is {e}')
            flash('Can not Store your Details please reload the page')
            return redirect(url_for('register'))
        else:
            if decrypted_userdata['stored_otp'] == user_otp:
                cursor = mydb.cursor()
                cursor.execute(
                    'insert into users(username,useremail,password,gender) values(%s,%s,%s,%s)',
                    [decrypted_userdata['username'], decrypted_userdata['useremail'],
                     decrypted_userdata['userpassword'], decrypted_userdata['usergender']]
                )
                mydb.commit()
                cursor.close()
                flash('Details registered successfully')
                return redirect(url_for('login'))
            else:
                flash('OTP was wrong')
                return redirect(url_for('register'))
    return render_template('otp.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if not session.get('user'):
        if request.method == 'POST':
            uemail = request.form['useremail']
            password = request.form['userpassword']
            cursor = mydb.cursor(buffered=True)
            cursor.execute('select count(useremail) from users where useremail=%s', [uemail])
            count_useremail = cursor.fetchone()
            print(count_useremail)
            if count_useremail[0] == 1:
                cursor.execute('select password from users where useremail=%s', [uemail])
                stored_password = cursor.fetchone()
                if stored_password[0] == password:
                    session['user'] = uemail
                    return redirect(url_for('dashboard'))
                else:
                    flash('password was wrong pls check')
                    return redirect(url_for('login'))
            elif count_useremail[0] == 0:
                flash('Email not found pls register')
                return redirect(url_for('login'))
        return render_template('login.html')
    else:
        return redirect(url_for('dashboard'))


@app.route('/forgotpassword', methods=['GET', 'POST'])
def forgotpassword():
    if request.method == 'POST':
        useremail = request.form['useremail']
        cursor = mydb.cursor(buffered=True)
        cursor.execute('select count(useremail) from users where useremail=%s', [useremail])
        count_useremail = cursor.fetchone()
        if count_useremail[0] == 1:
            subject = 'Reset link for password update'
            body = f"{url_for('newpassword', data=entoken(useremail), _external=True)}"
            send_mail(to=useremail, subject=subject, body=body)
            flash(f'Reset link has been sent to given email {useremail}')
            return redirect(url_for('forgotpassword'))
        elif count_useremail[0] == 0:
            flash('Email not found pls register')
            return redirect(url_for('login'))

    return render_template('forgot.html')


@app.route('/newpassword/<data>', methods=['GET', 'POST'])
def newpassword(data):
    if request.method == 'POST':
        npassword = request.form['newPassword']
        cpassword = request.form['confirmPassword']
        try:
            decrypt_email = dntoken(data)
        except Exception as e:
            print(e)
            flash('Could not fetch new password update link')
            return redirect(url_for('forgotpassword'))
        else:
            if npassword == cpassword:
                cursor = mydb.cursor(buffered=True)
                cursor.execute('update users set password=%s where useremail=%s', [npassword, decrypt_email])
                mydb.commit()
                cursor.close()
                flash('Password updated successfully')
                return redirect(url_for('login'))
            else:
                flash('password mismatch')

    return render_template('newpassword.html')


@app.route('/dashboard')
def dashboard():
    if session.get('user'):
        print(session)
        return render_template('dashboard.html')
    else:
        flash('pls login first')
        return redirect(url_for('login'))


@app.route('/addnotes', methods=['GET', 'POST'])
def addnotes():
    if session.get('user'):
        if request.method == 'POST':
            title = request.form['title']
            description = request.form['description']
            cursor = mydb.cursor(buffered=True)
            cursor.execute('insert into notes(title,description,added_by) values(%s,%s,%s)', [title, description, session.get('user')])
            mydb.commit()
            cursor.close()
            flash(f'{title} added successfully')
            return redirect(url_for('viewallnotes'))
        return render_template('addnotes.html')
    else:
        flash('pls login first')
        return redirect(url_for('login'))


@app.route('/viewallnotes')
def viewallnotes():
    cursor = mydb.cursor(buffered=True)
    cursor.execute('select * from notes where added_by=%s',[session.get('user')])  # You likely need this line to fetch data
    notes_data = cursor.fetchall()
    print(notes_data)
    return render_template('viewallnotes.html', notes_data=notes_data)
@app.route('/viewnotes/<nid>')
def viewnotes(nid):
    cursor=mydb.cursor(buffered=True)
    cursor.execute('select * from notes where nid=%s and added_by=%s',[nid,session.get('user')])
    notesdata=cursor.fetchone()
    return render_template('viewnotes.html',notesdata=notesdata)
@app.route('/deletenotes/<nid>')
def deletenotes(nid):
    if session.get('user'):
       cursor=mydb.cursor(buffered=True)
       cursor.execute('delete from notes where nid=%s and added_by=%s',[nid,session.get('user')])
       mydb.commit()
       flash('Notes deleted Successfully')
       return redirect(url_for('viewallnotes'))
    else:
        flash('pls login first')
        return redirect(url_for('login'))
@app.route('/updatenotes/<nid>',methods=['GET','POST'])
def updatenotes(nid):
    if session.get('user'):
        cursor=mydb.cursor(buffered=True)
        cursor.execute('select * from notes where nid=%s and added_by=%s',[nid,session.get('user')])
        notesdata=cursor.fetchone()
        print(notesdata)
        if request.method=='POST':
            title=request.form['title']
            description=request.form['description']
            cursor.execute('update notes set title=%s,description=%s where nid=%s and added_by=%s',[title,description,nid,session.get('user')])
            mydb.commit()
            cursor.close()
            flash(f'notes updated successfully{title}')
            return redirect(url_for('viewallnotes'))

        return render_template('update.html',notesdata=notesdata)
    else:
        flash('pls login first')
@app.route('/fileupload',methods=['GET','POST'])
def fileupload():
    if session.get('user'):
        if request.method=='POST':
            filedata=request.files['file']
            fname=filedata.filename
            fdata=filedata.read()
            cursor=mydb.cursor(buffered=True)
            cursor.execute('insert into filedata(file_name,file_data,added_by) values(%s,%s,%s)',[fname,fdata,session.get('user')])
            mydb.commit()
            cursor.close()
            flash(f'{fname} successfully stored')
        return render_template('fileupload.html')
    else:
        flash('please login first')
        return redirect(url_for('login'))
@app.route('/viewallfiles')
def viewallfiles():
    if session.get('user'):
        cursor=mydb.cursor(buffered=True)
        cursor.execute('select * from filedata where added_by=%s',[session.get('user')])
        files_data=cursor.fetchall()
        # print(files_data)
        return render_template('viewallfiles.html',files_data=files_data)
    else:
        flash('please login first')
        return redirect(url_for('login'))
@app.route('/view_file/<fid>')
def view_file(fid):
    if session.get('user'):
        cursor=mydb.cursor(buffered=True)
        cursor.execute('select fid,file_name,file_data from filedata where fid=%s and added_by=%s',[fid,session.get('user')])
        fdata=cursor.fetchone()
        data=BytesIO(fdata[2])
        mime_type, _=guess_type(fdata[1])
        print(mime_type)
        return send_file(data,download_name=fdata[1],mimetype=mime_type or 'application/octat-stream',as_attachment=False)
    else:
        flash('please login first')
        return redirect(url_for('login'))
@app.route('/download_file/<fid>')
def download_file(fid):
    if session.get('user'):
        cursor=mydb.cursor(buffered=True)
        cursor.execute('select fid,file_name,file_data from filedata where fid=%s and added_by=%s',[fid,session.get('user')])
        fdata=cursor.fetchone()
        data=BytesIO(fdata[2])
        mime_type, _=guess_type(fdata[1])
        print(mime_type)
        return send_file(data,download_name=fdata[1],mimetype=mime_type or 'application/octat-stream',as_attachment=True)
    else:
        flash('please login first')
        return redirect(url_for('login'))
@app.route('/deletefiles/<fid>')
def deletefiles(fid):
    if session.get('user'):
        cursor=mydb.cursor(buffered=True)
        cursor.execute('delete from filedata where fid=%s and added_by=%s',[fid,session.get('user')])
        mydb.commit()
        cursor.close()
        flash('file deleted successfully')
        return redirect(url_for('viewallfiles'))
    else:
        flash('please login first')
        return redirect(url_for('login'))
@app.route('/search',methods=['GET','POST'])
def search():
    if session.get('user'):
        if request.method=='POST':
            sdata=request.form['searchdata']
            strg=['a-zA-Z0-9']
            pattern=re.compile(f'^{strg}',re.IGNORECASE)
            print(pattern)
            if pattern.match(sdata):
                cursor=mydb.cursor(buffered=True)
                cursor.execute('select * from notes where nid like %s or title like %s or description like %s or create_at like %s',[sdata+'%',sdata+'%',sdata+'%',sdata+'%'])
                matcheddata=cursor.fetchall()
                if matcheddata:
                    return render_template('dashboard.html',matcheddata=matcheddata)
                else:
                    flash(f'{sdata} not found')
                    return redirect(url_for('dashboard'))
            else:
                flash('invalid search data')
                return redirect(url_for('dashboard'))
    else:
        flash('please login first')
        return redirect(url_for('login'))
@app.route('/getexceldata')
def getexceldata():
    if session.get('user'):
        cursor=mydb.cursor(buffered=True)
        cursor.execute('select * from notes where added_by=%s',[session.get('user')])
        stored_data=cursor.fetchall()
        if stored_data:
            array_data=[list(i) for i in stored_data]
            columns=['NOTES_ID','TITLE','DESCRIPTION','CREATED_AT']
            array_data.insert(0,columns)
            return excel.make_response_from_array(array_data,'xlsx',filename='notesdata')
        else:
            flash('No data found')
            return redirect(url_for('dashboard'))
    else:
        flash('please login first')
        return redirect(url_for('login'))
@app.route('/userlogout')
def userlogout():
    if session.get('user'):
        session.pop('user')
        return redirect(url_for('login'))
    else:
        flash("please login to logout")
        return redirect(url_for('login'))
app.run(use_reloader=True, debug=True)
