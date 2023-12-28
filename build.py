from pathlib import Path
import shutil
import markdown
import yaml
from render import render
from datetime import datetime

with open("config.yaml", "r") as configFile:
    config = yaml.safe_load(configFile)

    build_path = Path(config["build"])
    css_path   = Path(config["css"])
    js_path    = Path(config["js"])

    templates = {
        "index": Path(config["templates"]["index"]).read_text(),
        "post": Path(config["templates"]["post"]).read_text()
    }

# create build 
build_path.mkdir(exist_ok=True)

# clear build
shutil.rmtree(build_path)

# copy css and js
shutil.copytree(css_path, build_path / "css/")
shutil.copytree(js_path, build_path  / "js/")

# posts

posts = []

posts_path     = Path("posts/")
for post in posts_path.glob("*.md"):
    md = markdown.Markdown(extensions=["meta", "extra", "toc"])
    body = md.convert(post.read_text())
    meta = md.Meta
    posts.append({
        "meta": meta,
        "body": body
    })

# sort posts by date
posts.sort(key=lambda post: datetime.strptime(post["meta"]["date"][0], f"%d/%m/%Y"))


for post in posts:
    title = post["meta"]["title"][0]
    
    html = render(templates["post"], context = {
        "title":  title,
        "author": post["meta"]["author"][0],
        "date":   post["meta"]["date"][0],
        "tags":   post["meta"]["tags"][0],
        "body":   post["body"],
    })
    
    output_path  = build_path / (title + ".html")
    with open(output_path, "w") as o:
        o.write(html)

# index

posts_list = ""
for post in posts:
    title = post["meta"]["title"][0]
    date  = post["meta"]["date"][0]
    posts_list += f'<a href="{title}.html" class="post">{title} ({date})</a>'

html = render(templates["index"], context = {
    "posts_list": posts_list
})

with open(build_path / "index.html", "w") as o:
    o.write(html)


# sucess message

print("Done.")
