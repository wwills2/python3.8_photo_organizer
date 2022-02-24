# python3.8_photo_organizer

This simple python program reorganizes a directory of unsorted photos into a sorted library.
The resulting library is a directory tree organized by year -> month -> day. That is, a photo from June 12, 2018, will be moved out
  of its current directory and into Photo_Libary/2018/06/18.
The script creates the year, month, and day directories as-needed

NOTE: Only JPEG and JPG images retain metadata so all other files within the source directory will NOT be moved or altered

The script takes no arguments, and will prompt for the path to the source directory then for the path where root of the library ./Photo_Libary
  will be created. The source directory (at this time) CANNOT have subfolders
  
The script prints out every file name it is moving, as well as the path to its new location
