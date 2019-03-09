from pyPodcastParser.Podcast import Podcast
import requests
import datetime
import unicodedata
from flask import Flask
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app, '/')

"""
TODO:
o   Pod title
o   Pod description
o   Pod published date
o   Compare pod published date to today
o   Format "aired date" to be only the day -- no time
o   Lookup episode -- except can't get Ep 299.5
"""


@ask.launch
def launch():
    speech_output = "Welcome to the Drinkin' Bros. Podcast Skill. What would you like to ask?"
    reprompt = "You can ask: " + \
               "For the title, description, or air date of a specific episode " + \
               "or ask for when the most recent episode was released. " + \
               "What would you like to do?"
    return question(speech_output).reprompt(reprompt)


def pod_lookup(pod_num):
    url = 'https://drinkingbros.libsyn.com/rss'
    response = requests.get(url)
    podcast = Podcast(response.content)
    select_pod = podcast.items[pod_num]

    pod_title = select_pod.title

    pod_desc_uf = select_pod.description
    pod_desc_f1 = pod_desc_uf.split("<p>")
    # pod_desc_f2 = pod_desc_f1.normalize("NFKD", correct_desc_f1[1])
    pod_desc_f2 = pod_desc_f1[1]
    pod_desc_f3 = pod_desc_f2.replace("</p>", "")
    pod_desc = pod_desc_f3

    pod_date = select_pod.date_time.strftime('%Y-%m-%d')

    return pod_title, pod_desc, pod_date


@ask.intent('GetNewestEpisodeInfo')
def newest_episode():

    pod_title, pod_desc, pod_date = pod_lookup(pod_num = 0)

    speech_output = "The newest episode was " + pod_title + " and it aired on " + str(pod_date)
    return statement(speech_output)


@ask.intent('GetSpecificEpisodeInfo', convert={'episode_num': float})
def specific_episode(episode_num):

    def total_pods():
        url = 'https://drinkingbros.libsyn.com/rss'
        response = requests.get(url)
        podcast = Podcast(response.content)
        all_pods = podcast.items[:]
        return all_pods

    all_pods = total_pods()
    all_titles = []
    for pod in all_pods:
        all_titles.append(pod.title)
    all_titles.reverse()

    pod_nums = []
    for pod_title in all_titles:
        pod_title_split = pod_title.split(" ")
        try:
            pod_nums.append(float(pod_title_split[1]))
        except:
            pod_nums.append("n/a")

    try:
        pod_nums.reverse() #put back in right order from rss feed
        real_indx = pod_nums.index(episode_num)
        print(real_indx)
        pod_title, pod_desc, pod_date = pod_lookup(pod_num = real_indx)
        speech_output = pod_title + ".\n" + pod_desc + "\n" + "Aired on " + str(pod_date) + "."
    except:
        err = True
        speech_output = "I'm sorry there was an error."

    return statement(speech_output)


if __name__ == '__main__':
    app.run(debug=True)
