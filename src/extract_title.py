def extract_title(markdown):
    title_found = False
    lines = markdown.split("\n")
    for line in lines:
        if line[0] == "#" and line[1] == " ":
            title_found = True
            return line[2:].strip()

    if not title_found:
        raise Exception("No title (level 1 heading, e.g.'# title') found")
