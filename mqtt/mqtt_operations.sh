#!/usr/bin/env bash
cd /home/xyz/venv/temp_impersonator/

source ./bin/activate
sudo python /home/xyz/practice/mqtt/MqttOperations.py --name subscriber --interpreter ./bin/python >/home/xyz/practice/mqtt/mqtt.log 2>/home/xyz/practice/mqtt/mqtt.log &
