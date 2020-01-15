#!/bin/bash

go build buildflow.go
./buildflow
python put.py

