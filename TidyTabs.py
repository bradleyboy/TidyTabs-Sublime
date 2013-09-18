import sublime
import sublime_plugin
import os
import time


class TidyTabsCommand(sublime_plugin.WindowCommand):

    def run(self):
        default_settings = sublime.load_settings("TidyTabs.sublime-settings")
        default_modified_duration = default_settings.get('tidytabs_modified_duration')
        default_accessed_duration = default_settings.get('tidytabs_accessed_duration')
        default_threshold = default_settings.get('tidytabs_threshold')
        modified_duration = int(self.window.active_view().settings().get('tidytabs_modified_duration', default_modified_duration))
        accessed_duration = int(self.window.active_view().settings().get('tidytabs_accessed_duration', default_accessed_duration))
        threshold = int(self.window.active_view().settings().get('tidytabs_threshold', default_threshold))
        now = time.time()

        for x in range(0, self.window.num_groups()):

            if (len(self.window.views_in_group(x)) < threshold):
                break

            for file in self.window.views_in_group(x):      
                path = file.file_name()

                '''
                Close the tab if all of the following are true:
                    * File still exists
                    * File is not the current view in its window
                    * File hasn't been modified in <modified_duration> seconds
                    * File hasn't been accessed in <accessed_duration> seconds
                    * File is not in an unsaved state (dirty)
                    * File is not a scratch (unsaved file)
                '''
                if (path
                    and os.path.exists(path) == True
                    and not file == self.window.active_view_in_group(x)
                    and now - os.path.getmtime(path) > modified_duration
                    and now - os.path.getatime(path) > accessed_duration
                    and not file.is_dirty()
                    and not file.is_scratch()):
                        print('CLOSE: ' + path)
                        self.window.focus_view(file)
                        self.window.run_command('close_file')
            


class TidyTabsListener(sublime_plugin.EventListener):
    def on_post_save(self, view):
        run_on_post_save = sublime.load_settings("TidyTabs.sublime-settings").get('tidytabs_run_on_post_save')
        if not run_on_post_save:
            return
        view.window().run_command("tidy_tabs")
