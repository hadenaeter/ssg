from recursive_copy import rcopy
from generate_page import generate_page

def main():
    rcopy("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__=="__main__":
    main()
