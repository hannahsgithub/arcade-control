# Raspberry Pi Controls Integration

This project integrates an analog joystick (from the SunFounder DaVinci Kit) with Raspberry Pi's GPIO pins and can output five different control commands.

## Features

- Connect and interface an analog joystick with Raspberry Pi.
- Python program that maps joystick outputs to your game controls.
- Communication mechanism using Python and the Socket library for transmitting, receiving, and decoding control signal for the client-end.

- ![pi](https://github.com/hannahsgithub/arcade-control/assets/122186988/129a143d-2c42-434f-a329-996a548293ac)

## Requirements

- Raspberry Pi (any model)
- Analog joystick 
- Any client device to deploy the game
- IDE for Python on both Raspberry Pi and client

## Installation

1. Clone the repository to your Raspberry Pi (`pi.py`) and client device (`pc.py`). For Pi, also clone `ADC0834.py`.
2. Install the required dependencies and ensure Raspberry Pi is up to date
3. Connect the analog joystick to the GPIO pins according to the pin mapping in the `pi.py` file, or however you'd like.
4. Set up your game on the client device
5. Configure game controls within the code (default set to W A S D)
6. Configure your IP address within the code

## Usage

1. Run the Python program on both client and Raspberry Pi
2. Enjoy playing your game using your diy joystick!
