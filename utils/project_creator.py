import configparser
import subprocess

config = configparser.ConfigParser()
config.read("config.ini")

cli = "cx-cli\\runCxConsole.cmd"


def create_project(projects, scm):
    for project in projects:
        git_url = "https://" + config["SCM"]["GH_USERNAME"] + ":" + config["SCM"]["GH_TOKEN"] + "@" + \
                  config["SCM"]["GH_URL"] + "/" + project.full_name + ".git"

        cmd = 'AsyncScan -v -CxServer "' + config["CXSAST"]["CX_SAST_URL"] + '" -CxUser "' + \
              config["CXSAST"]["CX_SAST_USERNAME"] + '" -CxPassword "' + config["CXSAST"]["CX_SAST_PASSWORD"] + \
              '" -ProjectName "' + project.team + "\\" + project.name + '" -LocationType "Git" -LocationURL "' + \
              git_url + '" -LocationBranch "refs/heads/' + project.branch + '" -Preset "' + \
              config["CXSAST"]["PRESET"] + '" -LocationPathExclude "' + project.exclude_folders + \
              '" -LocationFilesExclude "' + project.exclude_files + '" -Configuration "' + project.configuration \
              + '"'
        cmd = cli + " " + cmd

        subprocess.run(cmd)
