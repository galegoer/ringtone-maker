# Ringtone-Maker
This is a ringtone maker for Apple devices which asks for a YouTube video version of the ringtone and the time stamp (under 30 seconds).
Currently the following instructions are for Windows.

# Requirements
- Python 3.8 You can install this from https://www.python.org/downloads/ , when downloading make sure you check pip in the optional features
![python install](https://www.dev2qa.com/wp-content/uploads/2018/09/python-3.7-custom-installation-optional-features.png)

If you already have Python installed but not pip you may use this command:

      py -3 -m ensurepip

You can check if you have pip by opening a command prompt and entering the following command:

      pip -V

You should see output similar to the following:

      pip 18.0 from c:\users\administrator\appdata\local\programs\python\python37\lib\site-packages\pip (python 3.7)

- You will also need pytube (install using the command prompt with the command): 

      pip install pytube
- Lastly you will need ffmpeg 
follow this link https://video.stackexchange.com/questions/20495/how-do-i-set-up-and-use-ffmpeg-in-windows to install ffmpeg and add it to PATH (follow the first response)

- iTunes (to transfer your ringtones to your Apple device)

# Steps

1. When you run the program (Double click or open with IDLE and click run as module) you will be prompted to type the YouTube link, after typing it hit enter and type the start time of your ringtone in the format M:SS (example 1:05) then hit enter and similarly type the end time and hit enter. **Make sure the time from start to end is within 30 seconds total**
2. You will be then asked if you would like to use a save direcotry if you hit enter it will save the ringtone to wherever the playlistDownloader.py file is currently located. Otherwise type the directory similarly to the following (Example: C:\Users\myusername\Music\Ringtones\ ) **Make sure the directory exists and the pathname is correct**
3. After hitting enter the m4r file should appear in either the current directory that contains the playlistDownloader.py file if you did not provide a save path or in the save path if it was provided.
4. The last step is to simply drag it to the Tones section of your connected Apple device in the iTunes app.

# Known issues
(This issue would arise from the following output : Error with pytube: 'cipher' )
- Pytube may have an issue as YouTube sometimes changes its key names. You may follow this branch of the revised code 
https://github.com/nficano/pytube/pull/643
or if you would like to fix the issue yourself at line 299 of extract.py (you may find the file by typing 'pip list -v'):

      >pip list -v
      Package           Version    Location                      Installer
      ----------------- ---------- ----------------------------- ---------
      certifi           2020.4.5.2 c:\python38\lib\site-packages pip
      chardet           3.0.4      c:\python38\lib\site-packages pip
      idna              2.9        c:\python38\lib\site-packages pip
      pip               19.2.3     c:\python38\lib\site-packages pip
      **pytube3           9.6.4      c:\python38\lib\site-packages pip**
      requests          2.23.0     c:\python38\lib\site-packages pip
      setuptools        41.2.0     c:\python38\lib\site-packages pip
      typing-extensions 3.7.4.2    c:\python38\lib\site-packages pip
      urllib3           1.25.9     c:\python38\lib\site-packages pip

Follow the directory to pytube3 or pytube and once you locate the extract.py file edit the following line:


```python
299     except KeyError:
300              cipher_url = [
301                parse_qs(formats[i]["cipher"]) for i, data in enumerate(formats)
302              ]
```

Change the string "cipher" to "signatureCipher". Then save and rerun the playlistDownloader.py file.

- Sometimes pytube may not find the title of the youtube video in which case it will name the video unknown_title
