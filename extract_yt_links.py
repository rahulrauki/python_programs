import re
def extract_links(file_path, output=None):
    abs_path = file_path.strip()
    # finds https://you && https://www.you
    pattern = re.compile("https:\/\/(?:www\.)?you")

    def extract_link(line):
        word_list = line.strip().split()
        for word in word_list:
            return word if word.startswith("https") else None 

    link_list = []

    with open(abs_path, 'r',encoding="utf-8") as fhand:
        for line in fhand:
            if pattern.match(line):
                link_list.append(extract_link(line))

    if (output):
        with open("links.txt", "w", encoding="utf-8") as fhand:
            fhand.write("\n".join(link_list))
    else: return link_list
