import re


def main(filename):
    f = open(filename)
    txt = f.read()

    links = re.findall(r"\[[^]]+]\(\w[^)/]+\)", txt)

    for link in links:
        if ".md" in link:
            continue
        if "#" in link:
            new = link.replace("#", ".md#")
        else:
            new = link.rstrip(")") + ".md)"

        txt = txt.replace(link, new)
        print(new)

    print(len(links))

    if len(links):
        f = open(filename, "w")
        f.write(txt)
        f.close()


if __name__ == "__main__":

    from pathlib import Path

    pathlist = Path(".").rglob('*.md')
    for path in pathlist:
        print(str(path))
        main(str(path))
