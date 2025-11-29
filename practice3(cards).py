import itertools
import pickle
import gzip


def create_deck():
    '''создает стандартную колоду карт в виде кортежей'''
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']  # достоинства
    suits = ['♥', '♦', '♣', '♠']  # масти
    return list(itertools.product(ranks, suits))  # создает все возможные пары, возврат кортеж


def display_deck(deck, limit=10):  # показ только первых 10карт
    '''выводит карты в формате "достоинство-масть"'''
    print(f"Колода карт: ")
    for i, card in enumerate(deck[:limit], 1):  # нумерация карт, начиная с первой
        print(f"{i:2d}. {card[0]}{card[1]}")  # выравнивание(число на 2 символа), достоинство[0]+масть[1]


def generate_combinations(deck, num_cards):
    '''генерирует комбинации карт с нужным количеством карт'''
    return list(itertools.combinations(deck, num_cards))  # получаем список комбинаций


def display_combinations(combinations, limit=10):  # список комбинаций, первые 10
    '''выводит комбинации в читаемом формате'''
    print(f"\nПервые {limit} комбинаций: ")
    for i, combo in enumerate(combinations[:limit], 1):  # нумерация каждой комбинации отдельно, начиная с 1
        # каждая комбинация это кортеж кортежей
        cards_str = " + ".join([f"{card[0]}{card[1]}" for card in combo])  # каждая карта=>str "2♥", "3♦", соединяем "+"
        print(f"{i:2d}. {cards_str}")  # вырванивание на 2 символа, карты в формате строки

def save_binary(deck, combinations_2,combinations_3):
    '''самый эффективный способ-бинарный формат'''
    data={
        'deck': deck,
        'combinations_2': combinations_2,
        'combinations_3': combinations_3,
        'metadata': {
            'total_cards': len(deck),
            'total_combinations_2': len(combinations_2),
            'total_combinations_3': len(combinations_3)
        }
    }
    #обычный pickle
    with open('cards_data.pkl', 'wb') as f:
        pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)

    #сжатый протокол
    with gzip.open('cards_data.pkl.gz', 'wb') as f:
        pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)

    print(f"Бинарные файлы созданы.")
    print(f"  • Комбинаций по 2 карты: {len(combinations_2):,}")
    print(f"  • Комбинаций по 3 карты: {len(combinations_3):,}")

def load_binary(filename):
    '''загружает данные из бинарного файла(обычный и сжатый)'''
    if filename.endswith('.gz'):
        with gzip.open(filename, 'rb') as f:
            return pickle.load(f)
    else:
        with open(filename, 'rb') as f:
            return pickle.load(f)


# основная программа
deck = create_deck()  # создание колоды
display_deck(deck)  # вывод колоды

# генерируем комбинации по 2 карты
combinations_2 = generate_combinations(deck, 2)  # создаем пары
print(f"\nВсего комбинаций по 2 карты: {len(combinations_2):,}")  # сколько пар?

display_combinations(combinations_2)  # показываем пары комбинаций

# попробуем комбинации по 3 карты
combinations_3 = generate_combinations(deck, 3)
print((f"\nВсего комбинаций по 3 карты: {len(combinations_3):,}"))
display_combinations(combinations_3)

#сохраняем в бинарный формат
save_binary(deck, combinations_2, combinations_3)

# загрузка из файла:
loaded_data = load_binary('cards_data.pkl.gz')
print(f"Загружено карт: {len(loaded_data['deck'])}")
print(f"Загружено комбинаций по 2: {len(loaded_data['combinations_2'])}")
print(f"Загружено комбинаций по 3: {len(loaded_data['combinations_3'])}")