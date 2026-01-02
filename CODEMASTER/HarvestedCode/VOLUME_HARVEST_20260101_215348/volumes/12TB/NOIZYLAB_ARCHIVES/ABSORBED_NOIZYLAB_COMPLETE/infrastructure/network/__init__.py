#!/usr/bin/env python3
"""
NoizyLab Network Monitoring Package
====================================
DGS1210 network agent with automatic device detection and handshake
"""

from .dgs1210_network_agent import DGS1210Agent, ConnectedDevice, HandshakeResult

__all__ = [
    'DGS1210Agent',
    'ConnectedDevice',
    'HandshakeResult',
]

__version__ = '1.0.0'

