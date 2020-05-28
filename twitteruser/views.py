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
    twitteruser = TwitterUser.objects.get(id=user_id)
    following_list = request.user.following.all()
    followers_count = following_list.count()
    tweet_count = user_tweets.count()
    if twitteruser in following_list:
        is_following = True
    else:
        is_following = False
    return render(
        request, 'profile.html', {
            'user_tweets': user_tweets, 
            'twitteruser': twitteruser, 
            'is_following': is_following,
            'followers_count': followers_count,
            'tweet_count': tweet_count,
            })


#https://stackoverflow.com/questions/6218175/how-to-implement-followers-following-in-django
# How to implement followers/following in Django  
# Assistance from Peter Marsh 


def follow_user(request, id):
    current_user = request.user
    follow_user = TwitterUser.objects.get(id=id)
    current_user.following.add(follow_user)
    current_user.save()
    return HttpResponseRedirect(reverse('profile', kwargs={'user_id': id})) 


def unfollow_user(request, id):
    current_user = request.user
    follow_user = TwitterUser.objects.get(id=id)
    current_user.following.remove(follow_user)
    current_user.save()
    return HttpResponseRedirect(reverse('profile', kwargs={'user_id': id}))
 