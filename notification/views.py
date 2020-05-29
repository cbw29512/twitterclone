from django.shortcuts import render, HttpResponseRedirect, reverse
from notification.models import Notification
from twitteruser.models import TwitterUser


# Create your views here.


def notification_view(request):
    notified_user = request.user
    notifications = Notification.objects.filter(notify_user=notified_user, unread_notify = False)
    for notification in notifications:
        notification.unread_notify = True
        notification.save()
    return render(request, 'notification.html', {'notifications': notifications, 'notified_user': notified_user})