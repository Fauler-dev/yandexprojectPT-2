# Заврикиди Глеб, 18 когорта — Дипломный проект. Инженер по тестированию +

# Практический блок - вторая часть:
Работа с базой данных 
Файл с запросами (DataBaseRequest.sql) лежит в корне репозитория 

**Задание 1**
Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 

Скриншот результата запроса BD1.jpg (в корне проекта)

**Задание 2**

Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
Для этого: выведи все трекеры заказов и их статусы. 
Статусы определяются по следующему правилу:
Если поле finished == true, то вывести статус 2.
Если поле canсelled == true, то вывести статус -1.
Если поле inDelivery == true, то вывести статус 1.
Для остальных случаев вывести 0.

Скриншот результата запроса BD2.jpg (так же в корне проекта)

**Автоматизация теста.**

**Во время создания теста использовался временный сервер:**
https://955b2364-1a01-43fb-ab19-1864331fb8c3.serverhub.praktikum-services.ru
Для запуска необходимо установить библиотеку **pytest**
Инструкция по запуску:
- Октрываем файл test.py в pyCharm
- Нажимаем на него правой кнопкой мыши и нажимаем RUN в открывшемся списке
 
Скриншот автоматизации  Autotest.png (корень проекта)
