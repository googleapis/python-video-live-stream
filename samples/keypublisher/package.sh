#!/bin/bash

# Creates a zip archive of all files needed to run the key publisher.
# To run, just execute the script: `./package.sh`

set -e

CWD=$(pwd)
SRC_DIRECTORY=$(dirname "$0")
ZIP_DIR="/tmp/gcp_livestream_key_publisher"
OUTPUT_FILE="${CWD}/gcp_livestream_key_publisher_GENERIC_CONFIDENTIAL.zip"

if [[ -e "${OUTPUT_FILE}" ]]; then
  echo "File ${OUTPUT_FILE} already exists"
  exit 1
fi

cd "${SRC_DIRECTORY}"
mkdir "${ZIP_DIR}"
cp main.py main_test.py README.md api-config.template.yml requirements.txt "${ZIP_DIR}/"

mkdir "${ZIP_DIR}/clients"
cp clients/*.py "${ZIP_DIR}/clients/"
rm ${ZIP_DIR}/clients/keyos*

#mkdir "${ZIP_DIR}/third_party"
#cp third_party/*.py "${ZIP_DIR}/third_party/"

cd "$(dirname "${ZIP_DIR}")"
zip -r "${OUTPUT_FILE}" "$(basename "${ZIP_DIR}")"
rm -rf "${ZIP_DIR}"

echo "Successfully exported as ${OUTPUT_FILE}"
