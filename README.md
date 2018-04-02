## About

This repo provides a program to automatically generate my resume as a webpage and PDF from YAML.

The file `generate.py` reads from `resume.yaml` to pdf and html files by using Jinja templates.

## Usage

This requires a Python 3 installation and it needs `jinja2` and `pdfkit` packages. The installation of `pdfkit` please refer [the pdfkit repo](https://github.com/JazzCore/python-pdfkit).

``` shell
python generate.py resume.yaml
```

## Licensing

Please refer [the LICENSE file](https://github.com/ChingChuan-Chen/python-yaml-resume/blob/master/LICENSE.md).

## References

This repo is inspired by following projects:

1. https://github.com/ekCit/resume
1. https://github.com/nnadeau/cv
1. https://github.com/bamos/cv
1. https://github.com/jturner314/resume
