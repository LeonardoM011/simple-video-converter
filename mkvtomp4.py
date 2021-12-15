#!/usr/bin/env python

""" Simple script that converts files from mkv format to mp4 using ffmpeg library and it has to be run on linux """

import sys
import subprocess

__author__ = "Leonardo Marinovic"
__copyright__ = "Copyright (c) 2019 Leonardo Marinovic"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Leonardo Marinovic"
__email__ = "leonardo.leo.201@gmail.com"
__status__ = "Development"

def print_copyright():
    """ Prints copyright info """
    print("Copyright (c) 2019 Leonardo Marinovic")
    print("License MIT")
    print("This is free software: you are free to change and redistribute it.")
    print("There is NO WARRANTY, to the extent permitted by law.")
    print("Written by Leonardo Marinovic.")

def main():
    n = len(sys.argv)

    # If there are no arguments throw an error
    if n <= 1:
        print("Error: No file specified!")
        return

    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("Usage: python ./mkvtomp4.py [filename1] [filename2] ... [filenameN]")
        print("Simple script that converts files from mkv format to mp4 using ffmpeg library and it has to be run on linux")
        print("")
        print("  -h, --help         display this help and exit")
        print("  -v, --version      output version information and exit")
        print("")
        print("Examples: ")
        print("  python ./mkvtomp4.py video.mkv")
        print("""  python ./mkvtomp4.py "long video.mkv" shortvideo.mkv""")
        print("")
        print_copyright()
        return

    if sys.argv[1] == "-v" or sys.argv[1] == "--version":
        print("mkvtomp4 1.0")
        print_copyright()
        return

    # Iterating through all command line arguments
    for i in range(1, n):
        # Changing argument to end with .mp4 and removing old extension
        # Also taking care if file has multiple extensions
        filename = sys.argv[i]
        filename = filename.split('.')

        # If file already has an extension .mp4 ignore
        if filename[-1] == "mp4":
            print(f"Error: {filename[0]} already has an extension of .mp4!")
            continue

        # Everything except last extension
        filename = filename[:-1]
        # Join array using '.'
        filename = ".".join(filename)

        # If join didn't happen then the file has no extension
        if not filename:
            print(f"Error: {filename[0]} needs to have an extension!")
            continue

        # Converting file using ffmpeg (every item is seperated by space in normal bash command)
        bashCommand = ["ffmpeg", "-i", str(sys.argv[i]), "-codec", "copy", filename + ".mp4"]

        # Checking if subprocess throws an error
        try:
            process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE)
        except FileNotFoundError:
            print("Error: Check if you have ffmpeg installed and if its included in path!")
            return
    
        output, error = process.communicate()
        # If error still exists then close program
        if error:
            print(f"Undefined Error: {error}!")
            return
        print(output)


if __name__ == "__main__":
    main()
