# Delivery
**Техническое задание на разработку службы доставки**

**1.Обзор проекта**

Цель проекта создание веб интерфейса для организации доставки. Пользователи должны иметь возможность заказать доставку через веб интерейс, а так же просматривать избранные товары. А администратор имеет возможность работать с товарами

**2.Функциональные требования**

2.1. Регистрация и аутенфикация пользователей
- Пользователи должны иметь возможность регистрироваться и входить в систему.
- Для аутентификации нужно ввести номер телефона, пароль, email, имя, фамилия.

2.2. Заказ Доставки
- Пользователи должны иметь возможность заказать доставку, указав место прибытия, место назначения и время.
- Администраторы должны иметь возможности удалять не нужные товары или добавлять их
- Система должна автоматически подбирать время прибытия товара.

2.3 Телеграм бот
- Пользователи должны иметь возможность просмотреть статус их заказов в телеграм боте

**3. Нефункциональные требования**

3.1. Безопасность

- Все данные пользователей должны быть защищены и храниться в безопасном месте.
- Система должна защищаться от SQL-инъекций и других типов атак.

3.2. Интерфейс

- Интерфейс должен быть простым и интуитивно понятным, чтобы пользователи могли легко находить нужную информацию.

**4. Технологический стек**

- Python
- React
- PostgreSQL
- HTML
- SCSS (препроцессор css)

**5. Порядок разработки**

5.1. Разработка архитектуры

- Определить базу данных и ее структуру.
- Разработать структуру проекта.

5.2. Разработка функционала

- Реализовать регистрацию и аутентификацию пользователей.
- Реализовать магазин товаров.
- Реализовать просмотр товаров добавленных в корзину.
- Реализовать возможность заказа корзины.
- Реализовать телеграм бота

5.3. Тестирование

- Протестировать все функции на наличие ошибок.
- Протестировать систему на наличие уязвимостей.

**6. Ответственные лица**

- Руководитель проекта – <!-- тут сам -->

**7 Заключение**

Проект "Служба Доставки" - это веб-сервис, который позволяет пользователям заказывать доставку, просматривать статус заказов, а администраторы работать с товарами сайта.