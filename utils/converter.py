import markdown

# MARKDOWN

def markdown2html(text):
    md = markdown.Markdown(extensions=['meta', 'extra', 'toc'])
    body = md.convert(text)
    meta = {key: ' '.join(value) for (key, value) in md.Meta.items() }
    return meta, body

# LATEX

# not supported for the moment
def latex2html(text):
    meta = { 'title': '(empty)',
             'author': '(empty)',
             'date': '01/12/2023',
             'tags': '(empty)' }

    body = ''

    return meta, body