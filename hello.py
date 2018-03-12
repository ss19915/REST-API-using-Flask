import MySQLdb
from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/')
def index():
	return "This API can provide capital of various country. Please go to /capital/Country_Name/ to get capital of the given country in JSON format. "
@app.route('/capital')
def noInput():
	return "No Input found! Please enter /countryName after the link" 
@app.route('/capital/<string:countryName>',methods=['GET'])
def capital(countryName):
	name=countryName
	connection=MySQLdb.connect("localhost","root","1234","data");
	cursor=connection.cursor()
	sql='select country,capital from capital where country="'+name+'"'
	cursor.execute(sql)
	result= cursor.fetchall()
	connection.close()
	if len(result)<1:
		return "Invalid Country! No Country found with name '"+countryName+"'"
	return jsonify({'COUNTRY':result[0][0],'CAPITAL':result[0][1]})
if __name__ =='__main__':
	app.run(debug=True);