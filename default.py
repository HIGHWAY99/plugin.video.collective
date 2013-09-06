import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os,settings
from t0mm0.common.addon import Addon
from t0mm0.common.net import Net
from metahandler import metahandlers
from metahandler import metacontainers
from universal import favorites
from universal import _common as univ_common
from settings import *

############################################################################################################################################################

icon = 'icon.png'
fanart = 'fanart.png'
fav = favorites.Favorites('plugin.video.collective', sys.argv)
grab = metahandlers.MetaData(preparezip = False)
addon_id = 'plugin.video.collective'
local = xbmcaddon.Addon(id=addon_id)
collectivepath = local.getAddonInfo('path')
addon = Addon(addon_id, sys.argv)
datapath = addon.get_profile()
art = collectivepath+'/art'
net = Net()

############################################################################################################################################################

base_url = 'http://www.nzbmovieseeker.com'
movie_url = 'http://www.nzbmovieseeker.com/New/'
tv_url = 'http://www.nzbtvseeker.com/'
IMDb_url = 'http://www.imdb.com'
IMDbIT_url = 'http://www.imdb.com/movies-in-theaters/?ref_=nb_mv_2_inth'
IMDb250_url = 'http://www.imdb.com/search/title?groups=top_250&sort=user_rating&my_ratings=exclude'
onechannel_base = 'http://www.primewire.ag/'
onechannel_featured = 'http://www.primewire.ag/index.php?sort=featured'
onechannel_featuredtv = 'http://www.primewire.ag/?tv=&sort=featured'
onechannel_lastest = 'http://www.primewire.ag/?sort=date'
onechannel_lastesttv = 'http://www.primewire.ag/?tv=&sort=date'
onechannel_populartv = 'http://www.primewire.ag/?tv=&sort=views'
onechannel_popular = 'http://www.primewire.ag/?sort=views'
onechannel_ratings = 'http://www.primewire.ag/?sort=ratings'
onechannel_ratingstv = 'http://www.primewire.ag/?tv=&sort=ratings'
onechannel_releasedatetv = 'http://www.primewire.ag/?tv=&sort=release'
onechannel_releasedate = 'http://www.primewire.ag/?sort=release'

#_OA = Addon('plugin.video.otheraddons', sys.argv)
#IMDBTV_WATCHLIST = settings.imdbtv_watchlist_url()
#IMDB_LIST = settings.imdb_list_url()

#Metahandler
def GRABMETA(name,types):
	type = types
	EnableMeta = local.getSetting('Enable-Meta')
	if EnableMeta == 'true':
		if 'Movie' in type:
			meta = grab.get_meta('movie',name,'',None,None,overlay=6)
			infoLabels = {'rating': meta['rating'],'duration': meta['duration'],'genre': meta['genre'],'mpaa':"rated %s"%meta['mpaa'],'plot': meta['plot'],'title': meta['title'],'writer': meta['writer'],'cover_url': meta['cover_url'],'director': meta['director'],'cast': meta['cast'],'backdrop_url': meta['backdrop_url'],'backdrop_url': meta['backdrop_url'],'tmdb_id': meta['tmdb_id'],'year': meta['year']}
		elif 'tvshow' in type:
			meta = grab.get_meta('tvshow',name,'','',None,overlay=6)
			infoLabels = {'rating': meta['rating'],'genre': meta['genre'],'mpaa':"rated %s"%meta['mpaa'],'plot': meta['plot'],'title': meta['title'],'cover_url': meta['cover_url'],'cast': meta['cast'],'studio': meta['studio'],'banner_url': meta['banner_url'],'backdrop_url': meta['backdrop_url'],'status': meta['status']}
	else: infoLabels=[]
	return infoLabels

######################################################################################################################################################

 #      addDir(name,url,mode,iconimage,types,favtype) mode is where it tells the plugin where to go scroll to bottom to see where mode is
def CATEGORIES():
        addDir('Movies',onechannel_base,3,art_('Movies','Main Menu'),None,'')
        addDir('TV-Shows',onechannel_base,2,art_('TV Shows','Main Menu'),None,'TV-Shows')
        addDir('Music',onechannel_base,29,art_('music','Main Menu'),None,'')
        fav.add_my_fav_directory(img=art_('Favorites','Main Menu'))
        addDir('Settings','http://',309,art_('Settings','Main Menu'),None,'')
        set_view('list') 
       
       
def TVSHOWScat():
        addDir('Latest Added',onechannel_lastesttv,21,art_('Latest','Sub Menus'),None,'')
        addDir('Featured',onechannel_featuredtv,19,art_('Featured','Sub Menus'),None,'')
        addDir('Popular',onechannel_populartv,23,art_('Popular','Sub Menus'),None,'')
        addDir('Ratings',onechannel_ratingstv,25,art_('Ratings','Sub Menus'),None,'')
        addDir('Release Date',onechannel_releasedatetv,27,art_('Release Date','Sub Menus'),None,'')
        addDir('Genre',tv_url,5,art_('Genre','Sub Menus'),None,'')
        addDir('TVDB',tv_url,5,art_('TVDB','Sub Menus'),None,'')
        addDir('Search',onechannel_base,28,art_('Search','Sub Menus'),None,'')
        set_view('list') 
       
def MOVIEScat():
        addDir('Latest Added',onechannel_lastest,20,art_('Latest','Sub Menus'),None,'')
        addDir('Featured',onechannel_featured,18,art_('Featured','Sub Menus'),None,'')
        addDir('Popular',onechannel_popular,22,art_('Popular','Sub Menus'),None,'')
        addDir('Ratings',onechannel_ratings,24,art_('Ratings','Sub Menus'),None,'')
        addDir('Release Date',onechannel_releasedate,26,art_('Release Date','Sub Menus'),None,'')
        addDir('Genre',movie_url,4,art_('Genre','Sub Menus'),None,'')
        addDir('IMDb',IMDb_url,16,art_('IMDb','Sub Menus'),None,'')
        addDir('Search',onechannel_base,9,art_('Search','Sub Menus'),None,'')
        set_view('list')

def IMDbcat():
        addDir('In Theaters',IMDbIT_url,15,art_('In Theaters','Sub Menus'),None,'')
        addDir('Top 250',IMDb250_url,17,art_('Top 250','Sub Menus'),None,'')
        addDir('IMDb',movie_url,'',icon,None,'')
        addDir('IMDb watchlist',movie_url,13,art_('IMDb watchlist','Sub Menus'),None,'')
        addDir('Search',movie_url,9,art_('Search','Sub Menus'),None,'')
        set_view('list')

def MUSICcat():
        addDir('Lastest',onechannel_lastest,20,art_('Lastest','Sub Menus'),None,'')
        addDir('Featured',onechannel_featured,18,art_('Featured','Sub Menus'),None,'')
        addDir('Popular',onechannel_popular,22,art_('Popular','Sub Menus'),None,'')
        addDir('Ratings',onechannel_ratings,24,art_('Ratings','Sub Menus'),None,'')
        addDir('Release Date',onechannel_releasedate,26,art_('Release Date','Sub Menus'),None,'')
                                                                          
def MOVIESgene(url):#  cause mode is empty in this one it will go back to first directory
        addDir('Action',movie_url,'',icon,None,'')
                
def TVSHOWSgene(url):#  cause mode is empty in this one it will go back to first directory
        addDir('Action',tv_url,'',icon,None,'')

##############################################################################################################################

def NZBmovie(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match =  re.compile('<h3> <a href="(.+?)" class="movie-title" title=".+?">(.+?)</a> </h3>.+?<div class="poster">.+?<img src="(.+?)">',re.DOTALL).findall(link)
        for url, name, thumbnail in match:
                addDir(name,url,12,thumbnail,'')
        nextpage = re.compile('<span class="next">.+?<a href="(.+?)">Next</a>',re.DOTALL).findall(link)
        if nextpage:
                addDir('[COLOR blue]Next Page >>[/COLOR]','http://www.nzbmovieseeker.com'+nextpage[0],12,thumbnail,'')

def IMDbInTheaters(url):
        EnableMeta = local.getSetting('Enable-Meta')
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match =  re.compile('<div class=".+?">\n<img class=".+?"\nheight="209"\nwidth="140"\nalt=".+?"\ntitle="(.+?)"\nsrc="(.+?)"\nitemprop="image" />\n</div>').findall(link)
        for name, thumbnail in match:
                if EnableMeta == 'true':  addDir(name.encode('UTF-8','ignore'),url,12,'','Movie','Movies')
		if EnableMeta == 'false': addDir(name.encode('UTF-8','ignore'),url,12,thumbnail,None,'Movies')

def IMDbrate(url):
        EnableMeta = local.getSetting('Enable-Meta')
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match = re.compile('<a href="(.+?)" title="(.+?)"><img src=".+?" height="74" width="54" alt=".+?" title=".+?"></a>').findall(link)
        for url, name in match:
                if EnableMeta == 'true':  addDir(name.encode('UTF-8','ignore'),url,12,'','Movie','Movies')
		if EnableMeta == 'false': addDir(name.encode('UTF-8','ignore'),url,12,thumbnail,None,'Movies')
        nextpage = re.compile('<a href="(.+?)">Next.+?</a>').findall(link)
        if nextpage:
                addDir('[COLOR blue]Next Page >>[/COLOR]','http://www.imdb.com/'+nextpage[0],17,'',None,'')

def onechannelmfeature(url):
        EnableMeta = local.getSetting('Enable-Meta')
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match =  re.compile('<a href="(.+?)" title="Watch (.+?)"><img src="(.+?)" border="0" width="150" height="225" alt=".+?"><h2>.+?</h2></a>').findall(link)
        for url, name, thumbnail in match:
                if EnableMeta == 'true':  addDir(name.encode('UTF-8','ignore'),url,12,'','Movie','Movies')
		if EnableMeta == 'false': addDir(name.encode('UTF-8','ignore'),url,12,thumbnail,None,'Movies')
        nextpage = re.compile('<div class="pagination">.+?class=current>.+?href="(.+?)">.+?<a href=".+?">.+?</a>.+?<a href=".+?">.+?</div>',re.DOTALL).findall(link)
        if nextpage:
                addDir('[COLOR blue]Next Page >>[/COLOR]','http://www.primewire.ag'+nextpage[0],18,'',None,'')

def onechanneltvfeature(url):
        EnableMeta = local.getSetting('Enable-Meta')
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match =  re.compile('<a href="(.+?)" title="Watch (.+?)"><img src="(.+?)" border="0" width="150" height="225" alt=".+?"><h2>.+?</h2></a>').findall(link)
        for url, name, thumbnail in match:
                if EnableMeta == 'true': addDir(name.encode('UTF-8','ignore'),url,30,'','tvshows','TV-Shows')
		if EnableMeta == 'false': addDir(name.encode('UTF-8','ignore'),url,30,'',None,'TV-Shows')
        nextpage = re.compile('<div class="pagination">.+?class=current>.+?href="(.+?)">.+?<a href=".+?">.+?</a>.+?<a href=".+?">.+?</div>',re.DOTALL).findall(link)
        if nextpage:
                addDir('[COLOR blue]Next Page >>[/COLOR]','http://www.primewire.ag'+nextpage[0],18,'',None,'')
        set_view('tvshows') 

def onechannellastest(url):
        EnableMeta = local.getSetting('Enable-Meta')
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match =  re.compile('<a href="(.+?)" title="Watch (.+?)"><img src="(.+?)" border="0" width="150" height="225" alt=".+?"><h2>.+?</h2></a>').findall(link)
        for url, name, thumbnail in match:
                if EnableMeta == 'true':  addDir(name.encode('UTF-8','ignore'),url,12,'','Movie','Movies')
		if EnableMeta == 'false': addDir(name.encode('UTF-8','ignore'),url,12,thumbnail,None,'Movies')
        nextpage = re.compile('<div class="pagination">.+?class=current>.+?href="(.+?)">.+?<a href=".+?">.+?</a>.+?<a href=".+?">.+?</div>',re.DOTALL).findall(link)
        if nextpage:
                addDir('[COLOR blue]Next Page >>[/COLOR]','http://www.primewire.ag'+nextpage[0],18,'',None,'')

def onechannellastesttv(url):
        EnableMeta = local.getSetting('Enable-Meta')
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match =  re.compile('<a href="(.+?)" title="Watch (.+?)"><img src="(.+?)" border="0" width="150" height="225" alt=".+?"><h2>.+?</h2></a>').findall(link)
        for url, name, thumbnail in match:
                if EnableMeta == 'true': addDir(name.encode('UTF-8','ignore'),url,30,'','tvshows','TV-Shows')
		if EnableMeta == 'false': addDir(name.encode('UTF-8','ignore'),url,30,'',None,'TV-Shows')
        nextpage = re.compile('<div class="pagination">.+?class=current>.+?href="(.+?)">.+?<a href=".+?">.+?</a>.+?<a href=".+?">.+?</div>',re.DOTALL).findall(link)
        if nextpage:
                addDir('[COLOR blue]Next Page >>[/COLOR]','http://www.primewire.ag'+nextpage[0],18,'',None,'')
        set_view('tvshows')

def onechannelmpopular(url):
        EnableMeta = local.getSetting('Enable-Meta')
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match =  re.compile('<a href="(.+?)" title="Watch (.+?)"><img src="(.+?)" border="0" width="150" height="225" alt=".+?"><h2>.+?</h2></a>').findall(link)
        for url, name, thumbnail in match:
                if EnableMeta == 'true':  addDir(name.encode('UTF-8','ignore'),url,12,'','Movie','Movies')
		if EnableMeta == 'false': addDir(name.encode('UTF-8','ignore'),url,12,thumbnail,None,'Movies')
        nextpage = re.compile('<div class="pagination">.+?class=current>.+?href="(.+?)">.+?<a href=".+?">.+?</a>.+?<a href=".+?">.+?</div>',re.DOTALL).findall(link)
        if nextpage:
                addDir('[COLOR blue]Next Page >>[/COLOR]','http://www.primewire.ag'+nextpage[0],18,'',None,'')

def onechanneltvpopular(url):
        EnableMeta = local.getSetting('Enable-Meta')
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match =  re.compile('<a href="(.+?)" title="Watch (.+?)"><img src="(.+?)" border="0" width="150" height="225" alt=".+?"><h2>.+?</h2></a>').findall(link)
        for url, name, thumbnail in match:
                if EnableMeta == 'true': addDir(name.encode('UTF-8','ignore'),url,30,'','tvshows','TV-Shows')
		if EnableMeta == 'false': addDir(name.encode('UTF-8','ignore'),url,30,'',None,'TV-Shows')
        nextpage = re.compile('<div class="pagination">.+?class=current>.+?href="(.+?)">.+?<a href=".+?">.+?</a>.+?<a href=".+?">.+?</div>',re.DOTALL).findall(link)
        if nextpage:
                addDir('[COLOR blue]Next Page >>[/COLOR]','http://www.primewire.ag'+nextpage[0],18,'',None,'')
        set_view('tvshows')

def onechannelmratings(url):
        EnableMeta = local.getSetting('Enable-Meta')
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match =  re.compile('<a href="(.+?)" title="Watch (.+?)"><img src="(.+?)" border="0" width="150" height="225" alt=".+?"><h2>.+?</h2></a>').findall(link)
        for url, name, thumbnail in match:
                if EnableMeta == 'true':  addDir(name.encode('UTF-8','ignore'),url,12,'','Movie','Movies')
		if EnableMeta == 'false': addDir(name.encode('UTF-8','ignore'),url,12,thumbnail,None,'Movies')
        nextpage = re.compile('<div class="pagination">.+?class=current>.+?href="(.+?)">.+?<a href=".+?">.+?</a>.+?<a href=".+?">.+?</div>',re.DOTALL).findall(link)
        if nextpage:
                addDir('[COLOR blue]Next Page >>[/COLOR]','http://www.primewire.ag'+nextpage[0],18,'',None,'')

def onechanneltvratings(url):
        EnableMeta = local.getSetting('Enable-Meta')
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match =  re.compile('<a href="(.+?)" title="Watch (.+?)"><img src="(.+?)" border="0" width="150" height="225" alt=".+?"><h2>.+?</h2></a>').findall(link)
        for url, name, thumbnail in match:
                if EnableMeta == 'true': addDir(name.encode('UTF-8','ignore'),url,30,'','tvshows','TV-Shows')
		if EnableMeta == 'false': addDir(name.encode('UTF-8','ignore'),url,30,'',None,'TV-Shows')
        nextpage = re.compile('<div class="pagination">.+?class=current>.+?href="(.+?)">.+?<a href=".+?">.+?</a>.+?<a href=".+?">.+?</div>',re.DOTALL).findall(link)
        if nextpage:
                addDir('[COLOR blue]Next Page >>[/COLOR]','http://www.primewire.ag'+nextpage[0],18,'',None,'')
        set_view('tvshows')

def onechannelmreleasedate(url):
        EnableMeta = local.getSetting('Enable-Meta')
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match =  re.compile('<a href="(.+?)" title="Watch (.+?)"><img src="(.+?)" border="0" width="150" height="225" alt=".+?"><h2>.+?</h2></a>').findall(link)
        for url, name, thumbnail in match:
                if EnableMeta == 'true':  addDir(name.encode('UTF-8','ignore'),url,12,'','Movie','Movies')
		if EnableMeta == 'false': addDir(name.encode('UTF-8','ignore'),url,12,thumbnail,None,'Movies')
        nextpage = re.compile('<div class="pagination">.+?class=current>.+?href="(.+?)">.+?<a href=".+?">.+?</a>.+?<a href=".+?">.+?</div>',re.DOTALL).findall(link)
        if nextpage:
                addDir('[COLOR blue]Next Page >>[/COLOR]','http://www.primewire.ag'+nextpage[0],18,'',None,'')

def onechanneltvreleasedate(url):
        EnableMeta = local.getSetting('Enable-Meta')
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match =  re.compile('<a href="(.+?)" title="Watch (.+?)"><img src="(.+?)" border="0" width="150" height="225" alt=".+?"><h2>.+?</h2></a>').findall(link)
        for url, name, thumbnail in match:
                if EnableMeta == 'true': addDir(name.encode('UTF-8','ignore'),url,30,'','tvshows','TV-Shows')
		if EnableMeta == 'false': addDir(name.encode('UTF-8','ignore'),url,30,'',None,'TV-Shows')
        nextpage = re.compile('<div class="pagination">.+?class=current>.+?href="(.+?)">.+?<a href=".+?">.+?</a>.+?<a href=".+?">.+?</div>',re.DOTALL).findall(link)
        if nextpage:
                addDir('[COLOR blue]Next Page >>[/COLOR]','http://www.primewire.ag'+nextpage[0],18,'',None,'')
        set_view('tvshows')
                


####################################################################################################################################################################################                
                         
def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link = response.read()
    response.close()
    return link

def add_executeaddons(name):
        search = name
        addons_name = []
        addons_context = []
        if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.icefilms'):
                addons_name.append('IceFilms')
                addons_context.append('plugin://plugin.video.icefilms/?mode=555&url=http://www.icefilms.info/&search='+search+'&nextPage=1')
        if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.1channel'):
                addons_name.append('1channel (Movies)')
                addons_context.append('plugin://plugin.video.1channel/?mode=GetSearchQuery&section=&title=planes')
        if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.alluc'):
                addons_name.append('Alluc')
                addons_context.append('plugin://plugin.video.alluc/?mode=22&url=url&name='+name)
        if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.movie25'):
                addons_name.append('Mashup')
                addons_context.append('plugin://plugin.video.movie25/?mode=4&url='+name)
        if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.whatthefurk'):
                addons_name.append('WhatTheFurk')
                addons_context.append('plugin://plugin.video.whatthefurk/?mode=imdb result menu&url=url&name='+name)
        if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.theroyalwe'):
                addons_name.append('TheRoyalWe (Movies)')
                addons_context.append('plugin://plugin.video.theroyalwe/?mode=1250&url='+name+'')
        if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.OCM'):
                addons_name.append('OCM')
                addons_context.append('plugin://plugin.video.OCM/?mode=Search&url='+name)
        if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.moviekingdom'):
                addons_name.append('MovieKingdom')
                addons_context.append('plugin://plugin.video.moviekingdom/?mode=200&url='+name+'&imdb=SRO')

        
        dialog = xbmcgui.Dialog()
        ret = dialog.select('Search For "'+search.title()+'" At The Addons Below', addons_name)
        if ret == -1:
                return
        contextommand = addons_context[ret]
        xbmc.executebuiltin('Container.Update('+contextommand+')')
        

def add_executeaddonstv(name):
        search = name
        addons_name = []
        addons_context = []
        if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.icefilms'):
                addons_name.append('IceFilms')
                addons_context.append('plugin://plugin.video.icefilms/?mode=555&url=http://www.icefilms.info/&search='+search+'&nextPage=1')
        if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.1channel'):
                addons_name.append('1channel (Tv)')
                addons_context.append('plugin://plugin.video.1channel/?mode=GetSearchQuery&section=tv&title='+search)
        if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.iwatchonline'):
                addons_name.append('IwatchOnline (Tv)')
                addons_context.append('plugin://plugin.video.iwatchonline/?mode=Search&query=wentworth&searchin=t')#&searchin=t')
        if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.projectfreetv'):
                addons_name.append('ProjectFreeTv')
                addons_context.append('projectfreetv/?mode=search&url=url&name='+search)
        if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.movie25'):
                addons_name.append('Rlsmix (TV)')
                addons_context.append('movie25/?mode=137&url='+name)
        if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.tubeplus'):
                addons_name.append('TubePlus')
                addons_context.append('plugin://plugin.video.tubeplus/?mode=130&url=url&name='+name)
        if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.alluc'):
                addons_name.append('Alluc')
                addons_context.append('plugin://plugin.video.alluc/?mode=22&url=url&name='+name)
        if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.whatthefurk'):
                addons_name.append('WhatTheFurk')
                addons_context.append('plugin://plugin.video.whatthefurk/?mode=imdb result menu&url=url&name='+name)
        if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.theroyalwe'):
                addons_name.append('TheRoyalWe (TV)')
                addons_context.append('plugin://plugin.video.theroyalwe/?mode=1150&url='+name+'')
        if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.tv-release'):
                addons_name.append('TV-Release (TV)')
                addons_context.append('plugin://plugin.video.tv-release/?mode=20&url=url&name='+name)
        if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.hdtv-release'):
                addons_name.append('HDTV-Release (TV)')
                addons_context.append('plugin://plugin.video.hdtv-release/?mode=GetSearchQuery&url='+name)

        
        dialog = xbmcgui.Dialog()
        ret = dialog.select('Search For "'+search.title()+'" At The Addons Below', addons_name)
        if ret == -1:
                return
        contextommand = addons_context[ret]
        xbmc.executebuiltin('Container.Update('+contextommand+')')
       


#title = _OA.queries.get('title', '')
#video_type = _OA.queries.get('video_type', '')

def IMDB_LISTS(url):
        IMDBTV_WATCHLIST = "http://www.imdb.com/user/" + local.getSetting+('imdb_user') + "/watchlist?start=1&view=grid&sort=listorian:asc&defaults=1"
        addDir('Watch List',IMDBTV_WATCHLIST,12,addonfolder + artfolder + 'IMDB.png','')
        if settingsfile+('imdb_user') == 'ur********':
                xbmcgui.Dialog().ok('The Collective Information','You Need To Input Your IMDb Number Into ','Addon Settings')
        if settingsfile+('message') == 'false':
                xbmcgui.Dialog().ok('The Collective Information','            For Full Support For This Plugin Please Visit','                    [COLOR yellow][B]WWW.XBMCHUB.COM[/B][/COLOR]','Please Turn Off Message in Addon Settings')
        url=IMDB_LIST
        link=OPEN_URL(url)
        match = re.compile('<div class="list_name"><b><a    onclick=".+?"     href="(.+?)"    >(.+?)</a>').findall(link)
        for url, name in match:
            url='http://www.imdb.com'+str(url)+'?start=1&view=grid&sort=listorian:asc&defaults=1'   
            addDir(name,url,12,addonfolder + artfolder + 'IMDB.png','')    
            setView('movies', 'default-view')

def WATCH_TV_LIST(url):
        link=OPEN_URL(url)
        link=str(link).replace('\n','').replace('src="http://i.media-imdb.com/images/SFaa265aa19162c9e4f3781fbae59f856d/nopicture/medium/film.png" ','')
        link=link.split('<div class="list grid">')[1]
        link=link.split('<div class="see-more">')[0]
        match=re.compile('''src="(.+?)".+?<a href="(.+?)">(.+?)</a>''').findall(link)
        for iconimage, url, name in match:
            if re.search('V1', iconimage, re.IGNORECASE):
                regex=re.compile('(.+?)_V1.+?.jpg')
                match = regex.search(iconimage)
                iconimage='%s_V1_.SX593_SY799_.jpg'%(match.group(1))
                fanart=str(iconimage).replace('_.SX593_SY799_','')
            else:
                fanart='None'
            url = 'http://www.imdb.com'+str(url)
            name=str(name).replace('&#xB7;','').replace('&#x27;','').replace('&#x26;','And').replace(':','')
            series=str(name)
            description=''
            addDir(name,url,24,iconimage,fanart,series,description,'')   
            setView('movies', 'movies-view')



#def imdbtv_watchlist_url():
    #return "http://www.imdb.com/user/" + settingsfile.getSetting('imdb_user') + "/watchlist?start=1&view=grid&sort=listorian:asc&defaults=1"
    
#def imdb_list_url():
    #return 'http://www.imdb.com/user/' + settingsfile.getSetting('imdb_user') + '/lists?tab=public'
    
    
################################################################################################################################################################
        
def Searchmovies(url):
        EnableMeta = local.getSetting('Enable-Meta')
        searchStr = ''
        keyboard = xbmc.Keyboard(searchStr, "Search")
        keyboard.doModal()
        if (keyboard.isConfirmed() == False):
                return
        searchstring = keyboard.getText()
        if len(searchstring) == 0:
                return
        newStr = searchstring.replace(' ','%20')
        link = OPEN_URL(url+'/index.php?search_keywords='+newStr+'&key=fdd6063da4415536&search_section=1')
        match =  re.compile('<a href="(.+?)" title="Watch (.+?)"><img src="(.+?)" border="0" width="150" height="225" alt=".+?"><h2>.+?</h2></a>').findall(link)
        for url, name, thumbnail in match:
                if EnableMeta == 'true':  addDir(name.encode('UTF-8','ignore'),url,12,'','Movie','Movies')
		if EnableMeta == 'false': addDir(name.encode('UTF-8','ignore'),url,12,thumbnail,None,'Movies')
        #setView('movies', 'default')

def Searchtvshows(url):
        EnableMeta = local.getSetting('Enable-Meta')
        searchStr = ''
        keyboard = xbmc.Keyboard(searchStr, "Search")
        keyboard.doModal()
        if (keyboard.isConfirmed() == False):
                return
        searchstring = keyboard.getText()
        if len(searchstring) == 0:
                return
        newStr = searchstring.replace(' ','%20')
        link = OPEN_URL(url+'/index.php?search_keywords='+newStr+'&key=fdd6063da4415536&search_section=2')
        match =  re.compile('<a href="(.+?)" title="Watch (.+?)"><img src="(.+?)" border="0" width="150" height="225" alt=".+?"><h2>.+?</h2></a>').findall(link)
        for url, name, thumbnail in match:
                if EnableMeta == 'true': addDir(name.encode('UTF-8','ignore'),url,30,'','tvshows','TV-Shows')
		if EnableMeta == 'false': addDir(name.encode('UTF-8','ignore'),url,30,'',None,'TV-Shows')
        #setView('movies', 'default')

def IMDbSearch(url):
        EnableMeta = local.getSetting('Enable-Meta')
        searchStr = ''
        keyboard = xbmc.Keyboard(searchStr, "Search")
        keyboard.doModal()
        if (keyboard.isConfirmed() == False):
                return
        searchstring = keyboard.getText()
        if len(searchstring) == 0:
                return
        newStr = searchstring.replace(' ','%20')
        link = OPEN_URL(url+'/index.php?search_keywords='+newStr+'&key=fdd6063da4415536&search_section=2')
        match =  re.compile('<a href="(.+?)" title="Watch (.+?)"><img src="(.+?)" border="0" width="150" height="225" alt=".+?"><h2>.+?</h2></a>').findall(link)
        for url, name, thumbnail in match:
                if EnableMeta == 'true':  addDir(name.encode('UTF-8','ignore'),url,12,'','Movie','Movies')
		if EnableMeta == 'false': addDir(name.encode('UTF-8','ignore'),url,12,thumbnail,None,'Movies')
        #setView('movies', 'default')

def TVDBSearch(url):
        EnableMeta = local.getSetting('Enable-Meta')
        searchStr = ''
        keyboard = xbmc.Keyboard(searchStr, "Search")
        keyboard.doModal()
        if (keyboard.isConfirmed() == False):
                return
        searchstring = keyboard.getText()
        if len(searchstring) == 0:
                return
        newStr = searchstring.replace(' ','%20')
        link = OPEN_URL(url+'/index.php?search_keywords='+newStr+'&key=fdd6063da4415536&search_section=2')
        match =  re.compile('<a href="(.+?)" title="Watch (.+?)"><img src="(.+?)" border="0" width="150" height="225" alt=".+?"><h2>.+?</h2></a>').findall(link)
        for url, name, thumbnail in match:
                if EnableMeta == 'true':  addDir(name.encode('UTF-8','ignore'),url,30,'','Movie','Movies')
		if EnableMeta == 'false': addDir(name.encode('UTF-8','ignore'),url,30,thumbnail,None,'Movies')
        setView('movies', 'default')

#######################################################################################################################################################################

def get_params():
	param=[]
	paramstring=sys.argv[2]
	if len(paramstring)>=2:
		params=sys.argv[2]
		cleanedparams=params.replace('?','')
		if (params[len(params)-1]=='/'): params=params[0:len(params)-2]
		pairsofparams=cleanedparams.split('&')
		param={}
		for i in range(len(pairsofparams)):
			splitparams={}
			splitparams=pairsofparams[i].split('=')
			if (len(splitparams))==2: param[splitparams[0]]=splitparams[1]
	return param

def addLink(name,url,iconimage):
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
	return ok


def addDir(name,url,mode,iconimage,types,favtype):
	ok=True
	type = types
	if type != None: infoLabels = GRABMETA(name,types)
	else: infoLabels = {'title':name}
	try: img = infoLabels['cover_url']
	except: img= iconimage
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=img)
	liz.setInfo( type="Video", infoLabels= infoLabels)
	try: liz.setProperty( "Fanart_Image", infoLabels['backdrop_url'] )
	except: t=''
	contextMenuItems = []
	contextMenuItems.append(('Movie Information', 'XBMC.Action(Info)'))
	liz.addContextMenuItems(contextMenuItems, replaceItems=False)
	#Universal Favorites
	if 'Movies' in favtype:
		contextMenuItems.append(('Add to Favorites', fav.add_directory(name, u, section_title='Movies')))
		liz.addContextMenuItems(contextMenuItems, replaceItems=True)
	elif 'TV-Shows' in favtype:
		contextMenuItems.append(('Add to Favorites', fav.add_directory(name, u, section_title='TV-Shows')))
		liz.addContextMenuItems(contextMenuItems, replaceItems=True)
	else:
		contextMenuItems.append(('Add to Favorites', fav.add_directory(name, u, section_title='Other Favorites')))
		liz.addContextMenuItems(contextMenuItems, replaceItems=True)
	
#####################################################################################################################################################################
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
	return ok

params=get_params()
url=None; name=None; mode=None

try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: mode=int(params["mode"])
except: pass

print "Mode: "+str(mode); print "URL: "+str(url); print "Name: "+str(name)
   
        
#these are the modes which tells the plugin where to go
if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
        print ""+url
        NZBmovie(url)

elif mode==2:
        print ""+url
        TVSHOWScat()
        
elif mode==3:
        print ""+url
        MOVIEScat()

elif mode==4:
        print ""+url
        MOVIESgene(url)

elif mode==5:
        print ""+url
        TVSHOWSgene(url)

elif mode==6:
        print ""+url
        OPEN_URL(url)

elif mode==7:
        print ""+url
        getTorrents(url, page)
                
elif mode==8:
        print ""+url
        Download(url)

elif mode==9:
        print ""+url
        Searchmovies(url)

elif mode==10:
        print ""+url
        OPEN_playercorefactory()

elif mode==11:
        print ''+url
        OPEN_URL(url)

elif mode==12:
        print ''+url
        add_executeaddons(name)

elif mode==13:
        print ''+url
        IMDB_LISTS(url)

elif mode==14:
        print ''+url
        WATCH_TV_LIST(url)

elif mode==15:
        print ''+url
        IMDbInTheaters(url)

elif mode==16:
        print ''+url
        IMDbcat()

elif mode==17:
        print ''+url
        IMDbrate(url)

elif mode==18:
        print ''+url
        onechannelmfeature(url)

elif mode==19:
        print ''+url
        onechanneltvfeature(url)

elif mode==20:
        print ''+url
        onechannellastest(url)

elif mode==21:
        print ''+url
        onechannellastesttv(url)

elif mode==22:
        print ''+url
        onechannelmpopular(url)

elif mode==23:
        print ''+url
        onechanneltvpopular(url)

elif mode==24:
        print ''+url
        onechannelmratings(url)

elif mode==25:
        print ''+url
        onechanneltvratings(url)

elif mode==26:
        print ''+url
        onechannelmreleasedate(url)

elif mode==27:
        print ''+url
        onechanneltvreleasedate(url)

elif mode==28:
        print ''+url
        Searchtvshows(url)

elif mode==29:
        print ''+url
        MUSICcat()

elif mode==30:
        print ''+url
        add_executeaddonstv(name)

elif mode==31:
        print ''+url
        TVDBSearch(url)

elif mode==32:
        print ''+url
        IMDbSearch(url)

elif mode==309:
        print ''+url
        addon.addon.openSettings()

                
xbmcplugin.endOfDirectory(int(sys.argv[1]))