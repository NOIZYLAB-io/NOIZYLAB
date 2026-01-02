local controlTimer = nil

hs.hotkey.bind({}, "ctrl", function()
    controlTimer = hs.timer.doAfter(3, function()
        hs.osascript.applescript([[tell application "System Events"
            display dialog "Display numbers turned off!"
        end tell]])
    end)
end, function()
    if controlTimer then
        controlTimer:stop()
        controlTimer = nil
    end
end)