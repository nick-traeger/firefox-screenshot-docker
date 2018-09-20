import io
import os
import re
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
    parameter = ['firefox', '-headless', '-screenshot', temp, url]

    size = request.args.get("size", "")
    if re.match(r"^\d+(,\d+)?$", size):
        parameter.append(
            "--window-size=%s" % (size,)
        )

    subprocess.call(parameter)

    content = ""
    with open(temp, 'rb') as file:
        content = file.read()

    os.remove(temp)

    return send_file(
        io.BytesIO(content),
        mimetype='image/png',
    )
