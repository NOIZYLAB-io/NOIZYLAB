#!/bin/bash
echo "📱 Connection Information for iPad/iPhone"
echo "=========================================="
echo ""
echo "Your Mac Connection Details:"
echo "---------------------------"
echo "Username: $(whoami)"
echo "Hostname: $(hostname).local"
echo "IP Address (en0): $(ipconfig getifaddr en0 2>/dev/null || echo 'Not found')"
echo "IP Address (en1): $(ipconfig getifaddr en1 2>/dev/null || echo 'Not found')"
echo ""
echo "SSH Connection Command:"
echo "----------------------"
echo "ssh $(whoami)@$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null || hostname).local"
echo ""
echo "Or using IP address:"
if [ ! -z "$(ipconfig getifaddr en0)" ]; then
    echo "ssh $(whoami)@$(ipconfig getifaddr en0)"
elif [ ! -z "$(ipconfig getifaddr en1)" ]; then
    echo "ssh $(whoami)@$(ipconfig getifaddr en1)"
else
    echo "Could not detect IP address. Check manually: System Settings → Network"
fi
echo ""
echo "SSH Status:"
echo "----------"
if sudo systemsetup -getremotelogin 2>/dev/null | grep -q "On"; then
    echo "✅ SSH is ENABLED"
else
    echo "⚠️  SSH status unknown (requires sudo to check)"
    echo "   Enable manually: System Settings → General → Sharing → Remote Login"
fi
echo ""
echo "SSH Key Status:"
echo "--------------"
if [ -f ~/.ssh/id_rsa_ipad ]; then
    echo "✅ SSH key exists: ~/.ssh/id_rsa_ipad"
else
    echo "⚠️  SSH key not found"
    echo "   Create with: ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa_ipad -N '' -C 'ipad-dev-access'"
fi
echo ""
