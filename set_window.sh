#!/usr/bin/env bash

# See: http://stackoverflow.com/questions/10366003/applescript-google-chrome-activate-a-certain-window
/usr/bin/osascript <<-EOF
  tell application "Sublime Text"
      tell application "System Events"
          tell process "Sublime Text"
              repeat with myItem in every menu item of menu 1 of menu bar item "Window" of menu bar 1
                if "$1" is in name of myItem
                  click myItem
                  exit repeat
                end
              end repeat
          end tell
      end tell
      # Finally, activate the app.
      activate
  end tell
EOF
