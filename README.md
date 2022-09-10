Command line application that saves a picture of a cat in file structure.
API used for cat pictures: https://cataas.com/
Program wriiten in Python using the requests library to call the API
Uses the sys library to allow command line arguments in the program
Make use of the getop library for parsing the command line arguments
Arguments supported:
  -o {output filepath}: output file path to write the image to (required)
  -t {text to overlay}: text to be included in the downloaded image (optional)
If the program is ran without the -o option then the program tells the user that the -o argument is required and doesn't run.
Program is allowed to run without the -t option

RUNNING THE PROGRAM:
  Make sure the system program is being ran on has Python3 installed
  In the command line type: "Python3 mySampleApp.py -o {file_name} -t {optional_message}"
  Ex: Python3 mySampleApp.py -o cat_pic.jpg -t CatzRule

After executing the program there should be a new file in the same directory of the program that contains a picture of a cat