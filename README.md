The current repositary re-organises Cern's open HZZ analysis (found at https://github.com/atlas-outreach-data-tools/notebooks-collection-opendata/blob/master/13-TeV-examples/uproot_python/HZZAnalysis.ipynb) of the ATLAS 4lep data (https://opendata.atlas.cern/docs/datasets/files/) into mutliple docker containers which process the data in parralel.

The number of workers may be defined in the docker-compose file (at default it is at 3). 
All docker images and containers can be built by running the command 'docker compose up'. 