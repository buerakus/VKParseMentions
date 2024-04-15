import requests
import vk_api

access_token = ''
vk_session = vk_api.VkApi(token=access_token)
vk = vk_session.get_api()


def get_id(username):
    response = vk.utils.resolveScreenName(screen_name=username)
    if response:
        return response['object_id']
    return None


def main():
    print("Mentions parser: sends all available posts mentioned for a specified user")
    user_link = input("Enter link to user account: ")
    user_custom_id = user_link.split("/")[-1]
    user_id = get_id(user_custom_id)
    if user_id:
        mentions_link = f"https://vk.com/feed?obj={user_id}&section=mentions"
        print(f"Mentions link for {user_custom_id}: {mentions_link}")
        download_Page(mentions_link, user_id)
    else:
        print("Failed to retrieve user ID")


def download_Page(mentions_link, user_id):
    page = requests.get(mentions_link)
    with open(f'saved_pages/{user_id}.html', 'wb+') as f:
        f.write(page.content)


if __name__ == "__main__":
    main()
