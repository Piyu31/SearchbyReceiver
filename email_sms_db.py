from pymongo import MongoClient
import datetime
import sys

from bson.objectid import ObjectId

global con
global db
global col

"""
def connect_db():
	global con
	global db
	global col
	con = MongoClient('mongodb+srv://test:test@cluster0.kw4id.mongodb.net/Email_Config?retryWrites=true&w=majority')
	db = con.Email_Config
	col = db.email_sms_records
	"""



def connect_db():
	global con
	global db
	global col
	con = MongoClient('mongodb+srv://test:test@cluster0.kw4id.mongodb.net/consumer_db?retryWrites=true&w=majority')
	db = con.consumer_db
	col = db.email_info3


def get_email_sms_details():
	global col
	connect_db()
	email_Sms_data_from_db = col.find({})
	return email_Sms_data_from_db


def search_receiver_by_id(id):
   global col
   connect_db() 
   searched_data = col.find({'receiver_id':str(id)})
   return searched_data


"""
def save_email_sms_details(email_sms_data):
	global col
	connect_db()
	col.insert(email_sms_data)
	return "saved Successfully"
	"""