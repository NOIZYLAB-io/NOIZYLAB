#!/bin/bash
# Boot ritual for NoizyWind Ritual Pack

noizy_kernel --init
voice_trigger_daemon --listen
overlay_renderer --launch planar_eyelevel.html
capsule_daemon --schedule weekly
agent_broker --infuse sequoia
ambient_loop_engine --play charged_loop.wav
slablink_sync --push Capsule_20250929.zip
resurrection_protocol --monitor NOIZYWIND
