from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: list,
        props: dict | None = None
    ):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode is missing a tag")
        elif not self.children:
            raise ValueError("ParentNode is missing children")
        else:
            in_html = f"<{self.tag}{self.props_to_html()}>"
            for child in self.children:
                in_html += child.to_html()
            in_html += f"</{self.tag}>"
            return in_html
