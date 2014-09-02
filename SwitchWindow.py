import sublime, sublime_plugin
import codecs
import os

from subprocess import Popen, PIPE

class SwitchWindowCommand(sublime_plugin.ApplicationCommand):

  def script_path(self, script_name):
    return os.path.join(sublime.packages_path(), 'SwitchWindow', script_name)

  def window_items(self):
    items = []
    for w in sublime.windows():
      pd = w.project_data()
      if pd and 'folders' in pd and 'path' in pd['folders'][0]:
        # print(pd['folders'][0])
        items.append(pd['folders'][0]['path'].split("/")[-1])
    return sorted(items)

  def selected_window(self, index):
    if index != -1:
      print(self.window_items()[index])
      output = Popen([self.script_path('set_window.sh'), self.window_items()[index]], stdout=PIPE)


  def is_valid(self, val):
    invalid = ['Minimize', 'Minimize All', 'Zoom', 'Zoom All', 'missing value', 'Bring All to Front', 'Arrange in Front']
    if val.strip() in invalid:
      return False
    return True

  def run(self):
    sublime.active_window().show_quick_panel(self.window_items(), self.selected_window)

