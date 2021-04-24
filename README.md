 Реализация Web приложения “Новости группы из VK”
Создать Django приложение, которое интегрируется с группой из VK (можно создать
свою) и получает все посты (раз в день или использовать webhook), которые публикует
владелец сообщества.
Сохранять пост в БД (если его нет, если есть, редактировать существующие записи):
- текст
- картинка (если есть)
- дата публикации
- ID сообщения из VK
- Ссылку на пост
Функции админ панели:
1) Просмотр записей постов, фильтр по дате, поиск по тексту
Функции REST API:
1) Получение списка новостей (должен быть pagination и фильтр по дате)
2) Получение одной новости по ID
