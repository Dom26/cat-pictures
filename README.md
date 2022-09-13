Command line application that saves a picture of a cat in the current file structure.<br>
API used for cat pictures: https://cataas.com/<br>
Program wriiten in Python using the requests library to call the API<br>
Using the shutil library to write a file to the directory<br>
Uses the argparse library to allow command line arguments and parsing of arguments in the program<br>
Arguments supported:<br>
  -o {output filepath}: output file path to write the image to (required)<br>
  -t {text to overlay}: text to be included in the downloaded image (optional)<br>
If the program is ran without the -o option then the program tells the user that the -o argument is required and doesn't run.<br>
Program is allowed to run without the -t option<br>
<br>
RUNNING THE PROGRAM:<br>
  Make sure the system program is being ran on has Python3 installed<br>
  Make sure the system has the requests library for Python. Can be obtained via: pip install requests<br>
  In the command line type: "Python3 mySampleApp.py -o {file_name} -t {optional_message}"<br>
  Ex: Python3 mySampleApp.py -o cat_pic.jpg -t CatzRule<br>
  If you want to write a message that has whitespace surround the message around double quotes: -t "Catz Rule"<br><br>

After executing the program there should be a new file in the same directory of the program that contains a picture of a cat