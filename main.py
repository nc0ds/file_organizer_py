import os
import shutil

file_extensions = {
    "pdf": "PDFs",
    "png": "Images",
    "jpg": "Images",
    "jpeg": "Images",
    "gif": "Images",
    "doc": "Documents",
    "docx": "Documents",
    "txt": "Documents",
    "csv": "Data",
    "xlsx": "Data",
    "zip": "Archives",
    "rar": "Archives",
    "exe": "Executables",
    "mp3": "Music",
    "wav": "Music",
    "mp4": "Videos",
    "avi": "Videos",
    "flv": "Videos",
    "wmv": "Videos",
}


def get_is_relative_path():
    is_relative = None

    while True:
        option = input("Do you want to use relative path? (Y/n): ").strip()

        match option.lower():
            case "y" | "":
                is_relative = True
                break
            case "n":
                is_relative = False
                break
            case _:
                continue

    return is_relative


def is_valid_path(path):
    try:
        os.stat(path)
        return True
    except FileNotFoundError:
        return False


def get_path_from_user(is_relative):
    while True:
        user_path = input(
            "Type the path to directory to be organized: "
            + ("(using relative path) " if is_relative else "(using absolute path) ")
        ).strip()

        if not user_path:
            continue

        path = (os.getcwd() + "/" + user_path) if is_relative else user_path

        if is_valid_path(path):
            return path
        else:
            print("This path does not exist.")


def organize_files(path):
    dir = os.scandir(path)

    for item in dir:
        if not os.DirEntry.is_file(item):
            continue

        filename = item.name
        extension = filename.split(".")[-1]
        filepath = f"{path}/{filename}"
        file_folder = (
            file_extensions[extension] if extension in [*file_extensions] else None
        )
        is_supported = False if not file_folder else True

        if is_supported:
            exist_folder = file_extensions[extension] in [os.listdir(path)]
            output = f"{path}/{file_extensions[extension]}"

            if not exist_folder:
                os.mkdir(f"{path}/{file_extensions[extension]}")

            shutil.move(filepath, output)


def main():
    is_relative = get_is_relative_path()
    path = get_path_from_user(is_relative)
    organize_files(path)


if __name__ == "__main__":
    main()
