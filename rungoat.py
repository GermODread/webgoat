#!/usr/bin/python3
import subprocess, shlex

hoste="127.0.0.1"
port1="8080"
port2="9090"

def checkgoat():
    proc = subprocess.Popen("docker images", shell=True, stdout=subprocess.PIPE, text=True)
    output = proc.stdout.read()
    cmd_line = shlex.split(output)

    for lin in cmd_line:
        if lin == "webgoat/goatandwolf":
            print("Repo found")
            rungoat()
            break
    else:
        print("Pulling Webgoat")
        pullgoat()
        rungoat()


def pullgoat():
    subprocess.run("docker pull webgoat/goatandwolf", shell=True, text=True)

def rungoat():
    subprocess.run(f"docker run -p {hoste}:{port1}:{port1} -p {hoste}:{port2}:{port2} -e TZ=Europe/Amsterdam webgoat/goatandwolf", shell=True)

def main():
    try:
        checkgoat()
    except KeyboardInterrupt:
        proc = subprocess.Popen("docker ps", shell=True, stdout=subprocess.PIPE, text=True)
        output = proc.stdout.read()
        print("Keyboard Interrupt detected")
        print(output)
        print("Run: docker stop %CONTAINER_NAME")
        inputs = input("Enter name to stop Webgoat container : ")
        subprocess.run(f"docker stop {inputs}", shell=True)


if __name__ == "__main__":
    main()