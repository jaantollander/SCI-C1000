# Project Blog
Blog built using Pelican blogging platform. Blog is hosted in project's [GitHub pages](https://jaantollander.github.io/SCI-C1000/).

## Using Pelican
Read the Pelican [documentation](http://docs.getpelican.com/)

### General
Install Python into your machine. I recommed [Anaconda](https://www.continuum.io/downloads) distribution. You should also install some decent text and code editors such as [Atom](https://atom.io/) and [PyCharm](https://www.jetbrains.com/pycharm/).

### Installation
See `requirements.txt` file for installable packages. You can use command 

```
pip install -r requirements.txt
```


### Writing content
Write your content in the `content` folder. Static pages such as *About* and *Contact* are under `pages` folder. Content can be written in *ReStructuredText* (recommended) as  `.rst` files or *markdown* as `.md` or `.markdown` files.

### Developing
Make command to produce html

```
make html
```

Regenerate

```
make regenerate
```

Launch a development server in the `output` folder

```
python -m pelican.server
```

or if you installed `livereload` which refreshes updated content in your browser automatically run

```
livereload
```

in the `output` folder.

### Publish to blog GitHub pages
[Publishing to GitHub pages](http://docs.getpelican.com/en/3.6.3/tips.html?highlight=github#publishing-to-github)

In the root directory invoke command

```
make publish github
```
