"""Реализуем Алгоритм Дейкстры на практике
"""
#Реализуем граф при помощи вложенных хеш-таблиц:
graph = {}

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

#Реализуем таблицу стоимостей, которая будет обновляться по ходу работы проги.
#Стоимость перехода к финальному отрезку пока бесконечность.
infinity = float("inf")
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

#Создадим таблицу родителей:
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

#Массив отслеживания уже обработанных узлов(многократно нельзя обрабатывать)
processed = []

"""Перебираем все узлы в таблице стоимости. Если узел с наименьшей стоимостью из
уже выделенных и он еще не был обработан - он назначается новым узлом с
наименьшей стоимостью.
"""
#Функция для нахождения наименьшей стоимости пути
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

"""Ищем узел с наименьшей стоимостью среди не обработанных. Если все обработанны
цмкл завершается. Далее перебираем всех соседей текущего узла. Если к соседу
можно добраться быстрее через текущий узел - обновляем стоимость узла, и он
становится новым родителем для соседа. Помечаем узел как обработанный. Далее
ищем следующий узел для обработки и повторяем цикл
"""
#Сам алгоритм Дейкстры:
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)