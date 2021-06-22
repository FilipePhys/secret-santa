import random

from event.models import EventDay, Participant
from user.models import CustomUser


class Draw:

    @classmethod
    def save_draw(cls, my_event_id):
        event_filter = Participant.objects.filter(event_id=my_event_id)
        marmalade = EventDay.objects.get(pk=my_event_id).marmalade

        if marmalade:
            print(marmalade)
            participant, participant_drawn = cls.drawing_marmalade(my_event_id)
        else:
            participant, participant_drawn = cls.drawing(my_event_id)
        for i, participant_instance in enumerate(event_filter):
            participant_instance.drawn_id = participant_drawn[i]
            participant_instance.save()

    @classmethod
    def drawing_marmalade(cls, my_event_id):
        participant = cls.read_event_participant_id(my_event_id)
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
    def drawing(cls, my_event_id):
        participant = cls.read_event_participant_id(my_event_id)
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
    def read_event_participant_id(cls, my_event_id):
        try:
            event = EventDay.objects.get(pk=my_event_id)
            people_obj = event.event_day.all()
            event_sets = [p_id.participant_id for p_id in people_obj]
        except "PKDoNotExistError":
            event_sets = []
        return event_sets
