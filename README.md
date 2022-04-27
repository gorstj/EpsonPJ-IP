# EpsonPJ-IP

Needed a way to control my TW7100 (likely works with TW7000 and other) with an ELPAP10 USB wifi card to aid home automation (rather than use IR)

Usage:

EpsonPJ-IP.py on

EpsonPJ-IP.py off

Beware - I am not a programmer and can not vouch for reliability or efficiency of this script (but works for me!)

Just change the IP address to your own (and ensure you are using static IP or assigned DHCP lists on yoru router). There is no need to add a password to the script (as I don't think it is possible to change)

This works by hijacking the web page that the official Epson mobile app iProjection uses to control the projector. Sadly, there is no discrete on off button. Hence the IF statements to check if the web page is indicating if the projector is in standby or not. Even when the projector is warming up there is a delay before the web page indicates that the projector is on which may lead to inconsistancy.

Heavily adapted and credit to https://gist.github.com/0x4C4A/645b7a97281d624d88e29fcd7330fd75 and https://www.avsforum.com/threads/official-epson-5040ub-6040ub-owners-threa>


