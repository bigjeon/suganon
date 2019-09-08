from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import SpeakerItem


def speakerview(request):
    all_speaker_items=SpeakerItem.objects.all()
    return render(request, 'speaker.html', {'all_items':all_speaker_items})

def addspeaker(request):
    new_item = SpeakerItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/speaker/')

def deletespeaker(request, speaker_id):
    item_to_delete=SpeakerItem.objects.get(id = speaker_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/speaker/')