import service
import random


def main():
    show_header()

    max_episodes = service.download_info()

    display_results(max_episodes)


def display_results(mep):
    start = random.randint(1, 10)
    end = random.randint(20, mep + 1)

    for show_id in range(start, end):
        info = service.get_episode(show_id)
        print("{}. {}".format(info.show_id, info.title))


def show_header():
    print("Welcome to the talk python info downloader!")
    print()


if __name__ == '__main__':
    main()
