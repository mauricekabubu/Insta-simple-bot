from time import sleep
from instabot import Bot


my_bot = Bot()
# login into my user account
my_bot.login(username='Mauricekabubs',email='mauricekabubu2006@gmail.com')
# follow others using automation bot
my_bot.follow('pythondevs')
# approve pending follow requests using bot
my_bot.approve_pending_follow_requests()
# approving pending thread requests
my_bot.approve_pending_thread_requests()
# unfollow those who don't follow me back
my_bot.unfollow('')
# unfollow non followers
my_bot.unfollow_non_followers()

# liking posts and reels/media
my_bot.like('')
my_bot.comment_medias('')
# following those who follow back
my_bot.follow_following('')
# following user
my_bot.follow_users('pythondev',2)
# maximum followers to following
my_bot.max_followers_to_following_ratio(2)
my_bot.max_followers_to_follow(5)
my_bot.max_likes_to_like(3)
my_bot.min_likes_to_like(2)

sleep(20)
# commenting on posts and reels/medias
try:
    user_id = my_bot.get_user_id_from_username('')
    media_id = my_bot.get_last_user_medias(user_id,3)
    my_bot.comment(media_id,2)
except Exception as e:
    print(e)

# sending messages
my_bot.send_message("Hi Maurice i'm your automation bot\n"
                    "Call me Codex Bot",'Mauricekabubs')
my_bot.send_photo('','')

# following list and follower list
following_list = my_bot.get_user_following('Mauricekabubs',10)
follower_list = my_bot.get_user_followers('Mauricekabubs',10)

for count,each_follower in enumerate(follower_list):
    if count > 4:
        continue
    sleep(5)
    print(my_bot.get_user_id_from_username(each_follower))

for count,each_following in enumerate(following_list):
    if count > 4:
        continue
    sleep(5)
    print(my_bot.get_user_id_from_username(each_following))

my_bot.logout()