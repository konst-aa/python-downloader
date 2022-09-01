# importing the module 
from pytube import YouTube
import sys, getopt
import os

def main(argv):
    opts = []
    try:
        opts, args = getopt.getopt(argv,"hl:o:f:")
    except getopt.GetoptError:
        print("python main.py -l <yt-link> -o <output-path | output-dir if reading from a file> -f <txt-file>")
        sys.exit(2)
    opts_dict = dict(opts)
    jobs = []
    out = None
    if "-f" in opts_dict:
        out = opts_dict["-o"]
        with open(opts_dict["-f"], "r") as f:
            for line in f.readlines():
                temp = line.split(" | ")
                jobs += [(temp[0], temp[1].split("\n")[0])] # newline
    else:
        jobs = list(zip(map(lambda opt: opt[1], filter(lambda opt: opt[0] == "-l", opts)), map(lambda opt: opt[1], filter(lambda opt: opt[0] == "-o", opts))))
    for link, output_file in jobs:
        print(f"downloading link {link} as {output_file}")
        try:
            yt = YouTube(link)
        except:
            raise(Exception("Connection Error"))
        ext = output_file.split(".")[-1]
        streams = yt.streams.filter(only_audio=True) if ext == "mp3" else yt.streams.filter(file_extension=ext)
        streams[0].download(output_path=out, filename=(output_file if ext != "mp3" else "temp.wav"))
        if ext == "mp3":
            os.system(f"ffmpeg -i {((out + '/') if out else '') + 'temp.wav'} -codec:a libmp3lame -qscale:a 2 " + ((out + "/") if out else "") + '\ '.join(output_file.split(' ')))

            
if __name__ == "__main__":
    main(sys.argv[1:])
