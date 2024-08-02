import sys
import yaml

with open('/home/hadoop/gcpairflow/som/config.yaml') as file:
    som_config = yaml.load(file, Loader=yaml.FullLoader)
for levels in som_config:
    for variables in som_config[levels]:
        globals()[variables] = som_config[levels][variables]
