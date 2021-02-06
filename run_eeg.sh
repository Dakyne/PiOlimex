#!/bin/bash
recorder="sleepi"

while true ; do
    ls /dev/ttyUSB0 &> /dev/null
    if (( $? == 0 )) ; then
        echo -e "Found /dev/ttyUSB0"
        break
    fi
    ls /dev/ttyUSB1 &> /dev/null
    if (( $? == 0 )) ; then
        echo -e "Found /dev/ttyUSB1\nRestarting…"
        sudo shutdown -r now
    fi
    sleep 1
done
~/eeg/setuptty.sh
echo "START using SleePi"
ls /home/pi/data/record.dat &> /dev/null
if (( $? == 0 )) ; then
    mv /home/pi/data/record.dat /home/pi/data/$(date +"%Y-%m-%d_%H:%M:%S").dat
fi
./blink.py &
~/eeg/processor.py &
while true ; do
    ls /dev/ttyUSB0 &> /dev/null
    if (( $? != 0 )); then
        echo -e "Stop recording"
        break
    fi
    sleep 1
done
pkill blink.py
cut -d ' ' -f-2 /home/pi/data/record.dat > /home/pi/data/record.tmp && mv /home/pi/data/record.tmp /home/pi/data/record.dat
./poweroff.py
sudo shutdown now
