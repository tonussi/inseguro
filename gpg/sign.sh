#!/bin/bash

FILE=$1
YOURKEY=$2
YOURSERVER=$3

sign() {
  for line in $(cat $FILE); do
    echo "$USER - $(date +"%x %r %Z"):"

    gpg --keyserver ${YOURSERVER} --search-keys $line
    gpg -u $YOURKEY --sign-key $line
    gpg --armor --export $line > keys/$line.asc
    gpg --keyserver ${YOURSERVER} --send-key $line
    gpg --keyserver ${YOURSERVER} --recv-key $line
  done

  exit 1
}

email() {
  cd keys
  ls
}

if [ $# -lt 3 ]; then
  echo "example: sh sign.sh keys.txt {your key} {your server}"
else
  sign
  email
fi
