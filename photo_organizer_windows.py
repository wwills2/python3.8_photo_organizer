"""
Title = photo_organizer.py
Author = Zan Wills
Date = 12/22/2020
Description:
    takes in a given folder which contains a list of photos (no sub-folders), and the folder to create an
    organized photo library in
    the program then moves the files out of the origin folder into the photo library folder, organized by
    the creation date (year > month > day)
"""

from os import chdir, getcwd, mkdir, scandir, rename
from pathlib import Path

import PIL
from PIL import Image
from PIL.ExifTags import TAGS


def get_exif_date(photo):
    try:
        with Image.open(photo) as opened_photo:  # syntax to open a photo
            opened_photo_data = opened_photo._getexif()  # pulls the file's exif data as a dictionary
            try:
                for key in opened_photo_data:
                    try:
                        if (TAGS[key]) == "DateTimeOriginal":   # TAGS[dictKey] turns the numerical key into english
                            date_time_split = (opened_photo_data[key]).split()
                            creation_date = date_time_split[0]
                            return creation_date
                    except KeyError:
                        print(KeyError, photo)
            except:
                print("no exif data for", photo)
    except PIL.UnidentifiedImageError:
        print(PIL.UnidentifiedImageError)


def create_year(year):
    pass


def create_month(month):
    pass


def create(day):
    pass


def directory_watchdog(current_dir_, creation_year_match, creation_month_match, creation_day_match):
    current_dir_data = str(current_dir_).split("\\")
    if not (current_dir_data[len(current_dir_data)-1] == creation_day_match) and\
            (current_dir_data[len(current_dir_data) - 2] == creation_month_match) and\
            (current_dir_data[len(current_dir_data) - 3] == creation_year_match):
        print("***CRITICAL ERROR***: Failed to open correct directory")
        exit()


def source_check(source_path):
    num_files_source_check = 0
    check_dir = scandir(source_path)
    more_in_iterator = True
    while more_in_iterator:
        try:
            file_in_source = next(check_dir)
            num_files_source_check += 1
            if file_in_source.is_dir():
                print("the source folder can contain no sub-folders")
                return False
        except StopIteration:
            more_in_iterator = False
    print("\nfound", num_files_source_check, "files in", getcwd())
    return True


def move_photo(photo_to_move, photo_lib, creation_year_, creation_month_, creation_day_):
    years = scandir()
    year_exists = False
    for year in years:
        if year.name == creation_year_:
            year_exists = True
    if year_exists:
        chdir(creation_year_)
    else:
        mkdir(creation_year_)
        chdir(creation_year_)

    months = scandir()
    month_exists = False
    for month in months:
        if month.name == creation_month_:
            month_exists = True
    if month_exists:
        chdir(creation_month_)
    else:
        mkdir(creation_month_)
        chdir(creation_month_)

    days = scandir()
    day_exists = False
    for day in days:
        if day.name == creation_day_:
            day_exists = True
    if day_exists:
        chdir(creation_day_)
    else:
        mkdir(creation_day_)
        chdir(creation_day_)

    current_dir = getcwd()
    directory_watchdog(current_dir, creation_year_, creation_month_, creation_day_)
    print("MOVING TO:", getcwd())
    print("\tFROM:", photo_to_move.path)
    dir_to_move_to = Path(str(current_dir)+"\\"+photo_to_move.name)
    rename(photo_to_move.path, dir_to_move_to)
    chdir(photo_lib)


if __name__ == "__main__":
    path_to_source_folder = Path(input("Enter the path where the photos are located: "))
    photo_library_dir = Path(input("Enter the path to the new photo library: "))
    if source_check(path_to_source_folder):
        print("\"Photo Library\" will be created in:", photo_library_dir)
        input("\nPress ENTER to confirm, CTRL+C to abort...")
        chdir(photo_library_dir)
        try:
            mkdir("Photo Library")
        except FileExistsError:
            pass
        chdir("Photo Library")
        # loops through source directory file by file
        in_source_dir = scandir(path_to_source_folder)
        more_in_dir = True
        num_files = 0
        while more_in_dir:
            num_files += 1
            try:
                photo = next(in_source_dir)
                print("photo #"+str(num_files), photo.name)
                try:
                    creation_date = get_exif_date(photo.path).split(":")
                    creation_year = creation_date[0]
                    creation_month = creation_date[1]
                    creation_day = creation_date[2]
                    move_photo(photo, getcwd(), creation_year, creation_month, creation_day)
                except AttributeError:
                    print(AttributeError, "Bad date data")
            except StopIteration:
                more_in_dir = False






    

