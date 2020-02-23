# HandPose Recognition Using Robot Nao
# Hand Gesture Recognition

#Final results on youtube

https://youtu.be/Z4OlGZwVVWg

# Getting Started

These instructions will help you setting up the project and understanding how the software is working. You'll see the file structure and what each file does. 

# Requirements
See the *requirements.txt* file or simply run:

    pip install -r requirements.txt

I think that I have wrote them all/

# Training your model
Make sure that you have the needed dataset and then run

 python train.py --dataset data --model model/activity.model --label-bin model/lb.pickle --epochs 50

#Test Your Model

Test your trained model, by runing a code that does not require Nao, run:

python camera.py


# How To Run

It is a socket client server application so what you have to do is: 

 1) run python server.py
 2) run cl.py
 3) wait for the question "What Task Do You Want Me to Perform?"
 4) The available tasks are " Recognise , Add , Sub , Multiply , Exit "
 5) the programm either terminates by itself or by pressing q
 6) for more watch the video above

## Author
 Athanasia Karalakou , Technical University Of Crete , athanasiak1997@gmail.com
 
