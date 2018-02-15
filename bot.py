#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time

from src import InstaBot
from src.check_status import check_status
from src.feed_scanner import feed_scanner
from src.follow_protocol import follow_protocol
from src.unfollow_protocol import unfollow_protocol

count = 0

bot = InstaBot(
    login='lyric.raja',
    password='d#FUN3732',
    like_per_day=850,
    comments_per_day=850,
    tag_list=['vizagdairies', 'vizag', 'vishakapatnam', 'rkbeach', 'rushikonda', 'rushikondabeach', 'lovevizag', 'vizagdiaries', 'vizagbeach', 'vizagtrip', 
              'hyderabadDiaries', 'hyderabadDays', 'hyderabaddays', 'hyderabaddiaries', 'charminar', 'charminarstreets', 'HyderabadLife', 'hyderabadLove', 
              'hellohyderabad', 'hyderabadphotographers', 'sohyderabad', 'photographersofhyderabad'],
    tag_blacklist=['thunderstorm'],
    user_blacklist={},
    max_like_for_one_tag = 20,
    follow_per_day=100,
    follow_time= 2 * 60,
    unfollow_per_day = 100,
    unfollow_break_min = 60,
    unfollow_break_max = 120,
    log_mod=0,
    proxy='',
    # List of list of words, each of which will be used to generate comment
    # For example: "This shot feels wow!"
    comment_list=[["This", "The", "Your"],
                  ["photo", "picture", "pic", "shot", "snap"],
                  ["is", "looks", "is really"],
                  ["great", "super", "good", "very good","wow",
                   "WOW", "cool", "magnificent", "magical",
                   "very cool", "very beautiful", "beautiful", "so beautiful",
                   "so colorful", "lovely",
                   "so lovely", "very lovely", "glorious",
                   "adorable", "excellent", "amazing"],
                  [". :) Check out my pics too ", ".. :) Check out my pics too", "... Check out my pics too", 
                  "! :D Check out my pics too", "!! :) Check out my pics too", "!!! :d Check out my pics too"]],
    # Use unwanted_username_list to block usernames containing a string
    ## Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    ### 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list=[
        'second', 'stuff', 'art', 'project', 'love', 'life', 'food', 'blog',
        'free', 'keren', 'photo', 'graphy', 'indo', 'travel', 'art', 'shop',
        'store', 'sex', 'toko', 'jual', 'online', 'murah', 'jam', 'kaos',
        'case', 'baju', 'fashion', 'corp', 'tas', 'butik', 'grosir', 'karpet',
        'sosis', 'salon', 'skin', 'care', 'cloth', 'tech', 'rental', 'kamera',
        'beauty', 'express', 'kredit', 'collection', 'impor', 'preloved',
        'follow', 'follower', 'gain', '.id', '_id', 'bags'
    ],
    unfollow_whitelist=['example_user_1', 'example_user_2'])
	
while count < 100:

    #print("# MODE 0 = ORIGINAL MODE BY LEVPASHA")
    #print("## MODE 1 = MODIFIED MODE BY KEMONG")
    #print("### MODE 2 = ORIGINAL MODE + UNFOLLOW WHO DON'T FOLLOW BACK")
    #print("#### MODE 3 = MODIFIED MODE : UNFOLLOW USERS WHO DON'T FOLLOW YOU BASED ON RECENT FEED")
    #print("##### MODE 4 = MODIFIED MODE : FOLLOW USERS BASED ON RECENT FEED ONLY")
    #print("###### MODE 5 = MODIFIED MODE : JUST UNFOLLOW EVERYBODY, EITHER YOUR FOLLOWER OR NOT")

    ################################
    ##  WARNING   ###
    ################################

    # DON'T USE MODE 5 FOR A LONG PERIOD. YOU RISK YOUR ACCOUNT FROM GETTING BANNED
    ## USE MODE 5 IN BURST MODE, USE IT TO UNFOLLOW PEOPLE AS MANY AS YOU WANT IN SHORT TIME PERIOD

    mode = 0
    count = count + 1 
    #print("You choose mode : %i" %(mode))
    #print("CTRL + C to cancel this operation or wait 30 seconds to start")
    #time.sleep(30)

    if mode == 0:
        print("mode 1 selected")
        bot.new_auto_mod()

    elif mode == 1:
        check_status(bot)
        while bot.self_following - bot.self_follower > 200:
            unfollow_protocol(bot)
            time.sleep(1 * 60)
            check_status(bot)
        while bot.self_following - bot.self_follower < 400:
            while len(bot.user_info_list) < 50:
                feed_scanner(bot)
                time.sleep(1 * 60)
                follow_protocol(bot)
                time.sleep(1 * 60)
                check_status(bot)

    elif mode == 2:
        bot.bot_mode = 1
        bot.new_auto_mod()

    elif mode == 3:
        unfollow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 4:
        print("mode 4")
        feed_scanner(bot)
        time.sleep(60)
        follow_protocol(bot)
        time.sleep(1 * 60)

    elif mode == 5:
        bot.bot_mode = 2
        unfollow_protocol(bot)

    else:
        print("Wrong mode!")
