import re

path = "./sample.txt"
with open(path) as file:
    s = file.read()
    s = re.sub("<ul>", "<dl>", s)
    s = re.sub("</ul>", "</dl>", s)
    s = re.sub("<li>", "<dt>", s)
    s = re.sub("<br /> ", "<br />", s)
    s = re.sub("(<dt>.+?)(<br />)", "\\1</dt><dd>", s)
    s = re.sub("</li>", "</dd>", s)

path_w = path.replace(".txt", "_output.txt")
with open(path_w, mode='w') as file:
    file.write(s)
