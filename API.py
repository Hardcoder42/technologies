import requests

def get_repos(username):
    """
    Получает список репозиториев пользователя GitHub
    
    Параметры:
    username (str): Имя пользователя GitHub
    
    Возвращает:
    list: Список репозиториев, 
    None в случае ошибки  
    """
    
    url = f"https://api.github.com/users/{username}/repos"
    headers = {'User-Agent': 'MyGitHubApp/1.0'}
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print(f"Ошибка 404: Пользователь '{username}' не найден")
            return None
        elif response.status_code == 403:
            print("Ошибка 403: Превышен лимит запросов к API")
            return None
        else:
            print(f"Ошибка {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Ошибка подключения: {e}")
        return None


def analyze_repos(repos):
    """
    Анализирует данные о репозиториях и формирует статистику
    
    Параметры:
    repos (list): Список репозиториев
    
    Возвращает:
    dict: Словарь с аналитикой, 
    None если список пуст
    """
    
    if not repos:
        return None
    
    total_stars = 0
    languages = set()
    best_repo = None
    max_stars = -1
    
    for repo in repos:
        stars = repo['stargazers_count']
        total_stars += stars
        
        if repo['language']:
            languages.add(repo['language'])
        
        if stars > max_stars:
            max_stars = stars
            best_repo = repo
    
    return {
        'total_stars': total_stars,
        'repos_count': len(repos),
        'languages': list(languages),
        'best_repo': {
            'name': best_repo['name'] if best_repo else None,
            'stars': best_repo['stargazers_count'] if best_repo else 0
        }
    }


def main():
    """
    Основная функция программы
    
    Запрашивает имя пользователя, получает репозитории, выводит их и показывает статистику
    """
    username = input("Введите имя пользователя GitHub: ").strip()
    
    if not username:
        print("Имя пользователя не может быть пустым")
        return
    
    repos = get_repos(username)
    
    if repos is None:
        return
    
    if not repos:
        print(f"У пользователя {username} нет публичных репозиториев")
        return
    
    print(f"Репозитории пользователя {username}:")
    print("-" * 50)
    
    for repo in repos:
        print(f"\n   {repo['name']}")
        print(f"   Звезд: {repo['stargazers_count']}")
        print(f"   Язык: {repo['language'] or 'Не указан'}")
    
    analysis = analyze_repos(repos)
    
    if analysis:
        print("\n" + "=" * 50)
        print("   Статистика:")
        print(f"   Всего репозиториев: {analysis['repos_count']}")
        print(f"   Всего звезд: {analysis['total_stars']}")
        print(f"   Используемые языки: {', '.join(analysis['languages']) if analysis['languages'] else 'нет данных'}")
        
        if analysis['best_repo']['name']:
            print(f"\n   Лучший репозиторий: {analysis['best_repo']['name']} (⭐ {analysis['best_repo']['stars']} stars)")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n Программа прервана пользователем")