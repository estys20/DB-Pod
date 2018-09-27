from pyPodcastParser.Podcast import Podcast
import requests
import datetime
import unicodedata

"""
TODO:
o   Pod title
o   Pod description
o   Pod published date
o   Compare pod published date to today
x   Setup git repository
x   Git ignore for venv
x   Requirements file to install dependencies from
"""


def get_episode_info_old(url, episode):
    response = requests.get(url)
    podcast = Podcast(response.content)
    select_pod = podcast.items[episode]

    # invalid method since there are DB companion episodes & half episodes
    # l_pods = len(podcast.items)
    # print("\nTotal episodes: " + str(total_pods))

    pod_title = select_pod.title
    print("\nTitle: " + pod_title)

    pod_desc_uf = select_pod.description
    pod_desc_f1 = pod_desc_uf.split("<p>")
    print(pod_desc_f1)
    print(type(pod_desc_f1))
    pod_desc_f2 = unicodedata.normalize("NFKD", pod_desc_f1[1])
    pod_desc_f3 = pod_desc_f2.replace("</p>", "")
    pod_desc = pod_desc_f3
    print("\nDescription: " + pod_desc)

    pod_date = select_pod.date_time
    print("\nAir Date: " + str(pod_date))

    return

def episode_number(url, episode):
    response = requests.get(url)
    podcast = Podcast(response.content)
    new_pod = podcast.items[:]
    # print(len(new_pod))
    guess = podcast.items[len(new_pod)-episode]
    guess_title = guess.title
    title_split = guess_title.split(" ")
    guess_number = int(title_split[1])
    print("episode: " + str(episode))
    print("guess: " + str(guess_number))

    while guess_number != episode:
        if guess_number < episode:
            diff = episode-guess_number
            guess_number = guess_number + diff
        else:
            diff = guess_number-episode
            guess_number = guess_number - diff

        print("episode: " + str(episode))
        print("guess: " + str(guess_number))

    return



def check_newest_episode(url):
    response = requests.get(url)
    podcast = Podcast(response.content)
    new_pod = podcast.items[0]

    now = datetime.datetime.utcnow()
    print(str(now))
    pod0_date = new_pod.date_time
    date_diff = now - pod0_date
    print("\nDate Difference: " + str(date_diff))

    return date_diff


def get_episode_info_old2(episode_num):
    url = 'https://drinkingbros.libsyn.com/rss'
    response = requests.get(url)
    podcast = Podcast(response.content)
    all_pods = podcast.items[:]
    guess = podcast.items[len(all_pods)-episode_num]
    guess_title = guess.title
    title_split = guess_title.split(" ")
    guess_num = int(title_split[1])

    while guess_num != episode_num:
        if guess_num < episode_num:
            diff = episode_num - guess_num
            guess_num = guess_num + diff
        else:
            diff = guess_num - episode_num
            guess_num = guess_num - diff

    correct_pod = podcast.items[guess_num] #actually the right episode guess_number

    correct_pod_title = correct_pod.title

    correct_pod_desc_uf = correct_pod.description
    correct_pod_desc_f1 = correct_pod_desc_uf.split("<p>")
    # print(correct_pod_desc_f1)
    # correct_pod_desc_f2 = correct_pod_desc_f1.normalize("NFKD", correct_desc_f1[1])
    correct_pod_desc_f2 = correct_pod_desc_f1[1]
    correct_pod_desc_f3 = correct_pod_desc_f2.replace("</p>", "")
    correct_pod_desc = correct_pod_desc_f3

    print(correct_pod_desc)

    correct_pod_date = correct_pod.date_time.strftime('%Y-%m-%d')

    speech_output = correct_pod_title + "\n" + correct_pod_desc + "\n" + "Aired on: " + str(correct_pod_date)
    return statement(speech_output)


def get_episode_info()


if __name__ == '__main__':
    url = 'https://drinkingbros.libsyn.com/rss'
    episode_num = 13
    episode = episode_num
    # get_episode_info_old(url, episode)
    # check_newest_episode(url)
    # episode_number(url, episode)
    # get_episode_info(episode_num)
