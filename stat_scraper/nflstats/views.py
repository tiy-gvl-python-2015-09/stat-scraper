from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

import requests
import re
# Create your views here.

def helloview(request):
    if request.GET.get('player'):
        body = requests.get("http://www.nfl.com/players/search?category=name&filter={}&playerType=current".format(request.GET.get('player').lower().replace(" ", "+"))).content
        souper = BeautifulSoup(body)
        link_objects = souper.find_all('a', attrs={'href': True})
        stats_link = []
        for link in link_objects:
            if re.match('/player/.+', link['href']):
                stats_link.append(link['href'])
        if len(stats_link) == 1:
            player_stats_link = stats_link[0].replace('profile', 'careerstats')
        new_body = requests.get("http://www.nfl.com{}".format(player_stats_link))
        #new_souper = BeautifulSoup(new_body)
        #stats = new_souper.find('div', attrs={'id': 'player-stats-wrapper'}).text
        return HttpResponse(new_body)
    else:
        return render_to_response('index.html', {'context': 'Please search for a player'})