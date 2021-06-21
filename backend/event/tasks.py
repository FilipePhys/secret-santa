from event.models import EventDay


def read_event_participant_id(event_id):
    people_obj = EventDay.objects.get(pk=event_id).event_day.all()
    people_id = [p_id.participant_id for p_id in people_obj]
    return people_id
