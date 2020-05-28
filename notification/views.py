from django.shortcuts import render, HttpResponseRedirect, reverse
from notification.models import Notification
from twitteruser.models import TwitterUser


# Create your views here.


def notification_view(request):
    current_user = request.user
    notifications = Notification.objects.get(notify_user=current_user, unread_notifications=True)
    return render(request, 'notifications.html', {'notifications': notifications, 'notification_count': notification_count})