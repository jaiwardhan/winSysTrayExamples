from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast("Hello World!!!",
                   "Python is 10 seconds awsm!",
                   icon_path="custom.ico",
                   duration=10)

# toaster.show_toast("Hello World!!!",
#                    "Python is 10 seconds awsm!",
#                    icon_path="custom.ico",
#                    duration=10)

# Wait for threaded notification to finish
# while toaster.notification_active(): time.sleep(0.1)