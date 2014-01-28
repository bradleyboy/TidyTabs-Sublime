#Tidy Tabs for Sublime Text

*Note: Sublime Text 3 beta now supported!*

Ever get to the end (middle?) of a day of coding only to find your window littered with tabs that are nearly impossible to search through visually? Find yourself rage-quitting all your tabs in disgust and starting over? No? Just me? Ok.

With this plugin, a simple keystroke `ctrl + alt + w` will close all tabs whose file has not been modified in the last 30 minutes (to change this interval, see Preferences > Packages > TidyTabs > Settings). It will only close tabs in the background – so files that are open and active in your window won't be closed. Likewise, it will not close files with unsaved changes.

You can change the key binding in Preferences > Package Settings > TidyTabs > Key Bindings.

##Run automatically

You can also configure the plugin to automatically close old tabs each time you save a file. To enable this, go to Preferences > Package Settings > TidyTabs > Settings and set `tidytabs_run_on_post_save` to `true`:

~~~js
// Automatically run tidytabs after a file is saved
"tidytabs_run_on_post_save": true,
~~~

##Threshold

Another configuration option is the **threshold**. Setting this to a number greater than 0 will ensure that TidyTabs only runs when the number of tabs in that view is greater than the threshold.

~~~js
// If this is set and greater than 0, tidytabs will only run if
// the number of tabs is greater than the threshold setting.
"tidytabs_threshold": 5
~~~

##Installation with Package Manager (Recommended)

The easiest way to install is via the excellent [Sublime Package Manager](https://sublime.wbond.net/installation). Once Package Manager is installed, bring up the commands menu (`Command + Shift + P` on Mac, `Control + Shift + P` on Windows or Linux), then type "Package Control" to filter the commands list. Select the "Package Control: Install Package" command, then find and install the TidyTabs plugin.

##Installation without Package Manager
Clone or download this repo to your **Packages** folder.

##License
Licensed under the MIT license.

Copyright (c) Brad Daily

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
