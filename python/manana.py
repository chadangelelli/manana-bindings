# -*- coding: utf-8 -*-

import os, json
from random import randint
from Naked.toolshed.shell import muterun_js

class MananaException(Exception):
  pass

class Manana(object):
  def __init__(self, interpreter, node_wrapper, view_dir):
    self.interpreter = interpreter
    self.node_wrapper = node_wrapper
    self.view_dir = view_dir

  # - -- --- -- - -- --- -- - -- --- -- - -- --- -- - -- --- -- -
  def call(self, method, view, context={}):
    self.view = view
    self.context = context

    self.args = {}
    self.args['file'] = "/tmp/manana-{0}".format(str(randint(100000, 999999)))
    self.args['interpreter'] = self.interpreter
    self.args['view_dir'] = self.view_dir
    self.args['view'] = self.view
    self.args['context'] = self.context
    self.args['method'] = method

    args = json.dumps(self.args)

    with open(self.args['file'], 'w') as f:
      f.write(args)
    self.response = muterun_js(self.node_wrapper, self.args['file']);

    if self.response.exitcode == 0:
      self.output = self.response.stdout
      return self.output
    else:
      raise MananaException(self.response.stderr)

  # - -- --- -- - -- --- -- - -- --- -- - -- --- -- - -- --- -- -
  def get_template(self, name):
    return self.call('getTemplate', name)

  # - -- --- -- - -- --- -- - -- --- -- - -- --- -- - -- --- -- -
  def render(self, view, context):
    return self.call('render', view, context)

  # - -- --- -- - -- --- -- - -- --- -- - -- --- -- - -- --- -- -
  def bottle(self, view, context):
    return self.call('bottle', view, context)
