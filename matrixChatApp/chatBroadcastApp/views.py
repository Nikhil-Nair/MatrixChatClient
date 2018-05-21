from django.shortcuts import render
from django.http import HttpResponse
import requests, json

from .forms import MessageInputForm
from matrixChatApp.wsgi import acc_token
# Create your views here.
def home(request):
    access_key = acc_token
    room_keys = ["uxDBdZPYtvacXYNYUJ:matrix.org", "fPCYiApwrypdAIUFFJ:matrix.org", "AbBCCRYxHlyiiJydmA:matrix.org"]
    status = ""
    if request.method == 'POST':
        form = MessageInputForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['messageText']
            d = {"msgtype":"m.text", "body": message}
            status = "Hooray..Message sent successfully!"
            for rKey in room_keys:
                url = "https://matrix.org/_matrix/client/r0/rooms/%21{0}/send/m.room.message?access_token={1}".format(rKey, access_key)
                req = requests.post(url, data = json.dumps(d))
                if req.status_code != 200:
                    status = "Oops..Something Happened!One or more messages not sent."

    else:
        form = MessageInputForm()
    return render(request, "home.html", {"form" : form, "status" : status})
