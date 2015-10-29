## g4g-dl :bookmark:
###### Downloads all Geeks for Geeks Algo and Data Structures tutorials and save as PDF

Note: I wrote this script because I needed it for my own sake. I ain't sure if it's legal to scrape Geeks4Geeks. In future if I come across any such policies, I shall remove this repo without any hesitation.

Inspired from this awesome stuff called [Youtube-dl](https://github.com/rg3/youtube-dl)

### Installation

###### Dependency to be installed manually
[wkhtmltopdf](https://github.com/wkhtmltopdf/wkhtmltopdf)

##### Build from source
```sh
	git clone "https://github.com/tushar-rishav/g4g-dl.git"
	cd g4g-dl
	python setup.py install
```

###Default config:
	target  : g4gPdf

### Usage

##### Fetch single post
To fetch single tutorial, say Topological Sorting, run this in your shell
```sh

g4g-dl -p http://www.geeksforgeeks.org/topological-sorting/

```
Note: 
1. The above command will save the pdf in default directory
2. You must specify `-d` (for data structure) or `-a` (for algo) if you aren't fetching tutorials this way.

##### Fetch all data structure tutorial in your custom directory

```sh
g4g-dl -t my_directory_abs_path -d

```
##### Fetch top 10 algo tutorial in your custom directory

```sh
g4g-dl -t my_directory_abs_path -l 10 -a

```
Note: The order is according to they appear in page.

##### Get help
```sh
g4g-dl -h

```
##### Example
```sh
g4g-dl -l 10 -t DS_G4G -d

```
The above command will fetch top 10 data structures tutorials from Geeks for Geeks and save them as PDF in DS_G4G directory


### Contributions
Have an idea to make it better? Go ahead! I will be happy to see a pull request from you! :blush:

### License
![gpl](https://cloud.githubusercontent.com/assets/7397433/9025904/67008062-3936-11e5-8803-e5b164a0dfc0.png)
