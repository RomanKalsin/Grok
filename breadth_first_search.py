from collections import deque # Для создания очереди
def search(graph, name):
    search_queue = deque() # Создаем очередь
    search_queue += graph[name] 
    searched = [] # Для уже провренных элементов
    while search_queue:
        person = search_queue.popleft() # Вырезаем элемент из очереди
        if not person in searched: # Если Не провреялся проверяем элемент
            if person_is_need(person): # Функция с условием
                print(person + " I find them!")
                return True
            else:
                searched.append(person) # Добавляем в список проверенных
                search_queue += graph[person] # Добавляем связи текущего элемента
    print("I do not find them!")
    return False

def person_is_need(name):
    if len(name) == 5 and name[-1] == "a":
        return True
    else:
        return False
graph = {"Roman": ["Ira", "Kris", "Ivan"], 
        "Ira": ["Tanya", "Ylya"], 
        "Ivan": ["Maks", "Ilya"], 
        "Kris": [], "Tanya": [], "Ylya": [],
        "Maks": [], "Ilya": []}
search(graph, "Roman")
print(graph)