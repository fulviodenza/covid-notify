#!/usr/bin/bash
cp covid_info.py ~
sudo chmod +x covid_info.py
nohup python ~/covid_info.py &
