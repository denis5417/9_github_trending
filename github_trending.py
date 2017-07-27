import requests
import datetime


def get_info_about_trending_repositories(mon_date):
    parameters = {'q': 'created:>={}'.format(mon_date), 'sort': 'stars'}
    repos = requests.get("https://api.github.com/search/repositories", params=parameters)
    repos = repos.json()['items']
    repos_info = [(repo['name'], repo['html_url'], repo['open_issues']) for repo in repos]
    return repos_info


def get_closest_monday():
    monday_id = 1
    today = datetime.date.today()
    delta = datetime.timedelta(today.isoweekday() - monday_id)
    mon_date = today - delta
    return mon_date

if __name__ == '__main__':
    repo_quantity = 20
    mon_date = get_closest_monday()
    repos_info = get_info_about_trending_repositories(mon_date)[:repo_quantity]
    print("\n".join("{} | {} | {}".format(repo[0], repo[1], repo[2]) for repo in repos_info))
