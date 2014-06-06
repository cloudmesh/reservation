class Reservation:

    cm_id = TextField()
    label = TextField()
    summmary = TextField()
    hosts = TextField()
    user = TextField()
    project = TextField()
    start_time = DateTimeField()
    end_time = DateTimeField()

    _order = [
        "label",
        "cm_id",
        "summmary",
        "hosts",
        "user",
        "project",
        "start_time",
        "end_time"
    ]

    def __str__(self):
        d = self.to_json()
        r = ""
        for key in _order:
            r = r + key + ": " + d[key]
        return r

    def to_json(self):
        d = {"label:", label,
             "cm_id:", cm_id,
             "summmary:", summmary,
             "hosts:", hosts,
             "user:", user,
             "project:", project,
             "start_time:", start_time,
             "end_time:", end_time}
        return d
