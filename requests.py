import os
import cfg
import json

from tornado.web import RequestHandler
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
    def get(self):
        sv = ScoreViewer()
        json_scores = json.dumps(sv.get_scores('happy', 'sad'))
        self.write(json_scores)
