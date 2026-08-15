from pathlib import Path


file_path = Path(input("Enter the file path(Example file path: C:\\users\\Downloads):"))

if (file_path.is_dir()):
    print("================================Entered Path===========================================")

    print(f"Your entered file path is: {file_path}")

    

    for i in range(0,5):
        match(i):
            case 0:
                valid_extenstions = {".doc",".docx",".docm", ".dot", ".dotx", ".dotm",".xls",".xlsx", ".xlsm", ".xlsb", ".xlt", ".xltx", ".xltm",".pdf", ".ppt", ".pptx", ".pptm", ".pps",".ppsx", ".ppsm", ".pot", ".potx", ".potm", ".accdb", ".accde", ".accdt",".mdb",".pub",".vsd",".vsdx",".vsdm"}
                dir_files = Path(file_path , "Documents")
                if not dir_files.exists():
                    dir_files.mkdir(parents=True, exist_ok=True)
                doc_count = 0
            case 1:
                valid_extenstions = {".jpg",".jpeg",".png",".gif",".webp",".svg",".avif",".bmp",".tiff",".tif",".ico",".heic",".heif"}
                dir_files = Path(file_path , "Images")
                if not dir_files.exists():
                    dir_files.mkdir(parents=True, exist_ok=True)
                doc_count = 0
            case 2:
                valid_extenstions = {".mp4",".avi",".mov",".mkv",".wmv",".flv",".webm",".m4v"}
                dir_files = Path(file_path , "Videos")
                if not dir_files.exists():
                    dir_files.mkdir(parents=True, exist_ok=True)
                doc_count = 0
            case 3:
                valid_extenstions = {".mp3",".wav",".aac",".flac", ".ogg",".m4a",".wma",".aiff", ".alac",  ".au", ".amr",".ac3", ".caf",".opus",".ra",".snd"}
                dir_files = Path(file_path , "Audios")
                if not dir_files.exists():
                    dir_files.mkdir(parents=True, exist_ok=True)
                doc_count = 0
            case 4:
                valid_extenstions = {".doc",".docx",".docm", ".dot", ".dotx", ".dotm",".xls",".xlsx", ".xlsm", ".xlsb", ".xlt", ".xltx", ".xltm",".pdf", ".ppt", ".pptx", ".pptm", ".pps",".ppsx", ".ppsm", ".pot", ".potx", ".potm", ".accdb", ".accde", ".accdt",".mdb",".pub",".vsd",".vsdx",".vsdm",".jpg",".jpeg",".png",".gif",".webp",".svg",".avif",".bmp",".tiff",".tif",".ico",".heic",".heif",".mp4",".avi",".mov",".mkv",".wmv",".flv",".webm",".m4v",".mp3",".wav",".aac",".flac", ".ogg",".m4a",".wma",".aiff", ".alac",  ".au", ".amr",".ac3", ".caf",".opus",".ra",".snd"}
                dir_files = Path(file_path , "Others")
                if not dir_files.exists():
                    dir_files.mkdir(parents=True, exist_ok=True)
                doc_count = 0
        # Move Operation
        for file in file_path.iterdir():

            if(i!=4):
                if(file.suffix.lower() in valid_extenstions):
                    doc_count += 1

                    file_target = Path(f"{dir_files}/{file.name}")
                    if file_target.exists():
                        file_renamed = False
                        j =1
                        while(file_renamed == False):
                            print(f"new path setting i is: {i}")
                            new_path = str(file.parent) + "\\" + file.name.replace(file.suffix, "")+ "-" + str(j) + file.suffix
                            file = file.rename(new_path)
                            file_target = Path(f"{dir_files}/{file.name}")
        
                            if(Path(file_target).exists()):
                                print(f"I is: {j}")
                                j += 1
                                continue
                            else:
                                file.rename(file_target)
                                file_renamed = True
                    else:    
                        file.rename(file_target)
            else:
                if(file.suffix.lower() not in valid_extenstions):
                    print("Passed is valid extension for others")
                    
                    file_target = Path(f"{dir_files}/{file.name}")
                    print(file_target)
                    print(file_target.is_file())

                    if(file_target.is_file()):
                        print("Passed")
                        print(file_target)

                        if file_target.exists():
                            file_renamed = False
                            j =1
                            while(file_renamed == False):
                                print(f"new path setting i is: {j}")
                                new_path = str(file.parent) + "\\" + file.name.replace(file.suffix, "")+ "-" + str(j) + file.suffix
                                file = file.rename(new_path)
                                file_target = Path(f"{dir_files}/{file.name}")
            
                                if(Path(file_target).exists()):
                                    print(f"I is: {j}")
                                    j += 1
                                    continue
                                else:
                                    file.rename(file_target)
                                    file_renamed = True
                        else:    
                            file.rename(file_target)
        print(doc_count)


else:
    print("Your entered path is not a directory!")




