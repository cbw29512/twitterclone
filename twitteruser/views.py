from django.shortcuts import render, HttpResponseRedirect, reverse
from authentication.forms import SignUpForm, LoginForm
from twitteruser.models import TwitterUser
from django.contrib.auth.decorators import login_required
from tweet.models import Tweet
# Create your views here.


@login_required
def index(request):
    html = 'index.html'
    user_data = TwitterUser.objects.all()
    tweet_data = Tweet.objects.all()
    return render(request, html, {'tweet_data': tweet_data, "user_data": user_data})


def profileView(request, user_id):
    user_tweets = Tweet.objects.filter(author = user_id)
    return render(request, 'profile.html', {'user_tweets': user_tweets})
