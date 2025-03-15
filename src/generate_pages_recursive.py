import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    content_files = os.listdir(dir_path_content)
    for file in content_files:
        print(f"File: {file}")
        filepath = os.path.join(dir_path_content, file)
        print(f"Filepath: {filepath}")
        if os.path.isdir(filepath):
            print(f"{filepath} is directory")
            os.mkdir(os.path.join(dest_dir_path, file))
            generate_pages_recursive(
                filepath,
                template_path,
                os.path.join(dest_dir_path, file)
            )
        elif file[-3:] == ".md":
            print(f"{filepath} is .md")
            generate_page(
                filepath,
                template_path,
                os.path.join(dest_dir_path, file[0:-3] + ".html")
            )
