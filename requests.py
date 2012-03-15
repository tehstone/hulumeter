import os
import cfg

from tornado.web import RequestHandler
from tornado import template

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

