class Project:

    def __init__(self, name, full_name, preset, configuration, team, clone_url, owner, private, access_token, branch,
                 exclude_folders, exclude_files, schedule_type, schedule_days, schedule_time):
        self.name = name
        self.full_name = full_name
        self.preset = preset
        self.configuration = configuration
        self.team = team
        self.clone_url = clone_url
        self.owner = owner
        self.private = private
        self.access_token = access_token
        self.branch = branch
        self.exclude_folders = exclude_folders
        self.exclude_files = exclude_files
        self.schedule_type = schedule_type
        self.schedule_days = schedule_days
        self.schedule_time = schedule_time

