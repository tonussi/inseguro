#!/bin/bash

FILE=$1
YOURKEY=$2

sign() {
  for line in $(cat $FILE); do
    echo "$USER - $(date +"%x %r %Z"):"

    gpg --keyserver pgp.mit.edu --search-keys $line
    gpg -u $YOURKEY --sign-key $line
    gpg --armor --export $line > keys/$line.asc
    gpg --keyserver pgp.mit.edu --recv-key $line
    gpg --keyserver pgp.mit.edu --send-key $line
  done

  exit 1
}

email() {
  cd keys
  ls
}

if [ $# -lt 2 ]; then
  echo "example: sh sign.sh keys.txt {your_key}"
else
  # sign
  email
fi
