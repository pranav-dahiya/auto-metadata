# auto-metadata
 Python script for tagging metadata of flac files

 Assumes directory structure like so:
  
  - path/to/library/Author/Album/TrackNum - TrackName.flac 
 
 and:
  
  - path/to/library/Author/Album/cover.jpg 
  
 
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
