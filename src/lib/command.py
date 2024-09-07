import os


class Command:
    def __init__(self, root_folder):
        self.root_folder = root_folder

    def execute(self):
        try:
            _start_dir, folders, _ = next(os.walk(self.root_folder))
        except StopIteration:
            raise Exception(f'Folder "{self.root_folder}" not found.') from None
        for folder in folders:
            self.process_folder(folder)

    def process_folder(self, folder):
        print()
        print(f"Folder: {folder}")
        folder_path = os.path.join(self.root_folder, folder)
        _, subfolders, file_names = next(os.walk(folder_path))

        if not subfolders:
            print("No subfolders found. Skipping.")

        for subfolder in subfolders:
            print(f"Found subfolder: {subfolder}")
            self.move_files_to_parent(subfolder, folder_path)

    @staticmethod
    def move_files_to_parent(folder, parent_path):
        subfolder_path = os.path.join(parent_path, folder)
        _, _, file_names = next(os.walk(subfolder_path))

        log_files_found(file_names)

        for file_name in file_names:
            source_path = os.path.join(subfolder_path, file_name)
            destination_path = os.path.join(parent_path, file_name)
            try:
                os.rename(source_path, destination_path)
            except FileExistsError:
                print(f'Warning: file "{file_name}" already exists. Skipping.')


def log_files_found(file_names):
    if file_names:
        print(f"Found {len(file_names)} file(s). Moving to parent folder.")
    else:
        print("No files found. Skipping.")
