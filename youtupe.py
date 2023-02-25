from pytube import Playlist
import os

def download_videos():
    playlist_url = input('Enter playlist URL: ')
    playlist = Playlist(playlist_url)

    download_dir = input('Enter download directory (default is current directory): ')
    if download_dir == '':
        download_dir = os.getcwd()
    else:
        os.makedirs(download_dir, exist_ok=True)

    print(f'{len(playlist.video_urls)} videos found in the playlist.')

    confirmation = input('Do you want to start downloading? (y/n): ')
    if confirmation.lower() != 'y':
        print('Download cancelled.')
        return

    resolution_choice = input('Choose resolution (default is highest available): \n1. Highest\n2. Lowest\n3. Specific\nChoice: ')
    if resolution_choice == '3':
        resolution_input = input('Enter resolution (e.g. 1080p): ')
        resolution_filter = resolution_input.strip()
    elif resolution_choice == '2':
        resolution_filter = 'lowest'
    else:
        resolution_filter = 'highest'

    print('Downloading videos...')
    for video in playlist.videos:
        print(f'Downloading {video.title}...')
        try:
            if resolution_filter == 'lowest':
                video.streams.get_lowest_resolution().download(download_dir)
            elif resolution_filter == 'highest':
                video.streams.get_highest_resolution().download(download_dir)
            else:
                video.streams.filter(res=resolution_filter).first().download(download_dir)
            print(f'{video.title} downloaded successfully.')
        except:
            print(f'Error downloading {video.title}.')
            continue

    print('Download complete.')

if __name__ == '__main__':
    download_videos()
