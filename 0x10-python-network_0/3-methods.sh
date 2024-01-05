#!/bin/bash
# curl only methods
curl -sI "$1" | sed -n '/Allow: /s/Allow: //p'
