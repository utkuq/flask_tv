from flask import Flask, render_template, request, redirect
from tkinter import Button
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import tkinter as tk
import vlc
import streamlink
import socket
import os   

hostname=socket.gethostname()   
localhost=socket.gethostbyname(hostname)  

player = None
root = None
canvas = None

class remote:
    def quit_root():
        if player is not None:
            player.stop()
            root.destroy()
            return redirect(f"http://{localhost}:5000/")
            
        else:
            return 'Herhangi bir kanal açık değil.'
    
    def change_vol(volume_level):
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            volume.SetMasterVolume(volume_level, None)
    
    
    def kanal(urlf):
        global root
        root = tk.Tk()
        root.attributes('-fullscreen', True)
        root.configure(background="pink")

        

        canvas = tk.Canvas(root, highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True)
        
        
        
        
        url = urlf
        streams = streamlink.streams(url)
        best = streams["best"]
        
        global player
        if player == None:
            instance = vlc.Instance("--no-xlib","--fullscreen")
            player = instance.media_player_new()
            media = instance.media_new(best.url)
            player.set_media(media)
            player.set_hwnd(canvas.winfo_id())
            player.play()
                
            root.mainloop()
            return redirect(f"http://{localhost}:5000/")
        elif player is not None:
            player.stop()
            instance = vlc.Instance("--no-xlib","--fullscreen")
            player = instance.media_player_new()
            media = instance.media_new(best.url)
            player.set_media(media)
            player.set_hwnd(canvas.winfo_id())
            player.play()
                
            root.mainloop()
            return redirect(f"http://{localhost}:5000/")
        else:
            return 'HATA'



app = Flask('__name__')

@app.route("/")
def hello_world():
    return render_template("index.html")



@app.route("/show-tv", methods=["POST"])
def show_tv():
    url = request.form['showtv']
    dremote1 = remote
    dremote1.kanal(url)
    return redirect(f"http://{localhost}:5000/")

@app.route("/cnn-turk", methods=["POST"])
def cnn_turk():
    url = request.form['cnn-turk']
    dremote1 = remote
    dremote1.kanal(url)
    return redirect(f"http://{localhost}:5000/")

@app.route("/kanald", methods=["POST", "GET"])
def kanald():
    url = request.form['kanald']
    dremote1 = remote
    dremote1.kanal(url)
    return redirect(f"http://{localhost}:5000/")

@app.route("/atv", methods=["POST"])
def atv():
    url = request.form['atv']
    dremote1 = remote
    dremote1.kanal(url)
    return redirect(f"http://{localhost}:5000/")


@app.route("/trt-haber", methods=["POST"])
def trt_haber():
    url = request.form['trt-haber']
    dremote1 = remote
    dremote1.kanal(url)
    return redirect(f"http://{localhost}:5000/")

@app.route("/haberturk", methods=["POST"])
def haberturk():
    url = request.form['haberturk']
    dremote1 = remote
    dremote1.kanal(url)
    return redirect(f"http://{localhost}:5000/")

@app.route("/halk-tv", methods=["POST"])
def halk_tv():
    url = request.form['halk-tv']
    dremote1 = remote
    dremote1.kanal(url)
    return redirect(f"http://{localhost}:5000/")

@app.route("/haber-global", methods=["POST"])
def haber_global():
    url = request.form['haber-global']
    dremote1 = remote
    dremote1.kanal(url)
    return redirect(f"http://{localhost}:5000/")

@app.route("/ntv", methods=["POST"])
def ntv():
    url = request.form['ntv']
    dremote1 = remote
    dremote1.kanal(url)
    return redirect(f"http://{localhost}:5000/")

@app.route("/a-haber", methods=["POST"])
def a_haber():
    url = request.form['a-haber']
    dremote1 = remote
    dremote1.kanal(url)
    return redirect(f"http://{localhost}:5000/")

@app.route("/volup", methods=["POST"])
def volup():
    dremote2 = remote
    dremote2.change_vol(1)
    return redirect(f"http://{localhost}:5000/")
        
@app.route("/voldown", methods=["POST"])
def voldown():
    dremote2 = remote
    dremote2.change_vol(0)
    return redirect(f"http://{localhost}:5000/")


@app.route("/quit", methods=["POST"])
def quit():
    if request.form['quit'] == "1":
        if player is not None:
            dremote2 = remote
            dremote2.quit_root()
            return redirect(f"http://{localhost}:5000/")
        else:
            return redirect(f"http://{localhost}:5000/")
    else:
        return redirect(f"http://{localhost}:5000/")
    
@app.route("/shutdown", methods=["POST"])
def shutdown():
    os.system("shutdown /s /t 1")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 ,debug=True)