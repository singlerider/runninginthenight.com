---
layout: post
title:  "Decentralized Email over HAM Radio"
date:   2022-10-08 08:00:00 -0700
categories: ham hf radio
---

First of all, the instructions here are garbage:

https://github.com/la5nta/pat/wiki/ARDOP

From a newly-set-up copy of Ubuntu 22.04 LTS on a ThinkPad, I began from anew.

You will need to have USB access without `root` being required. So, before doing anything, might as well:

```shell
sudo usermod -a -G tty $USER
sudo usermod -a -G dialout $USER
```

Then, you should log out and log back in, but I recommend a full reboot. This will all you access to your `/dev/tty*` devices without requiring `sudo`.

The above-linked page links to https://www.cantab.net/users/john.wiseman/Documents/ARDOPC.html, which is supposed to tell you how to download `ardopc`. It only tells you the download link for a version that **DOES NOT WORK**:

```shell
~/ardop on  main [!?] 
➜ mv ~/Downloads/ardopc .

~/ardop on  main [!?] 
➜ chmod +x ardopc 

~/ardop on  main [!?] 
➜ ls -l
total 1112
-rwxrwxr-x 1 shane shane 521092 Oct  8 10:28 ardopc

~/ardop on  main [!?] 
➜ ./ardopc
zsh: no such file or directory: ./ardopc


```

What you _actually_ need is here:

https://www.cantab.net/users/john.wiseman/Downloads/ardopc64

```shell
~/ardop on  main [!?] 
➜ mv ~/Downloads/ardopc64 .

~/ardop on  main [!?] 
➜ chmod +x ardopc64

~/ardop on  main [!?] 
➜ ls -l
total 1112
-rwxrwxr-x 1 shane shane 587056 Oct  8 09:59 ardopc64

~/ardop on  main [!?] 
➜ ./ardopc64 
ardopc Version 1.0.4.1mBPQ-Debug5
ARDOPC listening on port 8515
Capture Devices

Card 0, ID `PCH', name `HDA Intel PCH'
  Device hw:0,0 ID `ALC257 Analog', name `ALC257 Analog', 1 subdevices (0 available)
Error -16 opening input device

Playback Devices

Card 0, ID `PCH', name `HDA Intel PCH'
  Device hw:0,0 ID `ALC257 Analog', name `ALC257 Analog', 1 subdevices (1 available)
    2 channels,  sampling rate 44100..48000 Hz
  Device hw:0,3 ID `HDMI 0', name `HDMI 0', 1 subdevices (1 available)
    2..8 channels, sampling rate 32000..192000 Hz
  Device hw:0,7 ID `HDMI 1', name `HDMI 1', 1 subdevices (1 available)
    2..8 channels, sampling rate 32000..192000 Hz
  Device hw:0,8 ID `HDMI 2', name `HDMI 2', 1 subdevices (1 available)
    2..8 channels, sampling rate 32000..192000 Hz
  Device hw:0,9 ID `HDMI 3', name `HDMI 3', 1 subdevices (1 available)
    2..8 channels, sampling rate 32000..192000 Hz
  Device hw:0,10 ID `HDMI 4', name `HDMI 4', 1 subdevices (1 available)
    2..8 channels, sampling rate 32000..192000 Hz

Using Both Channels of soundcard for RX
Using Both Channels of soundcard for TX
Opening Playback Device ARDOP Rate 12000
Opening Capture Device ARDOP Rate 12000

```

To configure `ardopc64`, first run:

```shell
~/ardop on  main [!?] 
➜ arecord -l
```

```
**** List of CAPTURE Hardware Devices ****
card 0: PCH [HDA Intel PCH], device 0: ALC257 Analog [ALC257 Analog]
  Subdevices: 1/1
  Subdevice #0: subdevice #0

```

Note card `0` and subdevice `0`. Based on that:

```shell
➜ echo 'pcm.ARDOP {type rate slave {pcm "plughw:0,0" rate 115200}}' > ~/.asoundrc
```

(Note `:0,0` above). My radio's baud is 115200. Not sure if this value matters too much, as it just maxes out to `12000`)

The next time you run `ardopc64`:

```shell
➜ ./ardopc64 
ardopc Version 1.0.4.1mBPQ-Debug5
ARDOPC listening on port 8515
Capture Devices

Card 0, ID `PCH', name `HDA Intel PCH'
  Device hw:0,0 ID `ALC257 Analog', name `ALC257 Analog', 1 subdevices (1 available)
    2 channels,  sampling rate 44100..192000 Hz

Card 1, ID `CODEC', name `USB Audio CODEC'
  Device hw:1,0 ID `USB Audio', name `USB Audio', 1 subdevices (1 available)
    1..2 channels, sampling rate 8000..48000 Hz

Playback Devices

Card 0, ID `PCH', name `HDA Intel PCH'
  Device hw:0,0 ID `ALC257 Analog', name `ALC257 Analog', 1 subdevices (1 available)
    2 channels,  sampling rate 44100..48000 Hz
  Device hw:0,3 ID `HDMI 0', name `HDMI 0', 1 subdevices (1 available)
    2..8 channels, sampling rate 32000..192000 Hz
  Device hw:0,7 ID `HDMI 1', name `HDMI 1', 1 subdevices (1 available)
    2..8 channels, sampling rate 32000..192000 Hz
  Device hw:0,8 ID `HDMI 2', name `HDMI 2', 1 subdevices (1 available)
    2..8 channels, sampling rate 32000..192000 Hz
  Device hw:0,9 ID `HDMI 3', name `HDMI 3', 1 subdevices (1 available)
    2..8 channels, sampling rate 32000..192000 Hz
  Device hw:0,10 ID `HDMI 4', name `HDMI 4', 1 subdevices (1 available)
    2..8 channels, sampling rate 32000..192000 Hz

Card 1, ID `CODEC', name `USB Audio CODEC'
  Device hw:1,0 ID `USB Audio', name `USB Audio', 1 subdevices (1 available)
    1..2 channels, sampling rate 32000..48000 Hz

Using Both Channels of soundcard for RX
Using Both Channels of soundcard for TX
Opening Playback Device ARDOP Rate 12000
Opening Capture Device ARDOP Rate 12000
ardopc listening on port 8515

```

You'll need hamlib utilities:

```shell
sudo apt-get install libhamlib-utils
```

Figure out which "rig" you have. You can use the following to list out available options.

```shell
rigctl -l
```

Mine is an IC-7300 ("rig" `3073`):

```shell
➜ rigctl -l | grep IC-7300
  3073  Icom                   IC-7300                 20210907.4      Stable      RIG_MODEL_IC7300

```

Now, you can use the `rigctld` (daemon) to access the USB interface to your radio:

```shell
➜ rigctld -m 3073 -r /dev/ttyUSB0 -s 115200

```

Just leave this running

In another tab, make sure you have `ardopc64` running as described above.

In another tab, double-check your `pat configuration`. Make sure you have your rig listed correctly as described here:

```json
  ...
  "hamlib_rigs": {
    "NAMEOFYOURRIG_CANBEANYTHING": {"address": "localhost:4532", "network": "tcp"}
  },
  ...
  "ardop": {
    "rig": "NAMEOFYOURRIG_CANBEANYTHING",
    "ptt_ctrl": false,
    "addr": "127.0.0.1:8515",
    "arq_bandwidth": {
      "Forced":false,
      "Max":500
    },
    "beacon_interval": 0,
    "cwid_enabled": true
  },
  ...

```

Note how I'm not using `localhost` in the ARDOP config. I am using `127.0.0.1`. Apparently, it's possible to have some IPV6 BS happen if you use `localhost`, so just skip that possibility.

Finally, assuming the rest of your `pat configure` is set up correctly, you're ready to run:

```shell
➜ pat http 
```

Everything will now work as you fully expect, and your computer's sound card will now act on behalf of your radio, making audio come out of your speakers. Have fun.