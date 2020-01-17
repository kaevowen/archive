import youtube_dl as ytdl

def Get_YT_Thumbnail(value):
    url = value.split('v=')
    try:
        video_id = url[1]
        # always return big thumbnail
        return f'http://img.youtube.com/vi/{video_id}/0.jpg'
    except IndexError:
        return False

def Download(value):
    # write some option here
    ytdl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': False,
        'no_warnings': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        #'writethumbnail' : 'best',
        #'skipdownload' : 'True'
    }

    with ytdl.YoutubeDL(ytdl_opts) as ydl :
        ydl.download([value])
        print("Jobs Done!")