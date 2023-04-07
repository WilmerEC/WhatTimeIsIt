# Owner: Wilmer Cubillan -- 04/06/2023
# Title: WhatTimeIsIt? 
# Description: Discord bot that converts from your current time to other timezones
# Etc: Currently supported timezones are EST, PST, CET, BST, CST, JST

import discord
from discord.ext import commands
import os
import random
import datetime
import pytz

bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'))
@bot.slash_command(name="time", Description="Gives back time. Use 24 hr format")
async def test(ctx, time, your_timezone):
    
    est = pytz.timezone("America/New_York")
    pst = pytz.timezone("America/Los_Angeles")
    cet = pytz.timezone("Europe/Amsterdam")
    bst = pytz.timezone("Europe/London")
    cst = pytz.timezone("Asia/Shanghai")
    jst = pytz.timezone("Asia/Tokyo")
    current_time = datetime.datetime.strptime(time, "%H:%M")
    
    if(your_timezone=="EST"):
        await ctx.respond(f"```Your Time: {current_time.hour}:{current_time.minute} {your_timezone}\n\nPST: { current_time.astimezone(pst).hour}:{current_time.astimezone(pst).minute}\nCET: { current_time.astimezone(cet).hour}:{current_time.astimezone(cet).minute}\nBST: { current_time.astimezone(bst).hour}:{current_time.astimezone(bst).minute}\nCST: { current_time.astimezone(cst).hour}:{current_time.astimezone(cst).minute}\nJST: { current_time.astimezone(jst).hour}:{current_time.astimezone(jst).minute}\n```")
    elif(your_timezone=="PST"):
        await ctx.respond(f"```Your Time: {current_time.hour}:{current_time.minute} {your_timezone}\n\nEST: { current_time.astimezone(est).hour}:{current_time.astimezone(est).minute}\nCET: { current_time.astimezone(cet).hour}:{current_time.astimezone(cet).minute}\nBST: { current_time.astimezone(bst).hour}:{current_time.astimezone(bst).minute}\nCST: { current_time.astimezone(cst).hour}:{current_time.astimezone(cst).minute}\nJST: { current_time.astimezone(jst).hour}:{current_time.astimezone(jst).minute}\n```")
    elif(your_timezone=="CET"):
        await ctx.respond(f"```Your Time: {current_time.astimezone(cet).hour}:{current_time.astimezone(cet).minute} {your_timezone}\n\nEST: { current_time.astimezone(est).hour}:{current_time.astimezone(est).minute}\nPST: { current_time.astimezone(pst).hour}:{current_time.astimezone(pst).minute}\nBST: { current_time.astimezone(bst).hour}:{current_time.astimezone(bst).minute}\nCST: { current_time.astimezone(cst).hour}:{current_time.astimezone(cst).minute}\nJST: { current_time.astimezone(jst).hour}:{current_time.astimezone(jst).minute}\n```")    
    elif(your_timezone=="BST"):
        await ctx.respond(f"```Your Time: {current_time.hour}:{current_time.minute} {your_timezone}\n\nEST: { current_time.astimezone(est).hour}:{current_time.astimezone(est).minute}\nPST: { current_time.astimezone(pst).hour}:{current_time.astimezone(pst).minute}\nCET: { current_time.astimezone(cet).hour}:{current_time.astimezone(cet).minute}\nCST: { current_time.astimezone(cst).hour}:{current_time.astimezone(cst).minute}\nJST: { current_time.astimezone(jst).hour}:{current_time.astimezone(jst).minute}\n```")
    elif(your_timezone=="CST"):
        await ctx.respond(f"```Your Time: {current_time.hour}:{current_time.minute} {your_timezone}\n\nEST: { current_time.astimezone(est).hour}:{current_time.astimezone(est).minute}\nPST: { current_time.astimezone(pst).hour}:{current_time.astimezone(pst).minute}\nCET: { current_time.astimezone(cet).hour}:{current_time.astimezone(cet).minute}\nBST: { current_time.astimezone(bst).hour}:{current_time.astimezone(bst).minute}\nJST: { current_time.astimezone(jst).hour}:{current_time.astimezone(jst).minute}\n```")
    elif(your_timezone=="CST"):
        await ctx.respond(f"```Your Time: {current_time.hour}:{current_time.minute} {your_timezone}\n\nEST: { current_time.astimezone(est).hour}:{current_time.astimezone(est).minute}\nPST: { current_time.astimezone(pst).hour}:{current_time.astimezone(pst).minute}\nCET: { current_time.astimezone(cet).hour}:{current_time.astimezone(cet).minute}\nBST: { current_time.astimezone(bst).hour}:{current_time.astimezone(bst).minute}\nCST: { current_time.astimezone(cst).hour}:{current_time.astimezone(cst).minute}\n```")

bot.run("TOKEN")
