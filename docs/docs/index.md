# Bauer_Mesa8418_Week3 documentation!

## Description

Uploading and manipulating data with git, CCDS, and S3

## Commands

The Makefile contains the central entry points for common tasks related to this project.

### Syncing data to cloud storage

* `make sync_data_up` will use `aws s3 sync` to recursively sync files in `data/` up to `s3://bauer-mesa8418-week3/data/`.
* `make sync_data_down` will use `aws s3 sync` to recursively sync files from `s3://bauer-mesa8418-week3/data/` to `data/`.


