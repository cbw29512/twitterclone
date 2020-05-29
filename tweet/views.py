from django.shortcuts import render, HttpResponseRedirect, reverse
from tweet.models import Tweet
from tweet.forms import AddTweet
from twitteruser.models import TwitterUser
from notification.models import Notification
from django.contrib.auth.decorators import login_required
import re


@login_required
def add_tweet(request, user_id):
    form = AddTweet()
    if request.method == 'POST':
        form = AddTweet(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            all_user = TwitterUser.objects.all()
            user = TwitterUser.objects.get(id=user_id)
            tweet = Tweet.objects.create(
                tweet = data['tweet'],
                author = user,
            )
            find_users = re.findall(r'@(\w+)', data['tweet'])
            #Derek Barnes and Matthem Perry assisted
            # for find_users in set(all_user):
            for tagged in find_users:
                Notification.objects.create(
                    notify_user = TwitterUser.objects.get(username=tagged),
                    tweet = tweet,
                )
            return HttpResponseRedirect(reverse('home'))
    return render(request, "add_tweet.html", {"form": form})


def tweetView(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    return render(request, 'tweet.html', {'tweet': tweet})