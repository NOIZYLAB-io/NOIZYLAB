#!/bin/zsh
# Launch all 96 agent .app bundles for Bobby in parallel

AGENT_ROOT="/Users/rsp_ms/Documents/_THE_Aquarium/_projects/NoizyFish/BigBubba/FinalApps"

for i in {01..96}
 do
    open "$AGENT_ROOT/Agent $i.app" &
done

wait

echo "All 96 agents launched."
