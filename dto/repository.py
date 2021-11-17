class Repository:

    def __init__(self, name, full_name, clone_url, branch_name, owner, private):
        self.name = name
        self.full_name = full_name
        self.clone_url = clone_url
        self.branch_name = branch_name
        self.owner = owner
        self.private = private
