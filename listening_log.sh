#!/bin/zsh
find ~/Desktop/MobileLearning -name "*.mp3" -exec stat -f "%Sm %N" {} + >> ~/SleepLearning_AppleTechCourse/listening_log.txt
