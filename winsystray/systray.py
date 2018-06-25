from infi.systray import SysTrayIcon
from balloonTip import WindowsBalloonTip
balloon = WindowsBalloonTip()
def say_hello(systray):
    print "Hello, World!"
    x = balloon.show("aawweseom", "mausam")
menu_options = (("Say Hello", None, say_hello),)
systray = SysTrayIcon("icon.ico", "Example tray icon", menu_options)
systray.start()