class HTMLNode():
    """
    Represents a node containing HTML content with optional children and props
    which are HTML attributes.
    """
    def __init__(self,
        tag: str | None = None, # Tag name
        value: str | None = None,
        children: list | None = None, # A list of HTMLNode objects
        props: dict | None = None, # key-values pairs representing the
                                   # attributes of the HTML tag
    ):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        """
        Converts the HTMLNode in HTML code. Implemented by child classes.
        """
        raise NotImplementedError()

    def props_to_html(self):
        """
        Converts the props (if available) to HTML code.
        """
        html_props = ""
        if self.props:
            for k in self.props:
                html_props += f' {k}="{self.props[k]}"'
            return html_props
        else:
            return ""

    def __repr__(self):
        return f"HTMLNode(tag={self.tag!r}, value={self.value!r}, children={self.children!r}, props={self.props!r})"
