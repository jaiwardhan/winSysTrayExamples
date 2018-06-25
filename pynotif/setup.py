
'''
################ For notif.py  ####################
'''
# from cx_Freeze import setup, Executable
# setup(
#     name = "notif",
#     version = "1.0.0",
#     options = {"build_exe": {
#         'packages': ["win10toast", "six"],
#         'include_msvcr': True,
#     }},
#     executables = [Executable("notif.py",base="Win32GUI")]
#     )
''''''


############### for balloonTip.py #####################
from cx_Freeze import setup, Executable
setup(
    name = "balloon",
    version = "1.0.0",
    options = {"build_exe": {
        'packages': ["win32gui"],
        'include_msvcr': True,
    }},
    executables = [Executable("balloonTip.py",base="Win32GUI")]
    )



# from cx_Freeze import setup, Executable
# setup(
#     name = "notif",
#     version = "1.0.0",
#     options = {"build_exe": {
#         'packages': ["win10toast"],
#         'include_files': ['boneca.jpg'],
#         'include_msvcr': True,
#     }},
#     executables = [Executable("boneca.py",base="Win32GUI")]
#     )