import os
import sys
import tqdm
from mutagen import flac, id3

if len(sys.argv) == 2:
      working_dir = sys.argv[1]
else:
      working_dir = os.getcwd()
      
for root, dirs, files in os.walk(working_dir):
      tracks = [filename for filename in files if filename[-5:] == '.flac']
      if len(tracks) > 0:
            album_cover = flac.Picture()
            with open(root + "/cover.jpg", 'rb') as f:
                  album_cover.data = f.read()
            album_cover.type = id3.PictureType.COVER_FRONT
            album_cover.mime = u"image/jpeg"
            artist, album = root.split("/")[-2:]
            print(artist, '-',  album)
            for filename in tqdm.tqdm(tracks):
                  track_number, track_name = filename[:-5].split(" - ")
                  track = flac.FLAC(root + "/" + filename)
                  track['TITLE'] = track_name 
                  track['ALBUM'] = album 
                  track['ARTIST'] = artist 
                  track['TRACKNUMBER'] = track_number
                  track['TOTALTRACKS'] = str(len(tracks))
                  track.add_picture(album_cover)
                  track.save()
