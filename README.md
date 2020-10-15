# cwl2atom 


## Installation

### Via conda

```bash
conda install -c eoepca cwl2atom
```

### Development

Clone this repo, then create the conda environment with:

```bash
cd cwl-wrapper
conda env create -f environment.yml
conda activate env_cwl2atom
```

Use setuptools to install the project:

```bash
python setup.py install
```

Check the installation with:

```bash
cwl2atom --help
```

## Run the tool

```bash
cwl2atom eoepca-vegetation-index-ref.cwl > eoepca-vegetation-index-ref.atom 
```

