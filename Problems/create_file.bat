@echo off
setlocal enabledelayedexpansion

REM Set the fixed location
set "folder_location=D:\Desktop_files\Hobby_Coding\DataStructures\Problems"

REM Prompt for folder name
set /p folder_name=Enter folder name:

REM Create the folder at the fixed location
mkdir "!folder_location!\!folder_name!"

REM Create two sample files inside the folder
echo. > "!folder_location!\!folder_name!\file1.txt"
echo Sample content for file 1 > "!folder_location!\!folder_name!\file1.txt"
echo. > "!folder_location!\!folder_name!\file2.txt"
echo Sample content for file 2 > "!folder_location!\!folder_name!\file2.txt"

echo Folder "!folder_name!" created at "!folder_location!" with two sample files.
pause
