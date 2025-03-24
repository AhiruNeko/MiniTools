import os


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
