# auto-metadata
 Python script for tagging metadata of flac files

 Assumes directory structure like so:
  
  - path/to/library/Author/Album/TrackNum - TrackName.flac 
 
 and:
  
  - path/to/library/Author/Album/cover.jpg 
  
  *For renaming files to fit this format, check out `rename`/`perl-rename` for bulk renaming files using regular expressions*
 
 Execute: 
 
 ```
 python auto-metadata.py path/to/library
 ```
 
 Depends on:
 
  - mutagen
  - tqdm 

Install dependencies:

```
pip install mutagen tqdm
```

Creates/Edits the following tags:

- TITLE
- TRACKNUMBER
- TOTALTRACKS
- ARTIST
- ALBUM
- COVER_FRONT
