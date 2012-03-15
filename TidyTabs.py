import sublime_plugin
import os
import time


class TidyTabsCommand(sublime_plugin.WindowCommand):

    def run(self):
        now = time.time()

        for file in self.window.views():

            path = file.file_name()

            '''
            Close the tab if all of the following are true:
                * File still exists
                * File is not the current view in its window
                * File hasn't been modified in 30 minutes
                * File hasn't been accessed in the last minute
                * File is not in an unsaved state (dirty)
                * File is not a scratch (unsaved file)
            '''
            if (os.path.exists(path) == True
                and file.window() == None
                and now - os.path.getmtime(path) > 1800
                and now - os.path.getatime(path) > 60
                and not file.is_dirty()
                and not file.is_scratch()):
                    self.window.focus_view(file)
                    self.window.run_command('close_file')
