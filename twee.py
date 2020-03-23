import sys
import tweepy
from decouple import config
import fnmatch
import time

status_replied = {}
music_dic = {}
f = open('musics.txt', 'r')
f_replied_users = open('replied_users.txt', 'r')

for line in f:
    music_dic[line.upper()] = 0

for line in f_replied_users:
    line = line.replace('\n', '')
    status_replied[line] = 1

f_replied_users.close()

auth = tweepy.OAuthHandler(config('CONSUMER_KEY'), config('CONSUMER_SECRET'))
auth.set_access_token(config('ACCESS_TOKEN'), config('ACCESS_TOKEN_SECRET'))

api = tweepy.API(auth, wait_on_rate_limit=True)

user_name = "@dabliucomsomdeu"
status_id = 1241892537889173509

status = api.get_status(status_id, tweet_mode='extended')

replies = ''
while (1):
    f_replied_users = open('replied_users.txt', 'a')
    replies = tweepy.Cursor(api.search, q='to:{}'.format(user_name),
                            since_id=status_id, tweet_mode='extended').items()
    if replies != '':
        user_screen_name = ''
        for rp in replies:
            if rp.in_reply_to_status_id == status_id:
                user_rp = rp.user
                user_screen_name = user_rp.screen_name

                if user_screen_name in status_replied:
                    status_replied[user_screen_name] += 1
                else:
                    new_reply = '@' + user_screen_name + ' '
                    rpText = rp.full_text.replace('@dabliucomsomdeu ', '')
                    for char in rpText:
                        char =  char.upper()
                        musics = fnmatch.filter(music_dic, char + '*')

                        min = 9999
                        mus_ans = ""
                        for m in musics:
                            if (music_dic[m] < min):
                                mus_ans = m
                                min = music_dic[m]
                                music_dic[m] += 1

                        new_reply += mus_ans

                    if len(new_reply) > 240:
                        rp1 = new_reply[0:239]
                        rp2 = new_reply[240:479]
                        rp3 = new_reply[480:719]
                        rp4 = new_reply[720:959]


                        if len(rp1) > 0:
                            st1 = api.update_status(rp1, rp.id)
                            if len(rp2) > 0:
                                st2 = api.update_status(rp2, st1.id)
                                if len(rp3) > 0:
                                    st3 = api.update_status(rp3, st2.id)
                                    if len(rp4) > 0:
                                        st4 = api.update_status(rp4, st3.id)
                    else:
                        api.update_status(new_reply, rp.id)
                        f_replied_users.write('\n' + user_screen_name)

                    print("Respondeu a :" + user_screen_name)
                    status_replied[user_screen_name] = 1
                    f_replied_users.write('\n' + user_screen_name)

        f_replied_users.close()
        time.sleep(60)
