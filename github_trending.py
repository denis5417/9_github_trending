import requests
import datetime


def get_info_about_trending_repositories(mon_date):
    repos = requests.get("https://api.github.com/search/repositories?q=created:>={}&sort=stars".format(mon_date))
    repos = repos.json()['items']
    return ["{} {} {}".format(repo['name'], repo['html_url'], str(repo['open_issues'])) for repo in repos]

def get_closest_monday():
    today = datetime.date.today()
    delta = datetime.timedelta(today.isoweekday() - 1)
    mon_date = today - delta
    return mon_date

if __name__ == '__main__':
    mon_date = get_closest_monday()
    links = get_info_about_trending_repositories(mon_date)
    print(*links[:20], sep="\n")

