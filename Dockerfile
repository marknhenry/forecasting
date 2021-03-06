FROM ubuntu:latest

ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN apt-get update  \
    && apt-get install -yq tzdata sudo jq \
    && ln -fs /usr/share/zoneinfo/Asia/Dubai /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata \
    && apt-get install -y wget graphviz libgraphviz-dev unzip git sudo \
    && rm -rf /var/lib/apt/lists/*

RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-py37_4.11.0-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-py37_4.11.0-Linux-x86_64.sh -b \
    && rm -f Miniconda3-py37_4.11.0-Linux-x86_64.sh 

RUN conda update -n base -c defaults conda -y \
  && conda init bash \
  && conda install -y nb_conda pandas matplotlib autopep8 ipykernel seaborn \
  && conda clean -a