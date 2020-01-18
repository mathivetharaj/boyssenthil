from app import app

@app.route('/')
def index():
	return "Thank God!"

@app.route('/home')
def home():
	return "Welcome to the new world!"