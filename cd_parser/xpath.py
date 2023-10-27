from lxml import etree, html


class Xpath:
    """
    A class to handle common XPath operations on XML and HTML content.

    Attributes:
        tree (lxml.etree.ElementTree or lxml.html.HtmlElement): The parsed XML or HTML tree.
        base_url (str, optional): The base URL of the content, used to differentiate internal and outbound links.

    Methods:
        get_nodes_by_tag: Returns nodes with a specific tag name.
        get_nodes_by_attribute: Returns nodes with a specific attribute and value.
        get_nodes_by_text: Returns nodes with specific text content.
        get_nth_child: Returns the nth child of a node.
        get_nodes_containing_text: Returns nodes containing specific text.
        get_nodes_by_attribute_containing_text: Returns nodes with an attribute containing specific text.
        get_nodes_by_class: Returns nodes with a specific class attribute.
        get_nodes_by_id: Returns nodes with a specific id attribute.
        get_nodes_by_data_attribute: Returns nodes based on HTML5 data attributes.
        get_nodes_by_name: Returns nodes based on the name attribute.
        get_article_text: Returns the text content of article elements on a page.
        get_images: Returns the src attributes of all image elements on a page.
        get_links: Returns the href attributes of all anchor elements on a page.
        get_links_with_text: Returns a dictionary of anchor text and their corresponding href attributes.
        get_outbound_links_only: Returns the href attributes of all anchor elements that are outbound links.
        get_internal_links_only: Returns the href attributes of all anchor elements that are internal links.
    """

    def __init__(self, content, content_type="html", base_url=None):
        """
        Initializes the Xpath object and parses the provided content.

        Parameters:
            content (str): The XML or HTML content to be parsed.
            content_type (str, optional): The type of content ('xml' or 'html'). Defaults to 'xml'.
            base_url (str, optional): The base URL of the content. Defaults to None.
        """
        if content_type == "xml":
            self.tree = etree.fromstring(content)
        elif content_type == "html":
            self.tree = html.fromstring(content)
        else:
            raise ValueError("Invalid content_type. Choose either 'xml' or 'html'.")
        self.base_url = base_url

    def get_nodes_by_tag(self, tagname):
        """
        Returns nodes with a specific tag name.

        Parameters:
            tagname (str): The tag name to search for.

        Returns:
            list: A list of nodes with the specified tag name.
        """
        return self.tree.xpath(f"//{tagname}")

    def get_nodes_by_attribute(self, tagname, attribute, value):
        """
        Returns nodes with a specific attribute and value.

        Parameters:
            tagname (str): The tag name to search for.
            attribute (str): The attribute name.
            value (str): The attribute value.

        Returns:
            list: A list of nodes with the specified attribute and value.
        """
        return self.tree.xpath(f"//{tagname}[@{attribute}='{value}']")

    def get_nodes_by_text(self, tagname, text):
        """
        Returns nodes with specific text content.

        Parameters:
            tagname (str): The tag name to search for.
            text (str): The text content to match.

        Returns:
            list: A list of nodes with the specified text content.
        """
        return self.tree.xpath(f"//{tagname}[text()='{text}']")

    def get_nth_child(self, parent, child, n):
        """
        Returns the nth child of a node.

        Parameters:
            parent (str): The parent node's tag name.
            child (str): The child node's tag name.
            n (int): The position of the child node.

        Returns:
            list: A list containing the nth child node.
        """
        return self.tree.xpath(f"//{parent}/{child}[{n}]")

    def get_nodes_containing_text(self, tagname, text):
        """
        Returns nodes containing specific text.

        Parameters:
            tagname (str): The tag name to search for.
            text (str): The text content to match.

        Returns:
            list: A list of nodes containing the specified text.
        """
        return self.tree.xpath(f"//{tagname}[contains(text(), '{text}')]")

    def get_nodes_by_attribute_containing_text(self, tagname, attribute, text):
        """
        Returns nodes with an attribute containing specific text.

        Parameters:
            tagname (str): The tag name to search for.
            attribute (str): The attribute name.
            text (str): The text content to match within the attribute value.

        Returns:
            list: A list of nodes with the specified attribute containing the text.
        """
        return self.tree.xpath(f"//{tagname}[contains(@{attribute}, '{text}')]")

    def get_nodes_by_class(self, classname):
        """
        Returns nodes with a specific class attribute.

        Parameters:
            classname (str): The class name to search for.

        Returns:
            list: A list of nodes with the specified class attribute.
        """
        return self.tree.xpath(f"//*[@class='{classname}']")

    def get_nodes_by_id(self, element_id):
        """
        Returns nodes with a specific id attribute.

        Parameters:
            element_id (str): The id value to search for.

        Returns:
            list: A list of nodes with the specified id attribute.
        """
        return self.tree.xpath(f"//*[@id='{element_id}']")

    def get_nodes_by_data_attribute(self, attribute, value):
        """
        Returns nodes based on HTML5 data attributes.

        Parameters:
            attribute (str): The data attribute name without the 'data-' prefix.
            value (str): The value of the data attribute to search for.

        Returns:
            list: A list of nodes with the specified data attribute and value.
        """
        return self.tree.xpath(f"//*[@data-{attribute}='{value}']")

    def get_nodes_by_name(self, name):
        """
        Returns nodes based on the name attribute.

        Parameters:
            name (str): The name attribute value to search for.

        Returns:
            list: A list of nodes with the specified name attribute.
        """
        return self.tree.xpath(f"//*[@name='{name}']")

    def get_article_text(self):
        """
        Returns the text content of article elements on a page.

        Returns:
            list: A list of text content from article elements.
        """
        articles = self.tree.xpath("//article//text()")
        return [text.strip() for text in articles if text.strip()]

    def get_images(self):
        """
        Returns the src attributes of all image elements on a page.

        Returns:
            list: A list of image URLs from the src attributes.
        """
        return self.tree.xpath("//img/@src")

    def get_links(self):
        """
        Returns the href attributes of all anchor elements on a page.

        Returns:
            list: A list of URLs from the href attributes.
        """
        return self.tree.xpath("//a/@href")

    def get_links_with_text(self):
        """
        Returns a dictionary of anchor text and their corresponding href attributes.

        Returns:
            dict: A dictionary where keys are anchor texts and values are URLs.
        """
        anchors = self.tree.xpath("//a")
        return {anchor.text: anchor.get("href") for anchor in anchors if anchor.text}

    def get_outbound_links_only(self):
        """
        Returns the href attributes of all anchor elements that are outbound links.

        Returns:
            list: A list of outbound link URLs.
        """
        all_links = self.get_links()
        if not self.base_url:
            return [link for link in all_links if link.startswith("http://") or link.startswith("https://")]
        return [link for link in all_links if
                (link.startswith("http://") or link.startswith("https://")) and not link.startswith(self.base_url)]

    def get_internal_links_only(self):
        """
        Returns the href attributes of all anchor elements that are internal links.

        Returns:
            list: A list of internal link URLs.
        """
        all_links = self.get_links()
        if not self.base_url:
            raise ValueError("Base URL is not provided. Cannot determine internal links.")
        return [link for link in all_links if link.startswith(self.base_url)]