#!/bin/bash
# Send a GET request to a given URL with a header variable.
# curl -sH "X-HolbertonSchool-User-Id: 98" "${1}"
if [ $# -eq 0 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

url=$1
header="X-HolbertonSchool-User-Id: 98"
curl -X GET -H "$header" "$url"
