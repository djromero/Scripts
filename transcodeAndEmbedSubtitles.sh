#!/bin/sh
# 
# Transcode a video to watch on iPad with embedded soft subtitles.
#
# See https://trac.handbrake.fr/wiki/CLIGuide
#

HandBrakeCLI=/Applications/HandBrake.app/Contents/MacOS/HandBrakeCLI
SRT_LANG=spa
PRESET=iPad

if [ $# -ne 2 ]
then
    echo $0 '<video> <subtitle>'
    exit 1
fi

if [ ! -x $HandBrakeCLI ]
then
    echo Missing HandBrakeCLI
    exit 2
fi

video=$1 && shift
subtitle=$1 && shift

$HandBrakeCLI -i "$video" -o "${video}.output.mp4" --preset $PRESET --srt-file "${subtitle}" --srt-lang $SRT_LANG
exit $?

