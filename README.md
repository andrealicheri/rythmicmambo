# RYTHMICMAMBO

A simple browser-info logger. HTMX x Plain JS on the frontend, Flask on the backend.

## Why?

Mostly to scare your friends.

This is not a revolutionary PoC, many other tools (such as BeEF) can already do this and more,
however this tool is intended to feel lightweight and easy to setup.

Also, it was of great help to kickstart my JS development. I have used JS before, but I mostly
copy-pasted stuff and hack it by instinct.

## Usage and requirements

Python 3.11.x or higher is required, as the config uses type generics.

To run:

    python utils.py -s

If you want to use ngrok or any other tunneling service, set `isTunnel` to `True` and `ipAddress` to your subdomain name

# Credits
Credits go to fingerprint.js and BeEF for some clear examples on how to handle browsers' APIs