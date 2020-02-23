import socket
import naoqi
from naoqi import ALProxy      

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1243))

# Creates a proxy on the speech-recognition module
tts=ALProxy("ALTextToSpeech","10.0.0.102",9559)
asr = ALProxy("ALSpeechRecognition", "10.0.0.102", 9559)
mem = ALProxy("ALMemory", "10.0.0.102",9559)

asr.setLanguage("English")

# for subscriber, period, prec in asr.getSubscribersInfo():
#     asr.unsubscribe(subscriber)

vocabulary = ["recognise","add","sub","multiply", "exit"]
asr.setVocabulary(vocabulary, False)

question="What task do you want me to perform?"
# count=0

# global count
# count += 1
print question

tts.say(question)
#starts listening for an answer
asr.subscribe("TEST_ASR")
data = (None, 0)
while not data[0]:
    data = mem.getData("WordRecognized")
#stops listening after he hears yes or no
asr.unsubscribe("TEST_ASR")
        
# print ("test" ,data[0])
# #client_socket, address = s.accept()
#data="calculate"
if data[0]!="recognise" and data[0]!="exit":
	task="calculate"
	s.send(task.encode())
else:
	s.send(data[0].encode())
tts.say(data[0])
if data[0]=="recognise" :
    tts.say("Ok, let me see")

    while True:
        full_msg = ''
        new_msg = True
        while True:
            msg = s.recv(16)
            if msg == "bye":
              tts.say("Project terminated")
              break;

            #print(msg)
            tts.say(msg)
        break
elif data[0]!="exit":
	i=0
	p=0
	q=1
	tts.say("Ok, let's calculate")
	while True:
		while True:
			msg = s.recv(16)
			print(msg)
			if msg=="openhand":
				a=5
				l1=str(a)
				tts.say(l1)
			elif msg=="win_gesture":
				a=2
				l1=str(a)
				tts.say(l1)
			elif msg=="finger":
				a=1
				l1=str(a)
				tts.say(l1)
			if msg == "bye" or i==2:
				l=str(p)
				lk="equals"
				tts.say(lk)
				tts.say(l)
				tts.say("Try Again")
				break;
			i=i+1
			if data[0]=="add":
				if i==1:
					tts.say("plus")
				p=a+p
			elif data[0]=="sub":
				if i==1:
					tts.say("minus")
				p=a-p
			elif data[0]=="multiply":
				if i==1:
					tts.say("times")
				q=a*q
				p=q
		break

else:
    tts.say("Project terminated")