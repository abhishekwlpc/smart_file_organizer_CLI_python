from pathlib import Path


try:
    file_path = Path(input("Enter the file path(Example file path: C:\\users\\Downloads):"))

    if (file_path.is_dir()):
        print("================================Entered Path===========================================")

        print(f"Your entered file path is: {file_path}")

        document_count =0
        image_count =0
        video_count =0
        audio_count =0
        other_file_count =0

        categorizes = {
            "doc_valid_extentions" : {".doc",".docx",".docm", ".dot", ".dotx", ".dotm",".xls",".xlsx", ".xlsm", ".xlsb", ".xlt", ".xltx", ".xltm",".pdf", ".ppt", ".pptx", ".pptm", ".pps",".ppsx", ".ppsm", ".pot", ".potx", ".potm", ".accdb", ".accde", ".accdt",".mdb",".pub",".vsd",".vsdx",".vsdm"},
            
            "image_valid_extentions" : {".jpg",".jpeg",".png",".gif",".webp",".svg",".avif",".bmp",".tiff",".tif",".ico",".heic",".heif"},
            
            "video_valid_extentions" : {".mp4",".avi",".mov",".mkv",".wmv",".flv",".webm",".m4v"},
            
            "audio_valid_extentions" : {".mp3",".wav",".aac",".flac", ".ogg",".m4a",".wma",".aiff", ".alac",  ".au", ".amr",".ac3", ".caf",".opus",".ra",".snd"}
        }

        folders = {
            "doc_valid_extentions" : "Documents",
            "image_valid_extentions" : "Images",
            "video_valid_extentions" : "Videos",
            "audio_valid_extentions" : "Audios",
            "other_extentions" : "Others"
        }
        

        for file in file_path.iterdir():

            if not file.is_file():
                continue

            type_of_file = ""
            for k ,v in categorizes.items():
                if str(file.suffix.lower()) in v:
                    type_of_file = k
                    break

            if (type_of_file == ""):
                type_of_file = "other_extentions"


            dir_files = Path(file_path, folders[type_of_file])
            dir_files.mkdir(parents=True, exist_ok=True)

            match(type_of_file):
                case "doc_valid_extentions":
                    document_count += 1

                case "image_valid_extentions":
                    image_count += 1

                case "video_valid_extentions":
                    video_count += 1

                case "audio_valid_extentions":
                    audio_count += 1

                case _:
                    other_file_count += 1

            file_target = dir_files / file.name
            if file_target.exists():
                file_renamed = False
                duplicate_file_count =1
                while(file_renamed == False):
                    new_path = dir_files / file.name.replace(file.suffix, str(f"-{duplicate_file_count}{file.suffix}"))
                    print(new_path)

                    if(new_path.exists()):
                        duplicate_file_count += 1
                        continue
                    else:
                        file = file.rename(new_path)
                        file_renamed = True

            else:    
                file.rename(file_target)
                
        print("=================================SUMMARY OF ORGANIZED FILES====================================")
        print("Documents: " , document_count)
        print("Images: " , image_count)
        print("Videos: " , video_count)
        print("Audios: " , audio_count)
        print("Others: " , other_file_count)



    else:
        print("Your entered path is not a directory!")

except FileExistsError as e:
    print("File exisis: " , e)

except FileNotFoundError as e:
    print("File is not found: ", e)