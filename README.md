# Project Blog
Blog built using Pelican blogging platform. Blog is hosted in project's [GitHub pages](https://jaantollander.github.io/SCI-C1000/).

## Using Pelican
Read the Pelican [documentation](http://docs.getpelican.com/)

### Installation
```
pip install Pelican markdown 
```

Optional but useful packages

```
pip install Fabric livereload
```

### Writing content
Write your content in the `content` folder. Static pages such as *About* and *Contact* are under `pages` folder. 

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
