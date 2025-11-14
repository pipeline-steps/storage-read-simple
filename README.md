
# gs-extract

## Description

This pipeline step reads a file from a gcs bucket and stores it locally. 

## Parameters

| Name           | Type    | Mandatory | Description                                                             |
|----------------|---------|-----------|-------------------------------------------------------------------------|
 | bucket         | String  | X         | name of the bucket                                                      |
 | path           | String  | X         | path (directory) within the bucket                                      |
 | filename       | String  | X         | filename of the bucket object                                           |
 | outputFile     | String  | X         | name of the local output file                                           |


