# ************************************************************************#
# Title:                    Views  API                                    #
# Description:              This class handles the rendering of data      #
# Author:                   Sambe Consulting <development@sambe.co.za>    #
# Original Date:            20 March 2021                                 #
# Version:                  0.1.0                                         #
# ************************************************************************#

from jinja2 import Environment, FileSystemLoader
from singleton_decorator import singleton
import os


@singleton
class Views(object):
    def __init__(self, view_path):
        self.view_environment = Environment(
            loader=FileSystemLoader(os.path.abspath(view_path))
        )

    def render_view(self, view_name, context=None):
        if context is None:
            context = {}
        return self.view_environment.get_template(view_name).render(**context)
