# book volume organiser

copies files from chapter subfolders into a single unified volume folder while renaming them in a consistent numbered format  

intended for organising scanned books manga chapters or other image based volumes from [HakuNeko](https://hakuneko.download/) and similar tools    

originally created by [KojoBailey](https://github.com/KojoBailey/book-volume-organiser), proper usage after using the tool can be seen in their complete guide [here](https://gist.github.com/KojoBailey/722d0f599a2279a6bee24ba07eaf2728)

## what it does

- one input volume folder (created manually) containing chapter subfolders (which should have been created by HakuNeko, or equivalent)
- each subfolder is treated as a chapter
- all files are copied into a single output folder
- files are renamed using chapter index per chapter index and global index
- original filenames are ignored except for the file extension
- works natively on mac, windows, and linux
- useful for easy imports into [calibre](https://calibre-ebook.com/download) or other epub editors

before
```
volume/
├── chapter 01/
│   ├── 01.jpg
│   ├── 02.jpg
│   └── 03.jpg
├── chapter 02/
│   ├── 01.jpg
│   ├── 02.jpg
│   └── 03.jpg
```
after
```
organised volume/
├── Ch1-1 (1).jpg
├── Ch1-2 (2).jpg
├── Ch1-3 (3).jpg
├── Ch2-1 (4).jpg
├── Ch2-2 (5).jpg
├── Ch2-3 (6).jpg
```
## behavior notes

- files are copied not moved  
- chapter folders and files are processed in sorted order by name  
- repeated filenames inside chapters are safe  
- existing files in the output folder may be overwritten if names collide  

## requirements

- python 3.9 or newer
- git (optional)


## installation

copy the script into a directory or clone the repository

```shell
git clone https://github.com/StarFallenJax/book-volume-organiser.git
cd book-volume-organiser
```

## usage

### mac and linux

run from terminal

```shell
python3 organise_volume.py "/path/to/volume"
```

### windows

run from command prompt or powershell

```shell
python organise_volume.py "C:\path\to\volume"
```

### custom output folder

by default the output folder is named organised volume and created in the current directory,
to specify a different output location

```shell
python organise_volume.py "/path/to/volume" -o "/path/to/output"
```



## license

free to use modify and distribute

original idea from [KojoBailey](https://github.com/KojoBailey/book-volume-organiser)



