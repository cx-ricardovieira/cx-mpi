import configparser
import argparse
import scm.gh as github
import utils.csv_worker as csv_worker
import utils.project_creator as project_creator
from dto.project import Project

config = configparser.ConfigParser()
config.read("config.ini")

projects = []

parser = argparse.ArgumentParser(description='cx-mpi. Checkmarx CxSAST Massive Project Importer')
parser.add_argument('scm', type=str, default='github', choices=['github', 'gitlab', 'bitbucket', 'azuredevops'],
                    help='scm to get projects from')
parser.add_argument('operation', type=str, default='get', choices=['get', 'create'],
                    help='operation to execute. get: get the list of projects in .csv file. create: creates the '
                         'projects in CxSAST')


def main():
    args = parser.parse_args()

    if args.scm == "github" and args.operation == "get":
        con = github.connect(config["SCM"]["GH_TOKEN"])
        for repo in github.get_repos(con):
            projects.append(
                Project(repo.name + "-" + repo.branch_name, repo.full_name, config["CXSAST"]["PRESET"],
                        config["CXSAST"]["CONFIGURATION"],
                        config["CXSAST"]["TEAM"], repo.clone_url, repo.owner, repo.private,
                        config["CXSAST"]["GIT_ACCESS_TOKEN"], repo.branch_name, config["CXSAST"]["EXCLUDE_FOLDERS"],
                        config["CXSAST"]["EXCLUDE_FILES"], config["CXSAST"]["SCHEDULE_TYPE"],
                        config["CXSAST"]["SCHEDULE_DAYS"], config["CXSAST"]["SCHEDULE_TIME"]))

        csv_worker.write_csv(projects, "github")

    if args.scm == "github" and args.operation == "create":
        projects_to_create = csv_worker.read_csv()
        project_creator.create_project(projects_to_create, "github")


if __name__ == "__main__":
    main()
