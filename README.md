# Books-Genre-Rental
In this project, I use an ETL pipeline to process data about books from a 
library.  
The result of this process is a list of books from the same genre 
that are popular and currently checked out.

## File for data processing
Excel file books.xlsx who has information about library book.  
Every row represent information about one book.  
Columns represent various characteristic for every book.  

Columns are:
- id (unique value for each book in file)
- title (book name)
- author (book writer)
- published (book published year)
- genre (one or two specific book genre)
- rental (shows whether book is rental or not at the moment)

## Introduction to main python code
Pandas library is used for data process.  
Every step in process is represented in a single function.  

Function is:
- extract data (extracting .xlsx file for further data process)
- filter data (filtering books which is currently rental and belongs to genre which is second parameter of the function)
- sort data (sorting books by published year in ascending order)
- new column (create new column in data, new column 'contra_published' represent published year in upside-down world, this is a little joke)
- create new files (create new excel file as a result of previous data process)

All function and his additional parameters (if there is) are implemented in ETL pipeline method.  
This Python code project is interactive, because when you run it, program will ask user to input desired genre.  
In this way, I have achieved a universal piece of code that will also work on other book files which has the same structure.

## Result files folder
This is folder with excel files which is result of project.  
Every file represent books which belongs to the same genre and is currently rental.  
Books also have new columns with funny reverse year of published.
