from flask import Flask, send_from_directory, request, render_template
import os

app = Flask(__name__, template_folder='../frontend')

# Props (see ../config.py)
with open("../config.py", "r") as f:
    config = f.read()
exec(config)

# Payloads route
@app.route('/<path:filename>')
def serve_data(filename):
    filename = filename.replace('\\', '/')
    return send_from_directory("../data/pages", filename)

@app.route('/js/<path:filename>')
def serve_js(filename):
    filename = filename.replace('\\', '/')
    return send_from_directory("../data/payloads", filename)

# Get route
@app.route('/backend/sendData/<path:name>', methods=['POST'])
def report(name):
    data = request.get_data().decode('utf-8')
    with open("../data/reports/{}.html".format(name), "w") as f:
        f.write("<table>" + data + "</table>")
    return "gotcha"

dbg = False
if debugMode:
    dbg = True

if __name__ == '__main__':
    app.run(debug=dbg, port=loggerPort)