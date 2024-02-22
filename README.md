# Canvas Merge

This repo produces attendance records for Canvas discussions. 

## Steps
**Step 1:**
Run `save_canvas_discussion.py` (credit to https://github.com/dsp444) targeting the desired Canvas discussion page. This script captures all the necessary discussion data and saves it as a JSON file. 

**Step 2:**
Execute canvas2csv.py with the JSON discussion data to automatically search for and match student names in a specified .csv roster file. It then updates and outputs a CSV file with the latest attendance record.

## Command Lines



Followings are the original readme forked from https://github.com/dsp444/save_canvas_discussion We thank their efforts!

## save_canvas_discussion
Script that will convert discussion posts from Canvas LMS and save them to files. Canvas allows you to download all submissions to assignments, but there is no way to do the same thing with discussion posts.  However, the data is available in JSON format, it just needs parsed into readable files.  This script will parse the data and save it into individual HTML files for each student.  The format of the HTML files is the same as the format of the HTML files from downloaded assignment submissions.

Unfortunately, Canvas requires Bearer authentication to get access to the data, which is a pain to do through the API and you have to go through institutional access.  So this Python script cannot get the data directly from the Canvas website, you have to download it into a text file first.

The script can be run 2 ways - with 2 different types of inputs:
   1) Give it 3 arguments: an institution name, course ID, and discussion ID.  If the script detects these inputs, it will report the web address to use to get your discussion posts. Copy and paste this address into a browser and save the results as a file.
   2) Once you have the posts saved as a file, run this script with a filename as the argument and it will process the file and save the posts into individual HTML files.
