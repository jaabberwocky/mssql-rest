import pymssql
from flask import Flask, jsonify, abort

# mssql connections
server = "EC2AMAZ-PK55OI8"
user = "tobias"
password = "tobias128"

conn = pymssql.connect(server, user, password)
c = conn.cursor()

app = Flask(__name__)

@app.route('/user/<int:id>')
def returnScores(id):
	try:
		c.execute('SELECT * FROM data WHERE id = %d' % id)
		r = c.fetchall()
		if len(r) == 0:
			return abort(404)
		d = {'id':r[0][0], 'score':r[0][1], 'lime':r[0][2]}
		resp = jsonify(d)
		resp.status_code = 200
		return resp
	except:
		return abort(404)

if __name__ == "__main__":
	app.run(host='0.0.0.0')

