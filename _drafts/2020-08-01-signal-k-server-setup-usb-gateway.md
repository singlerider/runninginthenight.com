---
layout: post
title:  "Setting Up A Signal K Server with a USB Gateway"
date:   2020-08-01 20:30:00 -0700
categories: signalk nmea2000
---

# Preface

[NMEA 2000](https://en.wikipedia.org/wiki/NMEA_2000) is a useful protocol.

The ability to bridge multiple, diverse, arbitrary sensors from multiple manufacturers gives hacker-types like me ideas for building out applications based on data that may be available.

The only problem is the data provided by NMEA 2000 isn't quite accessible from the start. "Messages" sent from the network come across through a protocol known as [CAN Bus](https://en.wikipedia.org/wiki/CAN_bus). You need an interface to translate into something that's usable.

# Options

There are a number of all-in-one options to handle these sorts of translations. The [iKommunicate](https://ikommunicate.com/) creates a webserver accessible from any device with a local network colnnection. At $300 (at the time of writing), that's a bit expensive for something that is merely a middle-man. The real draw is convenience — attach the iKommunicate to the network's backbone via a drop cable, plug in your device (computer) to the supplied ethernet port and you're off to the races, ready to use JSON data via the open source [Signal K](https://signalk.org/) protocol.

Introducing alternative gateways to achieve the same result. Both of these devices are around $190 (at the time of writing) and convert the NMEA 2000 drop cable connection to a USB plug for a computer:

## [Digital Yacht iKonvert](https://digitalyachtamerica.com/product/ikonvert/)

I previously tried the Digital Yacht version. I had an excellent experience with their customer service staff, but in the end, the iKonvert wasn't able to provide me with data.

## [Yacht Devices YDNU-02](https://www.yachtd.com/products/usb_gateway.html)

 I decided to go with the YDNU-02. I didn't realize when I purchased it that it ships from Russia and would be caught up in customs for nearly two months. But, now that I have it, I'll explain how I got it running.

# Setup

I performed these on Linux, but a translation to MacOS or Windows wouldn't be hard to find.

## Current Network

- B&G Wireless Wind Instrument
- Garmin Steadycast Heading Sensor
- Raymarine AXIOM 7 DV Multifunction Display (GPS)
- Standard Horizon GX6000 (AIS Receiver)

## Gateway Preparation

The YDNU-02, as shipped from Yacht Devices does not arrive in a configuration that is compatible with Signal K. The mode will need to be changed to `RAW`. This is the biggest hurdle I ran into to get this process going.

See [this Issue on GitHub](https://github.com/SignalK/signalk-server-node/issues/1090#issuecomment-667598345) to learn how to perform this step.

## Signal K Server

The following instructions require an installation of [Node JS](https://nodejs.org/en/).

I decided to `clone` the source code from the [Signal K Node Server Repository](https://github.com/SignalK/signalk-server-node/tree/c1ddf33da76da8ce4f4b442dd7f19c45ff3f8ffd) (c1ddf33da76da8ce4f4b442dd7f19c45ff3f8ffd was the latest commit when I did this):

```shell
$ git clone https://github.com/SignalK/signalk-server-node.git
$ cd signalk-server-node
```

When cloning from source, the repository's directions are a bit vague. Here are the steps I performed:

```shell
$ npm install --unsafe-perm
$ npm run build
$ npm install serialport --unsafe-perm # very important
$ cd bin
$ ./signalk-server-setup
```

After performing that step, I chose the `~/.signalk` directory for my project settings to live. To launch `signalk-server`:

```shell
$ cd ~/.signalk
$ ./signalk-server
```

You can then launch the dashboard at <http://localhost:3000>.

### Dashboard Setup

Click the "Login" button in the upper-right to create an admin user. Immediately after doing so, log in as that admin user. You'll now see more options in the left navigation bar. Select the option shown in the following screenshot:

![Server Connection Location](/assets/images/signalk-setup/server-connection-location.png)

After you're on that page, make sure your configuration resembles the following:

![Server Connection Location](/assets/images/signalk-setup/server-connection-configuration.png)

Click "Apply," then restart the server.

### Data

All of a sudden, I get beautiful data from <https://localhost:3000/signalk/v1/api/>:

```json
{
  "vessels": {
    "urn:mrn:signalk:uuid:2819432c-ed0a-4a9f-a2cd-47c4412d72f0": {
      "uuid": "urn:mrn:signalk:uuid:2819432c-ed0a-4a9f-a2cd-47c4412d72f0",
      "navigation": {
        "headingMagnetic": {
          "meta": {
            "units": "rad",
            "description": "Current magnetic heading of the vessel, equals 'headingCompass adjusted for magneticDeviation'"
          },
          "value": 1.0301,
          "$source": "usb-gateway.0",
          "timestamp": "2020-08-02T00:40:46.607Z",
          "pgn": 127250
        },
        "magneticDeviation": {
          "meta": {
            "units": "rad",
            "description": "Magnetic deviation of the compass at the current headingCompass"
          },
          "value": 0,
          "$source": "usb-gateway.0",
          "timestamp": "2020-08-02T00:40:46.607Z",
          "pgn": 127250
        },
        "position": {
          "meta": {
            "description": "The position of the vessel in 2 or 3 dimensions (WGS84 datum)"
          },
          "value": {
            "longitude": -122.3156456,
            "latitude": 37.8665382
          },
          "$source": "usb-gateway.3",
          "timestamp": "2020-08-02T00:40:46.674Z",
          "pgn": 129025
        },
        "magneticVariation": {
          "meta": {
            "units": "rad",
            "description": "The magnetic variation (declination) at the current position that must be added to the magnetic heading to derive the true heading. Easterly variations are positive and Westerly variations are negative (in Radians)."
          },
          "value": 0.2313,
          "$source": "usb-gateway.3",
          "timestamp": "2020-08-02T00:40:46.086Z",
          "pgn": 127258
        },
        "speedOverGround": {
          "meta": {
            "units": "m/s",
            "description": "Vessel speed over ground. If converting from AIS 'HIGH' value, set to 102.2 (Ais max value) and add warning in notifications"
          },
          "value": 0,
          "$source": "usb-gateway.3",
          "timestamp": "2020-08-02T00:40:46.558Z",
          "pgn": 129026
        },
        "courseOverGroundTrue": {
          "meta": {
            "units": "rad",
            "description": "Course over ground (true)"
          },
          "value": 3.6615,
          "$source": "usb-gateway.3",
          "timestamp": "2020-08-02T00:40:46.558Z",
          "pgn": 129026
        },
        "datetime": {
          "meta": {
            "description": "Time and Date from the GNSS Positioning System"
          },
          "value": "2020-08-02T00:40:46.17700Z",
          "$source": "usb-gateway.3",
          "timestamp": "2020-08-02T00:40:46.360Z",
          "pgn": 126992
        },
        ...
        "trip": {
          "log": {
            "meta": {
              "units": "m",
              "description": "Total distance traveled on this trip / since trip reset"
            },
            "value": 0,
            "$source": "usb-gateway.3",
            "timestamp": "2020-08-02T00:40:46.673Z",
            "pgn": 128275
          }
        },
        "log": {
          "meta": {
            "units": "m",
            "description": "Total distance traveled"
          },
          "value": 0,
          "$source": "usb-gateway.3",
          "timestamp": "2020-08-02T00:40:46.673Z",
          "pgn": 128275
        }
      },
      "environment": {
        "wind": {
          "speedApparent": {
            "meta": {
              "units": "m/s",
              "description": "Apparent wind speed"
            },
            "value": 3.52,
            "$source": "usb-gateway.1",
            "timestamp": "2020-08-02T00:40:46.642Z",
            "pgn": 130306
          },
          "angleApparent": {
            "meta": {
              "units": "rad",
              "description": "Apparent wind angle, negative to port"
            },
            "value": 3.0193,
            "$source": "usb-gateway.1",
            "timestamp": "2020-08-02T00:40:46.642Z",
            "pgn": 130306
          }
        }
      }
    }
  },
  ...
}
```

You're now ready to make whatever you'd like with this data. Stay tuned to see what I have planned for it.
