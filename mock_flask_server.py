import os
from flask import Flask, send_from_directory


def mock_file_server():
	app = Flask(__name__)

	@app.route('/uploads/<path:filename>', methods=['GET'])
	def download(filename):
		uploads = os.path.join(app.root_path, 'uploads')
		return send_from_directory(uploads, filename, as_attachment=True)
	
	return app

if __name__ == '__main__':
	
	app = mock_file_server()
	app.run(debug=True, host='127.0.0.1')

	