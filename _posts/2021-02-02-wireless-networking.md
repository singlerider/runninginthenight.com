---
layout: post
title:  "Wireless Networking on a Sailboat"
date:   2021-02-02 13:00:00 -0700
categories: wifi 4g lte wireless internet
---

Wireless Networking on a Sailboat
=================================

# Abstract

Network connection is a common thing today's sailor wants while out on the water for longer periods. The problem of cell coverage and available signal often arises when in a marina or even when going below deck.

# 4G LTE

There's an answer for those problems above and it runs off DC power.

[LTE Fix](https://ltefix.com/) has an excellent series of guides and a highly-knowledgable support staff that can answer questions from compatibility all the way to expected power consumption.

I used their guides located at [LTE Hacks](https://ltehacks.com/), including this one for gettings started — [Introduction to Building and Configuring a WiFiX/GoldenOrb/ROOter Cellular Router](https://ltehacks.com/viewtopic.php?f=21&t=74).

## Breakdown

The following segments are how I built my unit in the summer of 2020 and the best options will likely have changed by the time you read this.

I use [Google Fi](https://fi.google.com/) with my setup, with their "unlimited" plan, which offers 22GB per month of full-speed, unencumbered data, where after that quota, data speed is capped at 32KB per second, per device. The SIM that's in the modem is a data-only sort without the capability of dialing out with a phone number like a standard SIM. I share that card on the same plan as my primary phone.

A good reason to use Fi is it allows (mostly) seamless transitions across countries, which can be an asset on a boat when moving from one port to another. But it also piggybacks on T-Mobile and Sprint's antennas (in the US), giving a higher likelihood of getting a signal by any nearby towers. If you're in some faraway land, it will automatically use that area's agreed-upon network without the end-user having to do a thing.

## Parts

The total cost I incurred for parts for this build was $520, including enclosure and antennas.

[![Router Parts](/assets/images/wireless-networking/cart.jpg)](https://photos.app.goo.gl/mVsBZHrULkfTYPmJ6)

### Modem and Router

This is where you don't want to go too cheap. Buying the right modem can make a big difference in the maximum potential speed you'll see for downloading and uploading.

I chose this router because for a 36-foot vessel, I didn't need to broadcast a signal across the Bay.

- Sierra Wireless EM7565 CAT-12 LTE-A Pro Modem
- NEXQ6GO Cellular WiFi Router - NEXQ6GO-M

### Enclosure

Marine environments are harsh. Keep your router, modem, and DC to DC converter in a completely-enclosed area to keep it going as long as possible.

The WiFiX enclosure comes with poor-quality galvanized fasteners to keep the top and bottom of the fixture held together. I would recommend getting some 304 stainless M4 x 40mm flathead machine screws to make sure they won't ever disintegrate from salty sea air and rainwater.

I decided to go the extra mile and mount the enclosure directly underneath my radar assembly (photo at the end of the post).

- WiFiX Medium Router PCB Enclosure Kit

### Antennas

The antennas need to be placed at least a few feet apart to give better signal and the higher up they go, the better your signal will be.

- (2) Wilson Electronics 9.88-inch 4G Wide Band Omni-Directional Marine Antenna w/ SMA Male Connector

### Miscellaneous

- Mini PCI-E to M.2 (NGFF) Key B Adapter with Top SIM Card Slot
- (2) Shakespeare Antenna Mount Nylon Ratchet
- DC Voltage Converter Automatic Buck Boost Converter DC 8V-40V to 12V 3A

### Cables

- Proxicast 6 ft Low-Loss Coax Jumper Cable (50 Ohm) - N Male to N Male
- 8dBi WiFi RP-SMA Male Antenna 2.4GHz 5.8GHz Dual Band
- U.FL to SMA M.2 NGFF UFL to SMA Female MHF4 IPX4 IPEX4 Ipex Connector Pigtail WiFi Antenna Extension Cable
- SMA Adapter SMA Male to RP SMA Female Jack Connector for RF Coax Cable Wi-Fi

## Wiring

[![Router Parts](/assets/images/wireless-networking/parts.jpg)](https://photos.app.goo.gl/14t1E3D6BpBkMLdPA)

I have a 12V lithium bank. From there, I have a 12V DC to DC converter to keep the voltage to the modem nice and smooth.

The power draw is a smooth __0.1 amps at 12V__.

# Closing

[![Assembled System 1](/assets/images/wireless-networking/installation-1.jpg)](https://photos.app.goo.gl/SrXHhLtKfQMZFh2t9)
[![Assembled System 2](/assets/images/wireless-networking/installation-2.jpg)](https://photos.app.goo.gl/ioRggJyWn5RXzcD3A)

## Results

Results depend on time of day, tides (height of the boat relative to shore), and a few other things.

A one-to-one test from inside my insulated cabin showed the following results:

### Installation

Ping: 44
Download (Mbps): 8.95
Upload (Mbps): 8.14

### Pixel 4a on LTE

Ping: 45
Download (Mbps): 1.89
Upload (Mbps): 0.42

## Need Some Help?

If you decide to make something like this, send me an email and I'll help you out for free.
