#!/bin/sh
now=`date`
echo "Content-type: text/html"
echo ""
echo "<HTML>"
echo "<HEAD><TITLE>現在の時刻</TITLE></HEAD>"
echo "<BODY>"
echo "<H1>現在の時刻は</H1>"
echo "<H1><CENTER>$now </CENTER></H1>"
echo "<H1>です</H1>"
echo "</BODY>"
echo "</HTML>"