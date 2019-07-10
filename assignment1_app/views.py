from django.shortcuts import render
from assignment1_app.artist import Artist
from assignment1_app import tests
import json
import urllib,urllib.request
from assignment1_app.recursivejson import extract_values

# Create your views here.

def home(request):
    return render(request, 'index.html')

def data(request):
    return render(request,'data.html')  





###### the ABS data function ##############################

def abs (request):
    url= 'http://stat.data.abs.gov.au/sdmx-json/data/QBIS/50+70.B+C+D+F+G+H+TOTAL.0.99.10+20+30.Q/all?startTime=2018-Q2&endTime=2019-Q1&dimensionAtObservation=allDimensions'
    # url='https://jsonplaceholder.typicode.com/todos/1'
    json_obj= urllib.request.urlopen(url)
    data=json.load(json_obj)


### holy shit, so basically pass in (where 'Name' currently is) any key value you want the function to return from a JSON file ####

    names = extract_values(data,'name')
    observations = extract_values(data,'observation')


    page_data= {

        # 'data':data,
        'names': names,
        'observations': observations
     
     }

    return render (request, 'abs.html', page_data)

##########################################################


def artists_all(request):
    page_data = {'arts_list': create_artists() }
    return render(request, 'artists.html', page_data)


def artist_single(request, id):
    id = int(id)
    arts_list = create_artists()
    artist = None
    for item in arts_list:
        if item.id == id:
            artist = item
    page_data = {'artist': artist}
    print(artist)
    return render(request, 'artist_details.html', page_data)


def create_artists():
    the_list = []
    
    # the_list.append(Artist(1, 'John Coltrane', 'Jazz', , '26', False))

    the_list.append(Artist(1, 'John Coltrane', 'Jazz',"John William Coltrane was an American jazz saxophonist and composer. Working in the bebop and hard bop idioms early in his career, Coltrane helped pioneer the use of modes and was at the forefront of free jazz. He led at least fifty recording sessions and appeared on many albums by other musicians, including trumpeter Miles Davis and pianist Thelonious Monk. Over the course of his career, Coltrane's music took on an increasingly spiritual dimension.",'8',False))

    the_list.append(Artist(2, 'Meshuggah', 'Heavy Metal',"Meshuggah (/məˈʃʊɡə/) is a Swedish extreme metal band from Umeå, formed in 1987. Meshuggah's line-up consists of founding members vocalist Jens Kidman and lead guitarist Fredrik Thordendal, drummer Tomas Haake, who joined in 1990, rhythm guitarist Mårten Hagström, who joined in 1993 and bassist Dick Lövgren since 2004.Meshuggah first attracted international attention with the 1995 release Destroy Erase Improve for its fusion of fast-tempo death metal, thrash metal, progressive metal and jazz fusion elements." ,'8', False))

    the_list.append(Artist(3, 'Kendrick Lamar', 'Hip Hop',"Kendrick Lamar Duckworth (born June 17, 1987) is an American rapper, songwriter, and record producer. He is regarded as one of the most skillful and successful hip hop artists of his generation. Raised in Compton, California, Lamar embarked on his musical career as a teenager under the stage name K-Dot, releasing a mixtape that garnered local attention and led to his signing with indie record label Top Dawg Entertainment (TDE). He began to gain recognition in 2010, after his first retail release, Overly Dedicated.The following year, he independently released his first studio album, Section.80, which included his debut single, HiiiPoWeR. By that time, he had amassed a large online following and collaborated with several prominent hip hop artists, including The Game, Busta Rhymes, and Snoop Dogg." ,'4', False))

    the_list.append(Artist(4, 'Miles Davis', 'Jazz', "Miles Dewey Davis III (May 26, 1926 – September 28, 1991) was an American jazz trumpeter, bandleader, and composer. He is among the most influential and acclaimed figures in the history of jazz and 20th century music. Davis adopted a variety of musical directions in a five-decade career that kept him at the forefront of many major stylistic developments in jazz. Born and raised in Illinois, Davis left his studies at the Juilliard School in New York City and made his professional debut as a member of saxophonist Charlie Parkers bebop quintet from 1944 to 1948."  , '91', False))

    return the_list











