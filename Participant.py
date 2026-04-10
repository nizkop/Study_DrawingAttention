from STUDYGROUP import STUDYGROUP


class Participant(object):

    def __init__(self, id:str, studygroup: STUDYGROUP):
        self.id = id
        self.studygroup = studygroup

