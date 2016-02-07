from flask import Flask, request, jsonify, Response, render_template
import pymongo
import json
from flask.ext.pymongo import PyMongo


app = Flask("mentor")
mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def get_index():
	print('=' * 80)
	# render my html page here
	#server ---> quiery to mongodb server; db in background
	# print(mongo.db.collection_names())
	mentors = mongo.db.contacts.find( { "Skill 1" : "Python" } )
	print(mentors[0])
	return render_template('index.html', mentors_we_pass_in=mentors)

@app.route('/test', methods=['GET'])
def get_test():
	print('Inside get_test')
	# render my html page here
	#server ---> quiery to mongodb server; db in background
	# print(mongo.db.collection_names())
	return render_template('test.html')
 
if __name__ == '__main__': 
	app.run('0.0.0.0', port=5000, debug=True)


