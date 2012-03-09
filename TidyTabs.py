import sublime_plugin
import os
import time


class TidyTabsCommand(sublime_plugin.WindowCommand):

    def run(self):
        now = time.time()

        for file in self.window.views():
            mtime = os.path.getmtime(file.file_name())
            atime = os.path.getatime(file.file_name())
            group = self.window.get_view_index(file)[0]

            # Do not close the current file of any group
            if file.file_name() == self.window.active_view_in_group(group).file_name():
                continue

            # If file is not dirty and has not been modified in one hour
            # and also has not been accessed in the last minute, close it.
            if now - mtime > 3600 and now - atime > 60 and not file.is_dirty():
                self.window.focus_view(file)
                self.window.run_command('close_file')
