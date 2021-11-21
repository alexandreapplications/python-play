#!/bin/bash
sha256() {
    echo "$1 $2" | sha256sum --check
}

# wget https://github.com/prometheus/prometheus/releases/download/v2.31.1/prometheus-2.31.1.linux-amd64.tar.gz

# sha256 '7852dc11cfaa039577c1804fe6f082a07c5eb06be50babcffe29214aedf318b3' 'prometheus-2.31.1.linux-amd64.tar.gz'
# tar -xvf prometheus-2.31.1.linux-amd64.tar.gz

# wget https://github.com/prometheus/node_exporter/releases/download/v1.3.0/node_exporter-1.3.0.linux-amd64.tar.gz
sha256 'b16d5061d3bc3d0ad8232964071ee3ece7fc104afa817bb5f55570521756125d' 'node_exporter-1.3.0.linux-amd64.tar.gz'
tar xvfz node_exporter-*.*-amd64.tar.gz