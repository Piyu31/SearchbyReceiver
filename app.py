from flask import Flask,render_template,redirect,request,session,flash,url_for,g
import datetime
import sys
import random
import time

import json

import email_sms_db

app = Flask(__name__)

app.secret_key="gyw79wvdysbtt45je23asgz56"


@app.route("/")
def index():
	#get all data from db
	email_sms_data = email_sms_db.get_email_sms_details()
	email_sms_list = []
	for e in email_sms_data:
		email_sms_list.append(e)
	return render_template('email_form.html')



receiverlist = []
search_results_activated_by_receiver = False

@app.route("/receiverdata", methods=['GET'])
def receiverWrapper():
   global receiverlist
   global search_results_activated_by_receiver
   receivers_list = []
   if search_results_activated_by_receiver:
       receivers_list = receiverlist
   else:
       receiver_user_list = email_sms_db.get_email_sms_details()
       for user_r in receiver_user_list:
           receivers_list.append(user_r)
   search_results_activated_by_receiver = False
   return render_template('email_form.html',  emailsmslist = receivers_list)


@app.route('/reveiver/searchbyid', methods=['POST'])
def searchDatabyreceiverid():
   global receiverlist
   global search_results_activated_by_receiver
   receivers_list = []
   receiver_id = request.form['searchbyreceiverid']
   receiver_user_list = email_sms_db.search_receiver_by_id(receiver_id)
   for user_r in receiver_user_list:
       receivers_list.append(user_r)
   print(receivers_list)
   receiverlist = receivers_list
   search_results_activated_by_receiver = True
   return redirect(url_for('receiverWrapper'))



"""
def setData():
	emailsmsRecords = {}
	
	user_name = request.form['uname']
	mobile_number =  request.form['mobilenum']
	user_email =  request.form['uemail']
	#set data to the Empty list
	emailsmsRecords ["user_name"]=user_name
	emailsmsRecords ["mobile_number"]=mobile_number
	emailsmsRecords ["user_email"]=user_email
	
	return emailsmsRecords


@app.route("/", methods=['POST'])
def update_emailsmsrecord():
	emailsmsRecords = setData()
	#print records in cmd
	print(emailsmsRecords)
	email_sms_db.save_email_sms_details(emailsmsRecords)
	return redirect(url_for('index'))
	"""


if __name__ == '__main__':
	app.run(debug=True)

	
