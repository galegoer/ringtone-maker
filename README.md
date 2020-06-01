# Ringtone-Maker
This is a ringtone maker for Apple devices which requires a YouTube link you would like to use as your ringtone and the time stamp (under 30 seconds).

# Requirements
- Python 3.8
- pytube (install using pip or from the web)
- ffmpeg (install using pip or from the web)
- iTunes (to transfer your ringtones to your iPhone)

# Steps

1. First change the save location for your ringtones in line 6 SAVE_PATH of the ringtone-maker.py file.
Example directory: "C:\\Users\\USERNAME\\Music\\Ringtones\\'

    **Make sure the directory exists and the pathname is correct**

2. When you run the program (Right click the ringtone-maker.py file and click run with python) you will be prompted to type the YouTube link, after typing it hit enter and type the start time of your ringtone in the format M:SS (example 1:05) then hit enter and similarly type the end time and hit enter. **Make sure the time from start to end is within 30 seconds total**
3. After hitting enter the m4r file should appear in the directory you put in SAVE_PATH, the next step is to simply drag it to the Tones section of your connected Apple device.
4. Enjoy your new ringtones


# Known issue
Pytube may have an issue as YouTube sometimes changes its key names. You may follow this branch of the revised code 
https://github.com/nficano/pytube/pull/643
or if you would like to fix the issue yourself at line 299 of extract.py (located where you installed pytube)

```python
299     except KeyError:
300              cipher_url = [
301                parse_qs(formats[i]["cipher"]) for i, data in enumerate(formats)
302              ]
```

Change the string "cipher" to "signatureCipher". Then save and rerun the program.
