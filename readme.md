# Paper organizer

Did you ever search for scientific paper downloaded before and you can't 
find it because it was downloaded as `dsjkgqwtqoy843175.pdf`?

This project analyzes all your pdf files and displays them as web page 
containing titles and authors.

### Structure
1. All *.pdf files are found in `srcdir`
2. Those files are converted to html with great library - https://github
.com/coolwanglu/pdf2htmlEX (because PDF is not good for parsing)
3. Most probable title is found in the file
4. The article is found at scholar.google.com based on the title and the result
 is saved to LMDB
5. Stored results are presented by flask web page

## Disclaimer !!!
This project is in alpha version, see todo section.

## Issues
Please report all problems as [Github issues](https://github.com/tivvit/articleOrganizer/issues).

## Installation
##### Docker
 1. `git clone git@github.com:tivvit/articleOrganizer.git`
 2. `docker-compose up -d web`
 3. wait until the scan is finished
 4. go to `http://localhost:5050`
 
##### Without docker
 - You are on your own here (consult Dockerfile)
    - project is based on https://github.com/coolwanglu/pdf2htmlEX
    - python3 (pip3 install -r requirements.txt)
    - analyze papers `python3 main.py`
    - run web server `python3 web.py`
    
## Configuration
Edit `conf.yaml`
- `srcdir`: directory with articles

## Todo
 - add keywords
 - toggle abstract
 - secure paths from user (no folder in path to pdf)
 - "read that" plugin
 - do not keep html option
 - no abstracts in db option
 - generate - file watcher process
 - Images to docker hub with simple readme (without docker-compose)
 - explain all configuration options
 - add publish year

## Development

Feel free to contribute.

## Copyright and License
&copy; 2016 [Vít Listík](http://tivvit.cz)

Released under [MIT license](https://github.com/tivvit/articleOrganizer/blob/master/LICENSE)
