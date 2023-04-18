Problem:
* Difficulty in knowing the characteristics of a database in its entirety
* Comparing the set of images in a database traditionally (Done by humans) for observing the type of manipulations that they have undergone
* Find Data from our not so traditional sources, such as different file formats

Solutions:
* This analyzer can help us understand the kind of manipulations we are dealing with
* It can give us a quick idea of large amounts of data without the need to stop and review it
* It is scalable, and we can add the analysis of other characteristics thanks to its implementation prepared to be expanded
* It is a tool that can speed up the process of searching for databases that are useful to us

Notes on Tool Execution:
(To test the analyzer, we must understand the way it works)
* Open your terminal
* Go to the directory "scripts" were you'll see the main.py file
* Run "py main.py" along with the masks in the command prompt (For example: "py main.py 0 1 0 0" for analyzing a database mean dimensions)

Functionalities:
(The program will allow us to select those characteristics that we mark as "1" in the arguments, which we can analyze, or mark them with "0" to ignore them)
* First: Percentage of Color Images in the Database (A folder path is required)
* Second: Average Dimensions of Images in the Database (A folder path is required)
* Third: Manipulations suffered on an Image from the Database (Paths of original and tampered images are required)
* Fourth: Extraction of Images from a .pdf File (PDF File is required)

Remember:
! It is advisable to place the database in directory "resources/database"
! The fourth functionality, will generate a folder with the same name as the PDF file (For an easier identification) in "resources/articles" folder, that will contain the images found in the PDF File

Execution Example:
*As we have mentioned, by running "py main.py 1 1 1 1", we can perform analyses on the four possible characteristics.

--------------------------------------------------------------------------------------------------------------------------------

Implementation Details:
* It's fully implemented in Python
* It uses a pickle import for faster parameters identification, as it's a tool prepared to be scaled
--> For adding functionalities, we would just add the functionality name to the imported dictionary and few more things
* Every module follows the exact same structure
