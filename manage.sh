#!/usr/bin/bash
sudo echo "00 18 * * *   $(pwd)/covid_info.py" >> /var/spool/cron/$USER
python ~/covid_info.py