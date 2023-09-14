
from docutils import nodes
from docutils.parsers.rst import Directive
from typing import List


class NotificationBanner(Directive):

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = True

    def run(self) -> list[nodes.Element]:
        self.assert_has_content()
        node = nodes.container(classes=["wavelet-node"])
        
