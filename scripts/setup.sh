#!/bin/bash
bash scripts/build_base.sh
bash scripts/build.sh
mkdir model
bash scripts/save_model.sh