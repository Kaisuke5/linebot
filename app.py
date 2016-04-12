#coding:utf-8
from flask import Flask, send_from_directory,render_template, request, redirect, url_for, jsonify, json,session
import time
import random

app = Flask(__name__)


# application start



@app.route("/test")
def test():
	return render_template("test.html")


@app.route("/")
def index():
	result = {
			"result": {
				"data1": 1,
				"data2": 2,
			}
	}
	return jsonify(result = result)




@app.route("/post",methods=['GET', 'POST'])
def post():
	return



if __name__ == "__main__":
	app.debug = True
	app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
	app.run()
