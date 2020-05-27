from django.shortcuts import render, HttpResponseRedirect, reverse
from tweet.models import Tweet
from tweet.forms import AddTweet
from twitteruser.models import TwitterUser


def add_tweet(request, user_id):
    form = AddTweet()
    if request.method == 'POST':
        form = AddTweet(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = TwitterUser.objects.get(id=user_id)
            tweet = Tweet.objects.create(
                tweet = data['tweet'],
                author = user,
            )
            return HttpResponseRedirect(reverse('home'))
    return render(request, "add_tweet.html", {"form": form})
