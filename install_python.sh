#!/usr/bin/env bash
# install_python.sh
# Downloads the official Python installer from python.org and installs it
# silently on macOS or Windows (run from Git Bash / MSYS / Cygwin).
# No Homebrew, winget or Chocolatey needed - only an internet connection.
#
# Usage: bash install_python.sh
# Change PY_VERSION below to install a different release.

set -euo pipefail

PY_VERSION="3.13.17"
BASE_URL="https://www.python.org/ftp/python/${PY_VERSION}"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

log()  { printf '\033[1;34m[install_python]\033[0m %s\n' "$*"; }
fail() { printf '\033[1;31m[install_python] ERROR:\033[0m %s\n' "$*" >&2; exit 1; }
have() { command -v "$1" >/dev/null 2>&1; }

download() {
  local url="$1" out="$2"
  log "Downloading $url"
  if have curl; then
    curl -fL --progress-bar "$url" -o "$out"
  elif have wget; then
    wget -q --show-progress "$url" -O "$out"
  else
    fail "Neither curl nor wget found."
  fi
}

# Skip if a usable Python 3 is already present
if have python3 && python3 --version >/dev/null 2>&1; then
  log "Python already installed: $(python3 --version)"
  exit 0
fi
if have python && python --version 2>&1 | grep -q "Python 3"; then
  log "Python already installed: $(python --version)"
  exit 0
fi

OS="$(uname -s)"
ARCH="$(uname -m)"

case "$OS" in
  Darwin)
    log "Detected macOS ($ARCH)"
    PKG="python-${PY_VERSION}-macos11.pkg"   # universal installer (Intel + Apple Silicon)
    download "${BASE_URL}/${PKG}" "${TMP_DIR}/${PKG}"
    log "Installing (sudo password required)..."
    sudo installer -pkg "${TMP_DIR}/${PKG}" -target /
    log "Installed: $(/usr/local/bin/python3 --version 2>/dev/null || echo 'open a new terminal and run python3 --version')"
    ;;

  MINGW*|MSYS*|CYGWIN*)
    log "Detected Windows ($ARCH)"
    case "$ARCH" in
      aarch64|arm64) EXE="python-${PY_VERSION}-arm64.exe" ;;
      *)             EXE="python-${PY_VERSION}-amd64.exe" ;;
    esac
    download "${BASE_URL}/${EXE}" "${TMP_DIR}/${EXE}"
    log "Installing silently (adds Python to PATH, current user only)..."
    # Run via cmd so the installer finishes before the script continues
    WIN_PATH="$(cygpath -w "${TMP_DIR}/${EXE}")"
    cmd //c "\"${WIN_PATH}\" /quiet InstallAllUsers=0 PrependPath=1 Include_test=0"
    log "Installed. Close and reopen your terminal, then run: python --version"
    ;;

  Linux)
    fail "Linux detected. This script supports macOS and Windows only."
    ;;

  *)
    fail "Unsupported OS: $OS"
    ;;
esac

log "Done."