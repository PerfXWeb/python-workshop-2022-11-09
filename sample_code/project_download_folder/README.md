## Project 2 - Automatically keeping your Downloads-folder clean

*(Source Code in sample_code/project_download_folder)*

### The issue
- I keep downloading stuff from the internet and my downloads folder gets cluttered
- I don't want any files to be deleted but rather to be restructured
- My downloads folder should look clean and accessible after running the program
- There should be an option to keep specific files in the downloads folder if I want to

### The solution
1. All files should be restructured based on their type:
 - Image files (.png, .jpg, .jpeg, .gif, ) should be moved to an "images" folder
 - Video files (.mov, .mp4) should be moved to a "videos" folder
 - Music files (.mp3, .wav, , .aac) should be moved to a "music" folder
 - Documents (.doc, .docx, .pdf, .ppt, .pptc, .xls, .xlsx) should be moved to a "documents" folder
 - Zip files (.zip, .tar, .tar.gz) should be moved to a "zips" folder
 - Any folders that are NOT the ones above should also be moved to the "zips" folder
1. Files that start with "x " should always be kept in the main downloads folder
1. If any of the folders above does not exist within the Downloads folder, then we need to create it