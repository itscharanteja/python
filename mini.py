import tkinter as tk 
import boto3 
import os 
import sys
from tempfile import gettempdir

from contextlib import closing

root=tk.Tk()
root.geometry("400x240")
root.title("text to speech converter ")
texthandler=tk.Text(root,height=10)
texthandler.pack()

def output():
    aws_mag_console=boto3.session.Session(profile_name='vicky_113')
    client=aws_mag_console.client(service_name='polly',region_name='us-east-1')
    result=texthandler.get("1.0","end")
    print(result)
    response=client.synthesize_speech(VoiceId='joanna',OutputFormat='mp3',Text=result,Engine='neural')
    print(response)
    if "audiostream" in response:
        with closing(response['audiostream']) as stream:
            out=os.path.join(gettempdir(),"speech.mp3")
            try:
                with open(out,"wb") as file:
                    file.write(stream.read())
            except IOError as error:
                print("input and output error ")
                sys.exit(-1)
    else:
        print("no audio data found ")
        sys.exit(-1)
    if sys.platform=='win32':
        os.startfile(out)
but=tk.Button(root,height=1,width=10,text="convert to speech ",command=output)
but.pack()


root.mainloop()