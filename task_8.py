"""Завдання

Уявіть, що вам на технічному інтерв'ю дають наступну задачу, яку треба розв'язати за допомогою купи.

Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати по два за раз в один кабель, 
використовуючи з'єднувачі, у порядку, який призведе до найменших витрат. Витрати на з'єднання двох 
кабелів дорівнюють їхній сумі довжин, а загальні витрати дорівнюють сумі з'єднання всіх кабелів.

Завдання полягає в тому, щоб знайти порядок об'єднання, який мінімізує загальні витрати."""

import heapq

def minimize_cable_costs(cable_lengths):
    # Ініціалізуємо мінімальну купу з довжин кабелів
    heapq.heapify(cable_lengths)
    total_cost = 0

    # Допоки в купі більше одного кабеля
    while len(cable_lengths) > 1:
        # Видаляємо два кабелі з найменшою довжиною
        shortest_cable_1 = heapq.heappop(cable_lengths)
        shortest_cable_2 = heapq.heappop(cable_lengths)

        # Об'єднуємо кабелі
        combined_cable = shortest_cable_1 + shortest_cable_2

        # Додаємо витрати на об'єднання до загальних витрат
        total_cost += combined_cable

        # Додаємо новий об'єднаний кабель назад до купи
        heapq.heappush(cable_lengths, combined_cable)

    return total_cost

# Приклад використання
cable_lengths = [5, 4, 2, 8]
min_cost = minimize_cable_costs(cable_lengths)
print(f"Мінімальні загальні витрати на з'єднання кабелів: {min_cost}")