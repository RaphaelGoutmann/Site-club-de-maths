import markdown

# MARKDOWN

def markdown2html(text):
    md = markdown.Markdown(extensions=['meta', 'extra', 'toc'])
    body = md.convert(text)
    meta = {key: ' '.join(value) for (key, value) in md.Meta.items() }
    return meta, body