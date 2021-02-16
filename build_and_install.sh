set -e
sudo apt remove autodnd -y || echo ''
cd package
debuild -b -uc -us
cd ..
sudo dpkg -i autodnd_*_amd64.deb
rm autodnd_*