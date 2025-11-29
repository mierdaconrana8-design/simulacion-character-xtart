#!/usr/bin/env bash
set -e

export DEBIAN_FRONTEND=noninteractive

apt-get update -y
apt-get upgrade -y

apt-get install -y xubuntu-desktop lightdm python3 python3-pip python3-venv

cp /vagrant/aventura.py /home/vagrant/aventura.py
chown vagrant:vagrant /home/vagrant/aventura.py
chmod +x /home/vagrant/aventura.py

sudo -u vagrant bash -lc "python3 -m venv /home/vagrant/venv"
sudo -u vagrant bash -lc "/home/vagrant/venv/bin/pip install --upgrade pip"

cat > /etc/systemd/system/aventura.service <<'EOF'
[Unit]
Description=Aventura Conversacional
After=network.target

[Service]
Type=simple
User=vagrant
WorkingDirectory=/home/vagrant
ExecStart=/home/vagrant/venv/bin/python /home/vagrant/aventura.py
Restart=on-failure
Environment=TERM=xterm-256color

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable aventura.service

echo "Instalación lista. Usa: sudo systemctl start aventura.service"
