import sys
from recursive_copy import rcopy
from generate_pages_recursive import generate_pages_recursive

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
        basepath = ("/" + basepath) if (basepath[0] != "/") else basepath
    else:
        basepath = "/"

    rcopy("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__=="__main__":
    main()
