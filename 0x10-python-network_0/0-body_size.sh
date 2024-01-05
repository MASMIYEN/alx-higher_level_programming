#!/bin/bash
#curl body size
curl -sw '%{size_download}\n' "$1" -o /dev/null | awk '{print $1}'
