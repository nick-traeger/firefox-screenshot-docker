import io
import os
import tempfile
import subprocess
from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/')
def screenshot():
    url = request.args.get("url", "")
    if not url:
        return "no url specified", 404

    _, temp = tempfile.mkstemp()
    subprocess.call(['firefox', '-headless', '-screenshot', temp, url])

    content = ""
    with open(temp, 'rb') as file:
        content = file.read()

    os.remove(temp)

    return send_file(
        io.BytesIO(content),
        mimetype='image/png',
    )
