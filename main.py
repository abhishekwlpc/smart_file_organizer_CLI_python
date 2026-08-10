import os
import shutil


file_path = input("Enter the file path(Example file path: C:\\users\\Downloads):")
file_list = os.listdir(file_path)
print("Files and directories in '", file_path, "' :")

image_files = "D:/python_learning/smart_file_organizer_CLI_python/Images"
document_files = "D:/python_learning/smart_file_organizer_CLI_python/Documents"
video_files = "D:/python_learning/smart_file_organizer_CLI_python/Videos"
audio_files ="D:/python_learning/smart_file_organizer_CLI_python/Audios"



for file in file_list:
    if (file.endswith('jpg') or file.endswith('jpeg') or file.endswith('png') or file.endswith('gif') or file.endswith('webp')):
        shutil.move(file, image_files)
    elif(file.endswith('pdf') or file.endswith('doc') or file.endswith('docx') or file.endswith('txt') or file.endswith('pptx') or file.endswith('ppt') or file.endswith('xls') or file.endswith('xlsx')):
        shutil.move(file, document_files)
    elif(file.endswith('mp4') or file.endswith('mkv') or file.endswith('avi') or file.endswith('mov')):
        shutil.move(file, video_files)
    elif(file.endswith('mp3') or file.endswith('wav') or file.endswith('flac')):
        shutil.move(file, audio_files)





