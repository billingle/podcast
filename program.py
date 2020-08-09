import service
import random


def main():
    show_header()
    service.download_info()
    print("there are {} episode.".format(service.get_latest_show_id()))
    display_results()


def display_results():
    start = random.randint(1, service.get_latest_show_id())
    end = service.get_latest_show_id() + 1

    for show_id in range(start, end):
        info = service.get_episode(show_id)
        print("{}. {}".format(info.show_id, info.title))


def show_header():
    print("Welcome to the talk python info downloader!")
    print()


if __name__ == '__main__':
    main()
