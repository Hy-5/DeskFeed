from appJar import gui

def interface():
    app.addLabel("title", "Welcome")
    app.setLabelBg("title","grey")


def appLaunch():
    global app
    app=gui()
    interface()
    app.go()