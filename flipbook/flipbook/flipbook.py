"""PieChartXBlock is a type of presentational XBlock,
where students are able to visualize data on a pie chart
and even interact with it."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String, List, Boolean, Float
from xblock.fragment import Fragment
from django.template import Context, Template
from django.conf import settings

@XBlock.needs('i18n')
class flipbookXBlock(XBlock):

    display_name = String(display_name="Display Name",
                          default="FlipBook",
                          scope=Scope.settings,
                          help="Name of the component in the edX platform")
    href = String(display_name="href",
                  default="",
                  scope=Scope.content,
                  help="PDF file that will be shown in the XBlock")
    lmsurl=String(display_name="lmsurl",
                  default=settings.LMS_ROOT_URL,
                  scope=Scope.content,
                  help="lms url root")

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        """
        The primary view of the PieChartXBlock, shown to students
        when viewing courses.
        """
        html_pdf = self.resource_string("static/html/flipbook.html")
        template = Template(html_pdf)
        html = template.render(Context({
        }))
        frag = Fragment(html.format(self=self))

        frag.add_javascript(self.resource_string("static/js/src/flipbook.js"))
        frag.initialize_js('flipbookXBlock')
        return frag

    def studio_view(self, context=None):
        """
        The primary view of the PieChartXBlock, shown to teachers
        when editing the block.
        """
        html_edit_chart = self.resource_string("static/html/flipbook_edit.html")
        template = Template(html_edit_chart)


        #parameters sent to browser for edit html page
        html = template.render(Context({
            'display_name': self.display_name,
            'href': self.href,
        }))

        frag = Fragment(html.format(self=self))
        #adding references to external css and js files
        frag.add_css(self.resource_string("static/css/flipbook_edit.css"))
        frag.add_javascript(self.resource_string("static/js/src/flipbook_edit.js"))
        frag.initialize_js('flipbookXBlockEdit')
        return frag

    @XBlock.json_handler
    def save_Charts(self, data, suffix=''):
        """
        Handler which saves the json data into XBlock fields.
        """
        self.display_name = data['display_name']
        self.href = data['href']

        return {
            'result': 'success',
        }

    @XBlock.json_handler
    def send_Data(self, data, suffix=''):
        """
        Handler which sends Pie Chart data back to the javascript
        """
        return {
            'result': 'success',
        }

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("flipbookXBlock",
             """<vertical_demo>
                <flipbook/>
                </vertical_demo>
             """),
        ]
