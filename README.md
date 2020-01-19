# MediaMaking: 
## Purpose

In microbiology, a culture is an cultivation of bacteria or other microbial organism. 
Media is a very important environment for bacteria to grow. This software is record the media pH, date, name, and notes 
in a json format, and as a graph in png format. This software also provides a friendly GUI, which still needs a lot of improvement.

## Requirements
* [Python3](https://www.python.org/)
* [PyQt5](https://pypi.org/project/PyQt5/)
* [pydot](https://github.com/erocarrera/pydot) 
* [graphviz](https://www.graphviz.org/)
* [dateparser](https://pypi.org/project/dateparser/)
## Installation
Users can either use github interface Download button or type the following command in command line:
```bash
git clone https://github.com/nguyenngochuy91/MediaMaking.git
```
The users can either download the source codes of the requirements or use package management systems such as [brew](https://brew.sh/),
 or [conda](https://conda.io/miniconda.html). Users can also try [pip](https://pypi.org/project/pip/), but it has some problems for downloading 
both pydot and graphviz. Conda might fail with dateparser because of PyQt4 package, recommend using pip3 to install this package.


## Usage
The easiest way to run the project is to execute the script [gui.py](https://github.com/nguyenngochuy91/Cell/blob/master/home.py)
User can run it by typing the following in command line:
```bash
python3 gui.py
```

After that, just follow the instructions printing on the screen. The program will output a text file and a png file.
The text file is in json format, which is basically a dictionary. The dictionary stores all the information of the experiment such as
the name , the pH, the date and the notes for a media. The png file is a visualization of the process,
the node represent a media, an edge from one media to the next could be is an update. The program supports 3 main functions: analyze, modify, and update.
The function modify is to modify a media information, and update is to dilute a media into several new media. Each of the function is accompanied with visualization
and color to indicate nodes being updated/modified. The analyze function is to generate alert message for user to warn user about media that is more than 1 month old.

## Examples:
Here are the examples of a text file and the png file.
### data

![data](https://github.com/nguyenngochuy91/MediaMaking/blob/master/data)
### temp

![data](https://github.com/nguyenngochuy91/MediaMaking/blob/master/temp)