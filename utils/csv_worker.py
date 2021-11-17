import csv
import glob
import os
from datetime import datetime

from dto.project import Project

list_of_projects = []


def write_csv(projects, scm):
    now = datetime.now()

    file = open("output/projects_" + scm + "_" + now.strftime("%Y%m%d%H%M%S") + ".csv", "w", newline="")
    fieldnames = ["name", "full_name", "preset", "configuration", "team", "clone_url", "owner", "private",
                  "access_token", "branch", "exclude_files", "exclude_folders", "schedule_type", "schedule_days",
                  "schedule_time"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer = csv.writer(file)
    for project in projects:
        writer.writerow([project.name, project.full_name, project.preset, project.configuration, project.team,
                         project.clone_url, project.owner, project.private, project.access_token, project.branch,
                         project.exclude_files, project.exclude_folders, project.schedule_type, project.schedule_days,
                         project.schedule_time])
    file.close()


def read_csv():
    files = glob.glob('output/*')
    latest_file = max(files, key=os.path.getctime)

    with open(latest_file, newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            list_of_projects.append(Project(row["name"], row["full_name"], row["preset"], row["configuration"],
                                            row["team"], row["clone_url"], row["owner"], row["private"],
                                            row["access_token"], row["branch"], row["exclude_files"],
                                            row["exclude_folders"], row["schedule_type"], row["schedule_days"],
                                            row["schedule_time"]))
            line_count += 1

    return list_of_projects
