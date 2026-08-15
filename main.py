import os
import shutil
from pathlib import Path
import uuid

file_path = Path(input("Enter the file path(Example file path: C:\\users\\Downloads):"))

if (file_path.is_dir()):
    print("================================Entered Path===========================================")

    print(f"Your entered file path is: {file_path}")

    #Files
    dir_files = Path(file_path , "Documents")

    if not dir_files.exists():
        dir_files.mkdir(parents=True, exist_ok=True)

    document_valid_extenstions = {".doc",
  ".docx",
  ".docm",
  ".dot",
  ".dotx",
  ".dotm",
  ".xls",
  ".xlsx",
  ".xlsm",
  ".xlsb",
  ".xlt",
  ".xltx",
  ".xltm",
  ".pdf",
  ".ppt",
  ".pptx",
  ".pptm",
  ".pps",
  ".ppsx",
  ".ppsm",
  ".pot",
  ".potx",
  ".potm",
  ".accdb",
  ".accde",
  ".accdt",
  ".mdb",
  ".pub",
  ".vsd",
  ".vsdx",
  ".vsdm"}


    for file in file_path.iterdir():
        if(file.suffix.lower() in document_valid_extenstions):
            file_target = Path(f"{dir_files}/{file.name}")
            if file_target.exists():
                print("Found a same name inside the folder")
                new_path = str(file.parent) + "\\" + file.name.replace(file.suffix, "")+ "-" + str(uuid.uuid4()) + file.suffix
                file = file.rename(new_path)
                file_target = Path(f"{dir_files}/{file.name}")
                file.rename(file_target)
            else:    
                file.rename(file_target)

    
    #Images
    dir_images = Path(file_path , "Images")

    if not dir_images.exists():
        dir_images.mkdir(parents=True, exist_ok=True)

    image_valid_extenstions = {
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".webp",
    ".svg",
    ".avif",
    ".bmp",
    ".tiff",
    ".tif",
    ".ico",
    ".heic",
    ".heif"}


    for image in file_path.iterdir():
        if(image.suffix.lower() in image_valid_extenstions):
            image_target = Path(f"{dir_images}/{image.name}")

            if image_target.exists():
                print("Found a same image name inside the folder")
                new_path = str(image.parent) + "\\" + image.name.replace(image.suffix, "")+ "-" + str(uuid.uuid4()) + image.suffix
                image = image.rename(new_path)
                image_target = Path(f"{dir_images}/{image.name}")
                image.rename(image_target)
            else:    
                image.rename(image_target)

    #Videos
    dir_videos = Path(file_path , "Videos")

    if not dir_videos.exists():
        dir_videos.mkdir(parents=True, exist_ok=True)

    video_valid_extenstions = {
  ".mp4",
  ".avi",
  ".mov",
  ".mkv",
  ".wmv",
  ".flv",
  ".webm",
  ".m4v"}


    for video in file_path.iterdir():
        if(video.suffix.lower() in video_valid_extenstions):
            video_target = Path(f"{dir_videos}/{video.name}")
            if video_target.exists():
                print("Found a same video name inside the folder")
                new_path = str(video.parent) + "\\" + video.name.replace(video.suffix, "")+ "-" + str(uuid.uuid4()) + video.suffix
                video = video.rename(new_path)
                video_target = Path(f"{dir_videos}/{video.name}")
                video.rename(video_target)
            else:    
                video.rename(video_target)

    #Audios
    dir_audios = Path(file_path , "Audios")

    if not dir_audios.exists():
        dir_audios.mkdir(parents=True, exist_ok=True)

    audio_valid_extenstions = {
    ".mp3",
    ".wav",
    ".aac",
    ".flac",
    ".ogg",
    ".m4a",
    ".wma",
    ".aiff",
    ".alac",
    ".au",
    ".amr",
    ".ac3",
    ".caf",
    ".opus",
    ".ra",
    ".snd"}


    for audio in file_path.iterdir():
        if(audio.suffix.lower() in audio_valid_extenstions):
            audio_target = Path(f"{dir_audios}/{audio.name}")
            if audio_target.exists():
                print("Found a same audio name inside the folder")
                new_path = str(audio.parent) + "\\" + audio.name.replace(audio.suffix, "")+ "-" + str(uuid.uuid4()) + audio.suffix
                audio = audio.rename(new_path)
                audio_target = Path(f"{dir_audios}/{audio.name}")
                audio.rename(audio_target)
            else:    
                audio.rename(audio_target)

    #Others
    dir_others = Path(file_path , "Others")

    if not dir_others.exists():
            dir_others.mkdir(parents=True, exist_ok=True)

    for other_file in file_path.iterdir():
        if not other_file.is_dir():
            other_file_target = Path(f"{dir_others}/{other_file.name}")
            if other_file_target.exists():
                print("Found a same file name inside the folder")
                new_path = str(other_file.parent) + "\\" + other_file.name.replace(other_file.suffix, "")+ "-" + str(uuid.uuid4()) + other_file.suffix
                other_file = other_file.rename(new_path)
                other_file_target = Path(f"{dir_others}/{other_file.name}")
                other_file.rename(other_file_target)
            else:    
                other_file.rename(other_file_target)

        
else:
    print("Your entered path is not a directory!")




