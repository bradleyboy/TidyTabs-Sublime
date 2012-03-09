import sublime_plugin
import sublime
import os
import time

win = sublime.Window


def scan_files():
    print sublime.Window.views().length


class TidyTabsCommand(sublime_plugin.WindowCommand):
    def run(self):
        now = time.time()
        for file in self.window.views():
            mtime = os.path.getmtime(file.file_name())
            group = self.window.get_view_index(file)[0]

            if file.file_name() == self.window.active_view_in_group(group).file_name():
                print file.window()
                continue

            print now - mtime

            if now - mtime > 5 and not file.is_dirty():
                print file.window()
                # file.window().run_command('close')
        # global win
        # win = self
        # sublime.set_timeout(scan_files, 1000)
