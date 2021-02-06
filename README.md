# PiOlimex
Dotfiles to improve olimex ergonomy

Required arborescence :

```
/home/pi
      ├── data
      └── eeg
          ├── blink.py
          ├── build.sh
          ├── eeg.o
          ├── eeg_reader.cpp
          ├── openeeg.so
          ├── plot.gpi
          ├── poweroff.py
          ├── processor.py
          ├── run_eeg.sh
          └── setuptty.sh
```

The modified files are the ones provided here.

To use `blink.py` and `poweroff.py`, you need to plug a LED to pin 17 and ground on the pi. Otherwise you can remove the lines in `run_eeg.sh`.

The auto recording and auto shutdown is made through a systemd service:
1. Create a file at `/etc/systemd/system/eeg.service` containing or copy the one from the repository:

```text
[Unit]
Description=Start recording with Olimex EEG

[Service]
User=pi
WorkingDirectory=/home/pi/eeg
ExecStart=/home/pi/eeg/run_eeg.sh
Restart=never

[Install]
WantedBy=multi-user.target
```
2. Reboot or run `systemctl daemon-reload` as root
3. Enable the service to start it on boot using `systemctl enable eeg.service` as root
