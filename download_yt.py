from pytube import YouTube
from extract_yt_links import extract_links
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Absolute file path")
    parser.add_argument("limit", help="Number of links to be downloaded")
    args = parser.parse_args()
    file_path = args.input
    link_list = extract_links(file_path, output=False)
    success, length = 0, len(link_list)
    if args.limit < length:
        length = args.limit
    for link in link_list[:length]:
        try:
            print(f"Starting to download : {link}")
            YouTube(link).streams.filter(progressive=True, file_extension='mp4').order_by("resolution").desc().first().download()
            print("Download completed successfully, going forward !!!")
            success += 1
        except Exception as e:
            print(f"Error downloading : {link}")
        print(" - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("################################")    
    print(f"Downloaded {success} / {length} videos found in the file !!!")

if __name__ == "__main__":
    main()
