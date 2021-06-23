import random

from user.models import CustomUser


#@app.task
def read_event_participant_id(my_event_id):
    from event.models import EventDay, Participant
    try:
        event = EventDay.objects.get(pk=my_event_id)
        people_obj = event.event_day.all()
        event_sets = [p_id.participant_id for p_id in people_obj]
    except "PKDoNotExistError":
        event_sets = []
    return event_sets


#@app.task
def drawing_marmalade(my_event_id):
    from event.models import Participant

    participant_model = Participant.objects.filter(event=my_event_id)
    participant = read_event_participant_id(my_event_id)
    validation = True
    while validation:
        participant_drawn = random.sample(participant, len(participant))
        count = 0
        for i in range(len(participant)):
            if participant_model[i].participant.relationship is not None:
                partner_id = participant_model[i].participant.relationship.pk
                print(participant[i], participant_drawn[i], partner_id)
                if participant[i] == participant_drawn[i] or participant_drawn[i] == partner_id:
                    count += 1
            else:
                print(participant[i], participant_drawn[i])
                if participant[i] == participant_drawn[i]:
                    count += 1
        if count == 0:
            validation = False
        else:
            validation = True

    return participant, participant_drawn


#@app.task
def drawing(my_event_id):
    participant = read_event_participant_id(my_event_id)
    validation = True
    while validation:
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


#@app.task
def save_draw(my_event_id):
    from event.models import EventDay, Participant

    event_filter = Participant.objects.filter(event_id=my_event_id)
    marmalade = EventDay.objects.get(pk=my_event_id).marmalade

    if marmalade:
        participant, participant_drawn = drawing_marmalade(my_event_id)
    else:
        participant, participant_drawn = drawing(my_event_id)

    for i, participant_instance in enumerate(event_filter):
        participant_instance.drawn_id = participant_drawn[i]
        participant_instance.save()
