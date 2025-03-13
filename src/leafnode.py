from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self,
        tag: str | None, # Tag name
        value: str,
        props: dict | None = None, # key-values pairs representing the
                                   # attributes of the HTML tag
    ):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value and self.value != "":
            raise ValueError("LeafNode is missing a value")
        elif not self.tag:
            return self.value
        else:
            in_html = f"<{self.tag}{self.props_to_html()}>"
            in_html += self.value
            in_html += f"</{self.tag}>"
            return in_html
