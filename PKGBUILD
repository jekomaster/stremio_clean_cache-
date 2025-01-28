# Maintainer: Your Name <your-email@example.com>
# Package: stremio-cache-cleaner
# Version: 1.0.0
# Description: Python app to clean Stremio cache

pkgname=stremio-cache-cleaner
pkgver=1.0.0
pkgrel=1
pkgdesc="A Python app to clean Stremio cache"
arch=('any')
url="https://github.com/yourusername/stremio-cache-cleaner"
license=('MIT')
depends=('python' 'libnotify' 'dunst') # Add any additional dependencies
makedepends=('python-pip' 'python-virtualenv') # To ensure virtualenv is installed during build
source=('clean_stremio_cache.py' 'requirements.txt' 'purge_stremio_cache.desktop')
sha256sums=('SKIP' 'SKIP' 'SKIP') # You can skip checksums or generate them for security purposes

build() {
  # Optionally, set up a virtual environment
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
}

package() {
  # Install the application files
  mkdir -p "$pkgdir/usr/bin"
  cp -r * "$pkgdir/usr/bin/"
  # Optionally, install the .desktop file if you want a launcher
  install -Dm644 purge_stremio_cache.desktop "$pkgdir/usr/share/applications/purge_stremio_cache.desktop"
  # Install the script to the bin folder
  install -Dm755 clean_stremio_cache.py "$pkgdir/usr/bin/clean_stremio_cache"
}
