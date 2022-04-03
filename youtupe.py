from pytube import Playlist
# By Eslam Es
def install():
    print('Enter URL Here')
    links = input('');play_list = Playlist(links)
    print('Enter Your path');Dir = input('')
    print(str(len(play_list.video_urls)) + ' > ' + 'Videos')
    print('Enter Y for Start Download or N for Cancel')
    what = input('')
    print('Enter resolution as 480, 720, 1080,')
    quilt = input('')
    if what == 'Y':
        for video in play_list.videos:
            video.streams.filter(res=quilt+'p', progressive=True, file_extension='mp4').first().download(Dir)
        print('Download is complete')
    else:
        print('Download is Not complete')

install()
