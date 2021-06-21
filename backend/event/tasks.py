import random

from event.models import EventDay, Participant
from user.models import CustomUser


class Draw:

    # @classmethod
    # def save_draw(cls, event_id):
    #     participant, participant_drawn = cls.drawing_marmalade(event_id)
    #     for i, id_participant in enumerate(participant_drawn):
    #         user = CustomUser.objects.get(pk=id_participant)
    #         Participant.objects.get(participant=participant[i])
    #         participant.drawn == user
    #         Participant.save()


    @classmethod
    def drawing_marmalade(cls, event_id):
        participant = cls.read_event_participant_id(event_id)
        print(participant)
        validation = True
        while validation:
            participant_drawn = random.sample(participant, len(participant))
            count = 0
            for i in range(len(participant)):
                try:
                    partner = CustomUser.objects.filter(pk=i)[0].relationship.pk
                    if participant[i] == participant_drawn[i] or participant_drawn[i] == partner:
                        count += 1
                except:
                    if participant[i] == participant_drawn[i]:
                        count += 1
            if count == 0:
                validation = False
            else:
                validation = True

        return participant, participant_drawn

    @classmethod
    def drawing(cls, event_id):
        participant = cls.read_event_participant_id(event_id)
        validation = True
        while validation:
            print('o')
            participant_drawn = random.sample(participant, len(participant))
            count = 0
            for i in range(len(participant)):
                if participant[i] == participant_drawn[i]:
                    count += 1
            if count == 0:
                validation = False
            else:
                validation = True

        return participant, participant_drawn

    @classmethod
    def read_event_participant_id(cls, event_id):
        try:
            event = EventDay.objects.get(pk=event_id)
            people_obj = event.event_day.all()
            event_sets = [p_id.participant_id for p_id in people_obj]
        except "PK_DoNotExistError":
            event_sets = []
        return event_sets
