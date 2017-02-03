# Blog Post API Assignment

To Install this api you need to clone from the  Github repository.
Once you have cloned the files you need to run setupapi.pl from the command line.
This file will ensure you have the perl modules needed and if not it will tell you what you need and how to install it.
The setup api also configures apache2 for cgi and the directory /opt/mas
Once that is setup it chowns the directory so that it can be read by apache to run the files.

The url that you will be using for the GET is blogapi/blogapi.cgi

The url for the POST is blogapi/bloginput.cgi

At this time the post takes a json file from the directory and puts it into the DB.

