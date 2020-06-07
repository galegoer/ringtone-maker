from pytube import YouTube 
import os
import subprocess


def download_audio(downloadLink, start_time, end_time, save_path):
    try:
        start_time = convert_time(start_time)
        end_time = convert_time(end_time)
    except:
        print("Error with start and or end times")
        print("Please input in format 0:00 and make sure the time code is valid")
        return
    
    #Begin downloading the video    
    try:
        yt = YouTube(downloadLink)
        for i in range(3):
            if yt.title == 'YouTube':
                yt = YouTube(downloadLink)
            else:
                break
    except Exception as e:
        print(e)
        return
    d_video = yt.streams.filter(only_audio=True).first()
    try:
        #downloading the video
        title = yt.title.replace('\\', '').replace('/', '').replace(':', ' - ').replace('*', '-').replace('?', '').replace('<', '').replace('>', '').replace('|', '').replace('.', '')        
        dfile = d_video.download()
        file_path = title+'.mp4'
        if save_path != '':
            file_path = save_path+title+'.mp4'
            os.rename(dfile, file_path)

        print("DOWNLOADED: "+ title)
    except Exception as e:
        print(e)
        print("Error Downloading the YouTube video") 
        return
                
    #ffmpeg convert mp3 to AAC
    mp4_file = title + '.mp4'
    m4a_file = title + '.m4a'
    m4r_file = title + '.m4r'
    if save_path != '':
        os.chdir(save_path)
        
    cmd = ['ffmpeg', '-ss', start_time, '-to', end_time, '-i', mp4_file, '-c:a', 'aac', m4a_file]
    subprocess.call(cmd)
    os.remove(mp4_file)
    
    os.rename(m4a_file, m4r_file)

def convert_time(time):
    time_array = time.split(':')
    mins = str(int(time_array[0])*60)
    seconds = str(int(time_array[1]))
    return mins + seconds

if __name__ == "__main__":
    print("You will need a link to a YouTube video of the ringtone you would like and start and end times (MAX 30 seconds)")
    print("Start and end time must be in the format M:SS ")
    link = input("Enter YouTube link: ")
    start_time = input("Enter start time of your ringtone in format 0:00 : ")
    end_time = input("Enter end time of your ringtone in the format 0:00 : ")
    save_path = input("Enter the save path where you would like to save your ringtones or push Enter/Return \n" +
          "to save it to wherever this file is located. \n An example of a save path is 'C:\\Users\\username\\Music\\Ringtones\\'")
    
    download_audio(link, start_time, end_time, save_path)