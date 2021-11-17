# cx-mpi
Checkmarx Massive Project Importer
A tool, developed in python, to massive import projects into CxSAST from your SCM. The projects are created in CxSAST using the git connection and ultimately configure the projects to trigger scans automatically using CxSAST built-in scheduler.

## How to use it?

usage: main.py [-h] {github,gitlab,bitbucket,azuredevops} {get,create}
---

configuration file (config.ini)
---
CX_SAST_URL - CxSAST host
CX_SAST_USERNAME - CxSAST username
CX_SAST_PASSWORD - CxSAST password
PRESET - CxSAST preset to be used in the project(s). Can be changed in the .csv file.
TEAM - CxSAST team to be assined to the project(s). Can be changed in the .csv file. Team needs to exists before using the create operation
GH_URL - github host
GH_USERNAME - github username
GH_TOKEN - github password

#### python main.py github get
Will create a csv file in the output folder with the details about the repos to be created in CxSAST.

#### python main.py github create
Will create the projects in CxSAST, using the most recent csv file in the output folder.

![cx-mips in action](https://github.com/cx-ricardovieira/cx-mpi/raw/main/how-to/cx-mpi-in-action.gif)

## Roadmap
- Use Checkmarx Python SDK.
- Implement for all other SCM.

## NOTE: At the moment only github is supported.
