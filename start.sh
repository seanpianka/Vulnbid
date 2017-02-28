#!/bin/bash
if [ "$1" == "--debug" ]; then
    echo "[*] Starting debug server"
    pushd `dirname $0` > /dev/null
    SCRIPTPATH=`pwd`
    popd > /dev/null
    python $SCRIPTPATH/vulnbid.py
else
    echo "[*] Starting production server (use --debug for development server)"
    uwsgi --ini vulnbid.ini
fi
