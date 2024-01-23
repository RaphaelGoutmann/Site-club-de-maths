from pathlib import Path
import shutil
import yaml
from datetime import datetime
from utils.render import render
from utils.converter import markdown2html


def log(msg):
    print(msg)
    

with open("config.yaml", "r") as configFile:
    config = yaml.safe_load(configFile)

    build_path  = Path(config["build"])
    css_path    = Path(config["css"])
    js_path     = Path(config["js"])
    img_path    = Path(config["img"])
    posts_path  = Path(config["posts"])

    
    countdown        = Path(config["countdown"])
    classroom        = Path(config["classroom"])

    templates = {
        "index": Path(config["templates"]["index"]).read_text(),
        "post": Path(config["templates"]["post"]).read_text()
    }

# create build 
build_path.mkdir(exist_ok=True)

# clear build
shutil.rmtree(build_path)

# copy css, js and img
shutil.copytree(css_path, build_path / "css/")
shutil.copytree(js_path,  build_path  / "js/")
shutil.copytree(img_path, build_path  / "img/")

# posts

posts = []

for post in posts_path.glob("*"):
    text = post.read_text()

    if post.suffix == ".md":
        meta, body = markdown2html(text)
    else:
        continue

    posts.append({
        "meta": meta,
        "body": body
    })

# sort posts by date
posts.sort(key=lambda post: datetime.strptime(post["meta"]["date"], f"%d/%m/%Y"), reverse=True)


for post in posts:
    title = post["meta"]["title"]
    
    html = render(templates["post"], context = {
        "title":  title,
        "author": post["meta"]["author"],
        "date":   post["meta"]["date"],
        "body":   post["body"],
    })
    
    output_path  = build_path / (title + ".html")
    with open(output_path, "w") as o:
        o.write(html)

    log(f'"{output_path.name}" written.')


# index

posts_list = ""
for post in posts:
    title = post["meta"]["title"]
    date  = post["meta"]["date"]
    posts_list += f'<a href="{title}.html" class="post">{title} ({date})</a>'

html = render(templates["index"], context = {
    "posts_list": posts_list,
    "countdown": countdown,
    "classroom": classroom
})

with open(build_path / "index.html", "w") as o:
    o.write(html)

log(f'"index.html" written.')

# sucess message

log("Everything's done.")
