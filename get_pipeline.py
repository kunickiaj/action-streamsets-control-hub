#!/usr/bin/env python3

import argparse
import json
import os

from git import Repo
from streamsets.sdk import ControlHub

parser = argparse.ArgumentParser(description="Fetch some pipelines")
parser.add_argument("url")
parser.add_argument("username")
parser.add_argument("pipeline_id")

args = parser.parse_args()

sch = ControlHub(
    args.url, username=args.username, password=os.environ.get("SCH_PASSWORD")
)

pipeline = sch.pipelines.get(pipeline_id=args.pipeline_id)
pipelineDefinition = json.loads(pipeline._data["pipelineDefinition"])
pipeline_file_name = "pipeline-%s.json" % pipeline.pipeline_id
with open(pipeline_file_name, "w") as exported_pipeline:
    json.dump(pipelineDefinition, exported_pipeline, indent=2)

repo = Repo(".")
index = repo.index
added_pipeline_path = os.path.join(repo.working_tree_dir, pipeline_file_name)
index.add([added_pipeline_path])
index.commit("Pipeline %s updated" % pipeline.name)
