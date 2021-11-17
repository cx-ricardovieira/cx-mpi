# cx-mpi
Checkmarx Massive Project Importer
A tool, developed in python, to massive import projects into CxSAST from your SCM. The projects are created in CxSAST using the git connection and ultimately configure the projects to trigger scans automatically using CxSAST built-in scheduler.

## How to use it?

usage: main.py [-h] {github,gitlab,bitbucket,azuredevops} {get,create}
---

#### python main.py github get
Will create a csv file in the output folder with the details about the repos to be created in CxSAST.

#### python main.py github create
Will create the projects in CxSAST, using the most recent csv file in the output folder.

NOTE: At the moment only github is supported.

## Roadmap
- Use Checkmarx Python SDK.
- Implement for all other SCM.
