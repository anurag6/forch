#!/bin/bash
# Should be run through go/benz

set -eux

cd git/benz-build-source
sudo kokoro/setup.sh
sudo apt-get install tree

echo "${TMPDIR}"
mkdir -p "${TMPDIR}/binary/"
mkdir -p "${TMPDIR}/glinux-build"

FAUCET_VERSION=$(< etc/FAUCET_VERSION)
echo Fixing debian faucet version to $FAUCET_VERSION
fgrep -v $FAUCET_VERSION debian/control > /dev/null
sed -i s/FAUCET_VERSION/${FAUCET_VERSION}/ debian/control
fgrep $FAUCET_VERSION debian/control

VERSION=$(git describe)
debchange --newversion $VERSION -b "New upstream release"

# Write version content to __version__.py
cat >forch/__version__.py <<VER_FILE
"""Forch version file"""

__version__ = '$VERSION'
VER_FILE

cat forch/__version__.py

glinux-build -type="binary" -base-path="${TMPDIR}/glinux-build" -additional-repos="enterprise-sdn-faucet-core-unstable" -name="rodete" . "${TMPDIR}/binary/"

if [ -f esdn-faucet/FORCH_VERSION ]; then
    echo Pollution from esdn-faucet should not be here.
    false
fi

(
    echo Starting build of esdn-faucet meta-package...

    git add debian
    git stash
    git checkout esdn
    git log -n 1
    cd esdn-faucet

    FORCH_VERSION=$(< FORCH_VERSION)
    echo Fixing debian forch version to $FORCH_VERSION
    fgrep -v $FORCH_VERSION debian/control > /dev/null
    sed -i s/FORCH_VERSION/${FORCH_VERSION}/ debian/control
    fgrep $FORCH_VERSION debian/control

    VERSION=$(git describe)
    echo esdn-faucet version $VERSION
    debchange --newversion $VERSION -b "New upstream release"

    glinux-build -type="binary" -base-path="${TMPDIR}/glinux-build" -additional-repos="enterprise-sdn-faucet-core-unstable" -name="rodete" . "${TMPDIR}/binary/"
)

mkdir binary
cp ${TMPDIR}/binary/* binary/
ls -l binary/