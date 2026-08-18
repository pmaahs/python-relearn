def initials(name):
    initials = ""
    for word in name.split():
        initials += word[0]
    return initials