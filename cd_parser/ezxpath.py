from lxml import html

def get_elements(x_path, resp_content):
    html_string = html.fromstring(resp_content)
    elements = html_string.xpath(x_path)
    #elemnts
    return elements