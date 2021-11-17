from github import Github
from dto.repository import Repository

repositories = []


def connect(token):
    return Github(token)


def get_repos(connection: Github):
    for repo in connection.get_user().get_repos():
        for branch in repo.get_branches():
            repositories.append(Repository(repo.name, repo.full_name, repo.clone_url, branch.name, repo.owner.login, repo.private))

    return repositories
