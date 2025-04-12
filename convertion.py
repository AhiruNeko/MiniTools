import os
from PIL import Image


def convert(directory, old_extension, new_extension):
    counter = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(old_extension.lower()):
                old_file_path = os.path.join(root, file)
                new_file_name = file[:-len(old_extension)] + new_extension
                new_file_path = os.path.join(root, new_file_name)
                try:
                    os.rename(old_file_path, new_file_path)
                    print(f'"{old_file_path}" -> "{new_file_path}"')
                    counter += 1
                except Exception as e:
                    print(f'"{old_file_path}": {e}')
    print("Total convertion:", counter)


def single_to_jpg(path, filename):
    name = ""
    for i in filename:
        if i != ".":
            name += i
        else:
            break
    try:
        with Image.open(path + filename) as img:
            if img.mode in ('RGBA', 'LA'):
                rgb_img = img.convert('RGB')
            else:
                rgb_img = img
            rgb_img.save(path + name + ".jpg", 'JPEG', quality=100)
            print(f"Done:", path + name + ".jpg")

    except Exception as e:
        print(f"Fail: {e}")
        return 0
    return 1


def to_jpg(path, filename, **kwargs):
    total = 0
    if filename == ".":
        for f in os.listdir(path):
            if f.lower().endswith('.png'):
                total += single_to_jpg(path, f)
                if kwargs["delete"]:
                    os.remove(os.path.join(path, f))
        print(total, "processes completed.")
    else:
        single_to_jpg(path, filename)
        if kwargs["delete"]:
            os.remove(os.path.join(path, filename))


def rename(path: str, name_format: str, var: str, begin: str, end: str):
    total = 0
    name_f, ext_f = os.path.splitext(name_format)

    try:
        begin = int(begin)
        if end != "inf":
            end = int(end)
        use_ascii = False
    except ValueError:
        begin = ord(begin)
        if end != "inf":
            end = ord(end)
        use_ascii = True
    iter_var = begin

    for filename in os.listdir(path):
        old_path = os.path.join(path, filename)

        if os.path.isfile(old_path):
            name, ext = os.path.splitext(filename)

            if ext == ext_f:
                new_name = name_f.replace(var, chr(iter_var) if use_ascii else str(iter_var)) + ext_f
                new_path = os.path.join(path, new_name)

                try:
                    os.rename(old_path, new_path)
                    print(f"Success: {filename} → {new_name}")
                except Exception as e:
                    print(f"Fail {filename}: {e}")
                    continue

                iter_var += 1
                total += 1
                if end != "inf":
                    if iter_var > end:
                        break

    print(total, "processes completed.")
