#!/bin/bash

case "$1" in 

'start')
	cat /usr/share/audio/at_your_service.au > /dev/audio
	;;
'end')
	cat /usr/share/audio/oh_no_not_again.au > /dev/audio
	;;
esac
exit 0
