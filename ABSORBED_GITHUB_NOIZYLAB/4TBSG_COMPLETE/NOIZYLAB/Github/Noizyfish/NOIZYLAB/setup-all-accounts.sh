#!/bin/bash
# Setup All MacMail Accounts

echo "Setting up Gmail Primary..."
osascript "/Users/m2ultra/NOIZYLAB/email-intelligence/macmail-scripts/setup-gmail-primary.applescript"
sleep 2

echo "Setting up NoizyLab hello..."
osascript "/Users/m2ultra/NOIZYLAB/email-intelligence/macmail-scripts/setup-noizylab-hello.applescript"
sleep 2

echo "Setting up NoizyLab help..."
osascript "/Users/m2ultra/NOIZYLAB/email-intelligence/macmail-scripts/setup-noizylab-help.applescript"
sleep 2

echo "Setting up NoizyLab rsp..."
osascript "/Users/m2ultra/NOIZYLAB/email-intelligence/macmail-scripts/setup-noizylab-rsp.applescript"
sleep 2

echo "Setting up Fish Music info..."
osascript "/Users/m2ultra/NOIZYLAB/email-intelligence/macmail-scripts/setup-fishmusic-info.applescript"
sleep 2

echo "Setting up Fish Music rp..."
osascript "/Users/m2ultra/NOIZYLAB/email-intelligence/macmail-scripts/setup-fishmusic-rp.applescript"
sleep 2

