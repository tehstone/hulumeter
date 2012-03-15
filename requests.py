import os
import cfg
import json

from tornado.web import RequestHandler, addslash
from tornado import template

from lib.scores import ScoreViewer

class TemplateRequest(RequestHandler):

    _template_path = os.path.join(cfg.root, 'templates')
    _loader = template.Loader(_template_path)

    def render_template(self, template, **kwargs):
        template = self._loader.load(template)
        rendered = template.generate(**kwargs)
        self.write(rendered)

class HelloRequest(TemplateRequest):
    def get(self):
        self.render_template('base.html')

class ScoresRequest(RequestHandler):
    @addslash
    def get(self):
        sv = ScoreViewer()
        self.write(sv.get_scores('happy', 'sad'))
