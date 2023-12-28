def render(s, context = {}):
    
    for key, value in context.items():
        s = s.replace("{{" + str(key) + "}}", str(value))

    return s