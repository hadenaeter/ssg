from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
    print((f"Generating page from {from_path} to {dest_path} using "
        f"{template_path}"))

    with open(from_path, "r") as f:
        markdown = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    print(f"Title: {title}")

    final_html = template.replace("{{ Title }}", title if title else "")
    final_html = final_html.replace("{{ Content }}", html)

    with open(dest_path, "w") as f:
        f.write(final_html)
