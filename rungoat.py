#!/usr/bin/python3
import subprocess, shlex
import webbrowser

hoste="127.0.0.1"
port1="8080"
port2="9090"

goatwolf = "webgoat/goatandwolf"

def checkgoat():
    proc = subprocess.Popen("docker images", shell=True, stdout=subprocess.PIPE, text=True)
    output = proc.stdout.read()
    cmd_line = shlex.split(output)

    for lin in cmd_line:
        if lin == goatwolf:
            print("Repo found")
            rungoat()
            break
    else:
        print("Pulling Webgoat")
        pullgoat()
        rungoat()


def pullgoat():
    subprocess.run(f"docker pull {goatwolf}", shell=True, text=True)

def rungoat():
    subprocess.run(f"docker run -p {hoste}:{port1}:{port1} -p {hoste}:{port2}:{port2} -e TZ=Europe/Amsterdam {goatwolf}", shell=True)

def main():
    try:
        checkgoat()
    except KeyboardInterrupt:
        print("Keyboard Interrupt detected")
        cmd = f"docker ps --filter ancestor={goatwolf}| grep -o "'"\w*$"'" | grep -v "'"NAMES"'""
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, text=True)
        output = proc.stdout.read()
        print(f"Stopping {output}")
        subprocess.run(str(f"docker stop str({output})"), shell=True)

if __name__ == "__main__":
    main()
