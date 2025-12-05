#!/usr/bin/env bash
# Launch LifeSaver Tablet cockpit panels on multiple displays

/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --new-window --kiosk "http://localhost:8080/creative" &

/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --new-window --kiosk "http://localhost:8080/emotech" &

/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --new-window --kiosk "http://localhost:8080/emergency" &
