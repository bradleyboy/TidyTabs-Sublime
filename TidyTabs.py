import sublime_plugin
import os
import time


class TidyTabsCommand(sublime_plugin.WindowCommand):

    def run(self):
        now = time.time()

        for file in self.window.views():
            mtime = os.path.getmtime(file.file_name())
            atime = os.path.getatime(file.file_name())

            # Do not close the current file of any group
            if file.window() != None:
                continue

            # If file is not dirty and has not been modified in one hour
            # and also has not been accessed in the last minute, close it.
            if (now - mtime > 3600 and now - atime > 60
                and not file.is_dirty() and not file.is_scratch()):
                self.window.focus_view(file)
                self.window.run_command('close_file')
