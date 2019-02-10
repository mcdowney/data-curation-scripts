# data-curation-scripts
Tiny, garbage scripts for data clean-up and curation

## file2folder (Ruby)
For each file in a directory, creates a new sub-directory using the filename minus the file extension, and moves that file into the new sub-directory. Will sort files with same file names and different extensions into the same file directory. Generally used to arrange files into DUL DDR standard ingest format, where one file is one item.

## fileSorter (Ruby)
Don't remember what this is used for

## fileBatcher (Ruby)
Can be used to create smaller batches from large groups of files (i.e., as with DUL Radio Haiti project). Takes a csv with a list of desired files and copies those files to a new directory.

## mets2csv (Python)
Used to extract element values from the descriptive metadata section of a directory of METS XML manifests and writes them to a csv file. Iterates through the directory and reads out element values for each XML file. XML elements are hardcoded into this script and not dynamically read, so some tweaking will need to be done to use on another collection.
