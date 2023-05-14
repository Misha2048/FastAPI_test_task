# Ex: google.com -> google.com/

def convert_link(link: str) -> str:
    return link + '/' if link[-1] != '/' else link
