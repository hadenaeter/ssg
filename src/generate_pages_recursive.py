import os
from generate_page import generate_page

def generate_pages_recursive(
    dir_path_content,
    template_path,
    dest_dir_path,
    BASEPATH = "/"
):
    content_files = os.listdir(dir_path_content)
    for file in content_files:
        filepath = os.path.join(dir_path_content, file)
        if os.path.isdir(filepath):
            os.mkdir(os.path.join(dest_dir_path, file))
            print(os.listdir(dest_dir_path))
            generate_pages_recursive(
                filepath,
                template_path,
                os.path.join(dest_dir_path, file)
            )
        elif file[-3:] == ".md":
            print(".md")
            generate_page(
                filepath,
                template_path,
                os.path.join(dest_dir_path, file[0:-3] + ".html"),
                BASEPATH
            )
