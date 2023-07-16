from flask import Flask, send_from_directory, request, render_template
import os

app = Flask(__name__, template_folder='../frontend')

# Props (see ../config.py)
with open("../config.py", "r") as f:
    config = f.read()
exec(config)

# Access frontend routes
@app.route('/<path:filename>')
def serve_app_files(filename):
    filename = filename.replace('\\', '/')
    return send_from_directory("../frontend/", filename)

@app.route('/')
def index():
    return send_from_directory("../frontend/", "index.html")

# Access data routes
# Terrible solution, data exposed to universal directory
@app.route('/data/<path:filename>')
def serve_data(filename):
    filename = filename.replace('\\', '/')
    return send_from_directory("../data/", filename)

# New Payload backend routes
@app.route('/backend/newPayload', methods=['POST'])
def newPayload():
    form_data = request.form
    with open("templates/base.js", "r") as f:
        base = f.read()
    addons = ""
    for key, value in form_data.items():
        if key == "name":
            # I'm sorry for the un-needed variables, they were just comfy to me
            name = value
            namefile = "../data/payloads/{}".format(value + ".js")
            # Avoids payload overwriting. The rest of the route becomes automatically out-of-scope
            if os.path.exists(namefile):
                return '<script defer src="/js/alreadyExists.js"></script>'
            with open(namefile, "w") as f:
                f.write(base.replace("NAMEVARIABLE", name))
            with open(namefile, "r") as f:
                payload = f.read()
        else:
            with open("templates/{}".format(key + ".js"), "r") as f:
                template = f.read()
            # "Addons" aren't added directly to the final payload.
            # They are first conserved in the "addons" var (see line 24) and added BEFORE the base content in a successive moment
            addons = template + "\n" + addons
    
    # See line 41
    with open (namefile, "w") as f:
        f.write('var dataHTML = ""' + "\n" + addons + payload)
    with open("templates/payloadPage.html") as f:
        payloadPage = f.read().replace("NAMEVARIABLE", name)
    page = "/data/pages/{}.html".format(name)
    with open("../" + page, "w") as f:
        f.write(payloadPage)
    with open ("templates/payloadResponse.html", "r") as f:
        response = f.read().replace("NAMEVARIABLE", name).replace("DOMAINVARIABLE", ipAddress).replace("PORTVARIABLE", str(loggerPort))
    
    
    return response
    
# Payload endpoint and reports
def list_all_files(directory):
    files = []
    for (dirpath, dirnames, filenames) in os.walk(directory):
        files += [os.path.relpath(os.path.join(dirpath, file),directory) for file in filenames]
    return files

@app.route('/reports')
def directory_listing():
    base_dir = "../data/reports"
    files = list_all_files(base_dir)
    return render_template('components/reports.html', files=files)

dbg = False
if debugMode:
    dbg = True
if __name__ == '__main__':
    app.run(debug=dbg, port=frontendPort)