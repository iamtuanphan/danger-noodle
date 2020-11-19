# danger-noodle

This Python script will copy all font files from your ANF fonts directory into your destination directory. Once set up, you will only need to change the "C" variable for future uses.

Let's first track down the three items needed. You can drag the file/folder into the below section (after the semi-colon) to get the path. 

1. Path to your font_copy.py file (A): 

2. Path to your ANF Fonts folder (B): 

3. Path to the issue you are working on (C): 

Now that you have the three parts of the puzzle, let's open up Terminal and run the script. Copy the A, B, and C paths from above into the respective places (inside the double quotes) in the following command, then hit Enter to run:



python "A" --input "B" --output "C"



Example:
python "Desktop/Danger_Noodle/Copy/font_copy.py" --input "/Projects/cr-apple-news-fonts" --output "/Projects/cr.anf.apple.news/Manual Edits/Magazine/Issue"


Tips/Notes: 
1. You can drag-and-drop the folders from your Finder directory into the Terminal window and the full path will be shown. If you do this, you may notice Terminal will add a backslash to your path if you have a space in it. 
2. Put your path inside the double quotes to avoid having to account for special characters or spaces in your file path. If you paste it in from Terminal, then you will need to remove the backslashes (if any).
3. You should only need to change the "C" variable as the script will be able to determine which fonts to copy based off of the output folder. 
