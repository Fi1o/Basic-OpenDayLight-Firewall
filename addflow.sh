#!/bin/bash

go build buildflow.go
./buildflow
python cliBase.py

