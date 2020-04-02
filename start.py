# This is a flask server
import flask, json, os, re
from flask import request
from waitress import serve

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
	# Force 35 char text limit
	text = request.args.get('text')
	
	# Filter out text
	regex = re.compile("([0-9a-zA-Z ]+)")
	text = regex.findall(text)
	text = "".join(text)

	if len(text) > 35:
		return "That's a lot of text to crash my server..."
	else:
		os.system("echo " + text + " > /dev/ttyACM0") # change this
	return "I should see it now."
serve(app, host='0.0.0.0', port=5002)
