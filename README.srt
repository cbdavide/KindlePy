=========
KindlePy
=========

CLI to send files to your kindle email address, or any other email address.

Config:
--------
Set the sender email:

    kindlepy config --sender <email>

Set the receiver email:

    kindlepy config --receiver <email>

**In case any of the mails are not configured, the script will ask for them.**

Usage:
-------
Send files to the receiver direction:

    kindlepy send <file>...


Supported email services:
--------------------------
- Google (googlemail, gmail) - Requires to activate less secure apps.
- Microsoft (hotmail, outlook)
- Yahoo (yahoo)
- AOL (aol)
