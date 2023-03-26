# Clone Zigbee2MQTT repository
sudo wget http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key
sudo apt-key add mosquitto-repo.gpg.key
cd /etc/apt/sources.list.d/
sudo wget http://repo.mosquitto.org/debian/mosquitto-jessie.list
sudo apt-get update
sudo apt-get install mosquitto
sudo git clone --depth 1 https://github.com/Koenkk/zigbee2mqtt.git opt/zigbee2mqtt
sudo chown -R pi:pi opt/zigbee2mqtt

# Enter folder
cd opt/zigbee2mqtt

# Install python env
python3 -m venv .

# Activate environment
source opt/zigbee2mqtt/bin/activate

# Upgrade pip, wheel and setuptools
pip install --upgrade pip wheel setuptools

# Install node environment
pip install nodeenv

# Init node environment
nodeenv -p -n 16.15.0

# Deactivate and activate environment to be sure
deactivate
source opt/zigbee2mqtt/bin/activate

# Install dependencies
cd opt/zigbee2mqtt
npm ci

# Deactivate environment
deactivate