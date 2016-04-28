FROM python:3.5

MAINTAINER Sylvain Bellemare <sbellem@gmail.com>

RUN apt-get update && apt-get install -y texlive texlive-latex-extra
RUN apt-get install -y pandoc
RUN apt-get install -y context
RUN apt-get install -y graphviz

RUN pip install --upgrade pip
RUN pip install sphinx hieroglyph

VOLUME /usr/src/
WORKDIR /usr/src/
