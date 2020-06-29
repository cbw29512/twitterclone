from django.shortcuts import render, HttpResponseRedirect, reverse
from notification.models import Notification
from twitteruser.models import TwitterUser
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View

# Create your views here.


class NotificationView(View):
    @method_decorator(login_required)
    def get(self,request):
        notified_user = request.user
        notifications = Notification.objects.filter(notify_user=notified_user, unread_notify = False)
        for notification in notifications:
            notification.unread_notify = True
            notification.save()
        return render(request, 'notification.html', {'notifications': notifications, 'notified_user': notified_user})