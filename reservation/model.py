class Reservation:

    cm_id = TextField()
    label = TextField()
    summmary = TextField()
    hosts = TextField()
    user = TextField()
    project = TextField()
    start_time = DateTimeField()
    end_time = DateTimeField()

    def __str__(self):
        
        r = "label:", label + "\n" + \
            + "cm_id:", cm_id + "\n" + \
            + "summmary:", summmary + "\n" + \
            + "hosts:", hosts + "\n" + \
            + "user:", user + "\n" + \
            + "project:", project + "\n" + \
            + "start_time:", start_time + "\n" + \
            + "end_time:", end_time + "\n"

