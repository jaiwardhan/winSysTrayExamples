
'''
https://fernandofreitasalves.com/how-to-create-python-exe-with-msi-installer-and-cx_freeze/

vc++ 2008 Py2.6+ 
@link https://www.microsoft.com/downloads/en/details.aspx?FamilyID=9b2da534-3e03-4391-8a4d-074b9f2bc1bf&displaylang=en
Build with >python setup.py bdist_msi
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
    name = "tray-notif",
    version = "1.0.0",
    options = {"build_exe": {
        'packages': ['win32gui'],
        'include_files': ['icon.ico'],
        'include_msvcr': True,
    }},
    executables = [Executable("Farm2SystrayManager.py",base="Win32GUI")]
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