FROM jupyter/r-notebook:latest

ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN apt-get update  \
    && apt-get install -yq tzdata \
    && ln -fs /usr/share/zoneinfo/Asia/Dubai /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata \
    && apt-get install -y wget graphviz libgraphviz-dev unzip git \
    && rm -rf /var/lib/apt/lists/*

# RUN wget \
#     # https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
#     https://repo.anaconda.com/miniconda/Miniconda3-py37_4.11.0-Linux-x86_64.sh \
#     && mkdir /root/.conda \
#     && bash Miniconda3-py37_4.11.0-Linux-x86_64.sh -b \
#     && rm -f Miniconda3-py37_4.11.0-Linux-x86_64.sh 
# RUN conda --version

# RUN conda update -n base -c defaults conda -y \
#   && conda clean -a \
#   && conda init bash
  
# RUN conda install -y pandas matplotlib autopep8 ipykernel nb_conda \
#   && conda clean -a
