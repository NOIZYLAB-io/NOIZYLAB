#!/usr/bin/env python3
"""
NoizyLab Slack Integration Package
===================================
Enterprise Slack integration for NoizyLab Portal
"""

from .slack_core import SlackClient, SlackMessage, SlackBlockBuilder, send_alert, send_system_status
from .slack_notifier import NoizyLabSlackNotifier, alert, network_event, email_event, deployment

__all__ = [
    'SlackClient',
    'SlackMessage',
    'SlackBlockBuilder',
    'NoizyLabSlackNotifier',
    'alert',
    'network_event',
    'email_event',
    'deployment',
    'send_alert',
    'send_system_status',
]

__version__ = '1.0.0'

