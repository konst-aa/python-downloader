# python-downloader
a small cli I wrote to download some songs for my brother. I found out about `youtube-dl` once I was 80% done with the script, lol.  
uses ffmpeg to reencode mp3 files. Didn't test with mp4 yet. Will add a playlist option as well.
# Usage: 
`python main.py -l <yt-link> -o <output-path | output-dir if reading from a file> -f <txt-file>`

# txt-file format:
On each line:
youtube-link | relative-path.extension 

## note:
trailing newlines will error!
