#!/usr/bin/python3
import speech_recognition as sr
import webbrowser
import subprocess



def command():
	r = sr.Recognizer()
	r.energy_threshold = 4000

	with sr.Microphone() as source:
		print("Говорите\n")
		r.pause_threshold = 0.5
		r.adjust_for_ambient_noise(source, duration=1)
		audio = r.listen(source)
	try:
		task = r.recognize_google(audio, language="ru-RU").lower()
		print("\nВы сказали " + task)
	except:
		task = command()
	return task


def makeSomething(task):
	print(task)
	if "открой steam" in task:
		subprocess.call("steam")
	elif "открой диспетчер" in task:
		subprocess.call(["htop"])
	elif "открой браузер" in task:
		subprocess.call(["firefox"])
	elif "данные о системе" in task:
		subprocess.call(["uname", "-a"])
		subprocess.call(["date"])
		subprocess.call(["neofetch"])
	elif "открой youtube" in task:
		webbrowser.open_new_tab('https://www.youtube.com/')
				


while True:
	makeSomething(command())