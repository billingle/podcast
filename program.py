import service


def main():
    show_header()

    max_episodes = service.download_info()

    for show_id in range(1, max_episodes + 1):
        info = service.get_episode(show_id)
        print("{}. {}".format(info.show_id, info.title))


def show_header():
    print("Welcome to the talk python info downloader.")
    print()


if __name__ == '__main__':
    main()
