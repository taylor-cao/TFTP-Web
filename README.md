# TFTP-Web

A web interface for TFTP servers.

[TFTP](http://de.wikipedia.org/wiki/Trivial_File_Transfer_Protocol) does not offer directory listing that allow for easy browsing. This is an interface providing html directory listings for a configurable TFTP server.

## Prerequisites

A TFTP server is expected to be running on the local machine.

### Fedora

Install it using yum:

    sudo yum install tftp-server
    
Configure it, by replacing `disable = yes` with `disable = no`:

    sudo nano /etc/xinetd.d/tftp

Turn TFTP on:

    sudo chkconfig tftp on

Turn xinetd on:

    sudo chkconfig xinetd on

Start xinetd:

    sudo service xinetd start

Test using tftp:

    sudo yum install tftp
    sudo touch /var/lib/tftpboot/test.txt
    tftp -4 localhost 69 -v -c get test.txt
    ls test.txt

## Requirements

-   [Python](http.//python.org)
-   [Bottle](http://bottlepy.org)

## Installing Requirements via pip

    sudo pip install -r requirements.txt

## Downloading

Clone this repository with git:

    git clone git@github.com:Bengt/TFTP-Web.git

## Configuring

Edit `TftpWeb.conf`:

    nano TftpWeb.conf

## Running

Start TFTP-Web with Python:

    python TftpWeb.py
    
## Using

Open in a web browser:

<http://localhost:8080>
    
## Limitations

-   ["Use of TFTP is strongly discouraged except in the most limited of circumstances where memory and CPU are at the highest premium."](http://tools.ietf.org/html/rfc3617#section-5)
-   TFTP-URLs can not be opened, because xdg-open does not support them.
