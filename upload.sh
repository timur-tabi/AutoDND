set -e
cd package
debuild -S
cd ..
dput ppa:isola/autodnd autodnd_*_source.changes
rm autodnd_*