from recursive_copy import rcopy
from generate_pages_recursive import generate_pages_recursive

def main():
    rcopy("static", "public")
    generate_pages_recursive("content", "template.html", "public")

if __name__=="__main__":
    main()
