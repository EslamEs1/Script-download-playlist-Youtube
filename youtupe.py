from pytube import Playlist
# By Eslam Es
def install():
    print('Enter URL playlist Here')
    links = input('');play_list = Playlist(links)
    print('Enter Your path');Dir = input('')
    print(str(len(play_list.video_urls)) + ' > ' + 'Videos')
    print('Enter Y for Start Download or N for Cancel')
    what = input('')
    if what == 'Y' or 'y':
        for video in play_list.videos:
                video.streams.get_highest_resolution().download(Dir)
        print('Download is complete')
    else:
        print('Download is Not complete')

install()
