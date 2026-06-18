class AccessPermission:
    def init(self):
        self.permissions = {}

    def add_permission(self, plate, gate_id):
        if plate not in self.permissions:
            self.permissions[plate] = []

        self.permissions[plate].append(gate_id)

    def check_access(self, plate, gate_id):
        if plate in self.permissions:
            return gate_id in self.permissions[plate]
        return False
