import subprocess
import os
import argparse

# Props (see config.py)
with open("config.py", "r") as f:
    config = f.read()
exec(config)

parser = argparse.ArgumentParser(
                    prog='RYTHMICMAMBO omni script',
                    description='Script utils for RYTHMICMAMBO',
                    epilog='Take care!')

parser.add_argument("-s", "--serve", action='store_true', help="Serves the app on port 5000")
parser.add_argument("-f", "--factory", action='store_true', help="Deletes ALL data!")
args = parser.parse_args()

if args.serve:
    os.chdir("backend/")
    subprocess.Popen(["python", "frontend.py"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    print("Frontend open on port {}".format(frontendPort))
    subprocess.Popen(["python", "logger.py"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    print("Logger open on port {}".format(loggerPort))
    quit()

if args.factory:
    def clearData(data):
        for root, dirs, files in os.walk("data/" + data):
            for file in files:
                # delete the file
                os.remove(os.path.join(root, file))
            for dir in dirs:
                # delete the subdirectory
                os.rmdir(os.path.join(root, dir))
    clearData("payloads")
    clearData("pages")
    clearData("reports")
    
    print("All data deleted!")
    quit()
    
print("Select an option. For the available ones, see -h.")