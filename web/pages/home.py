import streamlit as st


def home():
    st.title("🏠 Home")
    st.write(
        "This is a UI created using Streamlit. You can use this UI to test the API functionality."
    )

    st.markdown(
        """# ArticleAPI

- [Project description](#project-description)
- [How to launch a project](#how-to-launch-a-project)
- [API testing](#api-testing)
- [In the future](#in-the-future)

## Project Description

This is a small pet project to demonstrate my capabilities, knowledge and skills in creating REST, GraphQL and gRPC applications. In this project, I use technologies such as: 
- PostgreSQL
- MongoDB
- ElasticSearch

The project is an API developed in accordance with the best practices of REST. It is designed to be clear and easy to use. Here's what's worth noting:

- Following the principles of REST: The API structure is clear and logical, routes and methods (GET, POST, PUT, DELETE) are organized so that it is easy for developers to integrate them into their applications.

- Asynchronous approach: The API supports asynchronous request processing, which allows it to work efficiently even with a large number of connections. Asynchrony is used to interact with clients, but the database is processed synchronously to avoid unnecessary complications.

- Typing: The project code is fully typed, which makes it more readable and helps prevent errors.

- Working with data via Pydantic: All incoming and outgoing data is validated and serialized using Pydantic, which ensures reliability and convenience.

Authorization is not implemented well enough in the project, which makes it unreliable. This small disadvantage is due to the fact that the main focus of the development was on creating and improving the key functions of the application. I am aware of this problem, but I decided not to pay enough attention to it. Despite this, the focus on the main tasks allowed us to achieve high efficiency and functionality of the API.

The application also has gRPC support, which demonstrates the skills of working with high-performance interaction between services. Using gRPC makes it possible to efficiently organize data exchange in distributed systems, providing support for complex interaction scenarios.

In addition, GraphQL is integrated into the project, which emphasizes knowledge and experience in creating powerful and flexible APIs. GraphQL provides developers with the ability to make accurate queries to data, minimizing the unnecessary amount of information transmitted and increasing the speed of the application.

This application implements many modern technologies such as REST API, asynchronous queries, Python typing, Pydantic, gRPC and GraphQL support, which makes it flexible, scalable and thoughtful in terms of functionality. Despite this, the project has minor drawbacks, such as weak authorization and security issues, which I am aware of and plan to improve in the future.

Before completing the description, I would like to mention the optimization aspect separately. At the moment, working with the database and Elasticsearch remains not fully optimized. This leads to increased resource consumption. I am aware of this issue and plan to take the time to resolve it in order to improve the overall performance and efficiency of the application.

---
Это небольшой пет-проект для показания моих возможностей, знаний и умений в создании REST, GraphQL и gRPC приложений. В данном проекте я использую такие технологии как: 
- PostgreSQL
- MongoDB
- ElasticSearch

Проект представляет собой API, разработанное в соответствии с лучшими практиками REST. Оно построено так, чтобы быть понятным и удобным в использовании. Вот что стоит отметить:

- Следование принципам REST: Структура API четкая и логичная, маршруты и методы (GET, POST, PUT, DELETE) организованы так, чтобы разработчикам было просто интегрировать их в свои приложения.

- Асинхронный подход: API поддерживает асинхронную обработку запросов, что позволяет ему работать эффективно даже при большом количестве подключений. Асинхронность используется для взаимодействия с клиентами, но база данных обрабатывается синхронно, чтобы избежать лишних сложностей.

- Типизация: Код проекта полностью типизирован, что делает его более читаемым и помогает предотвращать ошибки.

- Работа с данными через Pydantic: Все входящие и исходящие данные проходят валидацию и сериализацию с помощью Pydantic, что обеспечивает надежность и удобство.

В проекте авторизация реализована недостаточно хорошо, что делает её ненадежной. Этот небольшой минус связан с тем, что основное внимание при разработке было уделено созданию и совершенствованию ключевых функций приложения. Я знаю о этой проблеме, но решил не уделять ей должного внимания Несмотря на это, акцент на основных задачах позволил добиться высокой эффективности и функциональности API.

В приложении также реализована поддержка gRPC, что демонстрирует навыки работы с высокопроизводительным взаимодействием между сервисами. Использование gRPC позволяет эффективно организовать обмен данными в распределённых системах, обеспечивая поддержку сложных сценариев взаимодействия.

Кроме того, в проект интегрирован GraphQL, что подчёркивает знания и опыт в создании мощных и гибких API. GraphQL предоставляет разработчикам возможность делать точные запросы к данным, минимизируя лишний объём передаваемой информации и повышая скорость работы приложения.

В этом приложении реализовано множество современных технологий, таких как REST API, асинхронные запросы, типизация с использованием Python, поддержка Pydantic, gRPC и GraphQL, что делает его гибким, масштабируемым и продуманным с точки зрения функциональности. Несмотря на это, проект имеет небольшие недостатки, такие как слабая авторизация и проблемы безопасности, которые я осознаю и планирую улучшить в будущем.

Перед завершением описания хочется отдельно отметить аспект оптимизации. На данный момент работа с базой данных и Elasticsearch остаётся не до конца оптимизированной. Это приводит к повышенному потреблению ресурсов. Я знаю об этой проблеме и планирую уделить время её решению, чтобы повысить общую производительность и эффективность приложения.

# How to launch a project
Download the project from GitHub:

```
git clone https://github.com/GwenB1ade/ArticleAPI
```

After that, we launch the Docker containers using the following command:

```
docker-compose up --build
```

Then we create a virtual environment and install all the necessary dependencies.:

```
python -m venv .venv
. .venv/bin/activate
pip3 install -r req.txt
```

After downloading the project, launching containers, and installing dependencies, you can launch the REST/GraphQL application using the following command:

```
python3 src/main.py run
```

If you need to run a gRPC application, use this command:

```
python3 src/main.py grpc
```
---
Скачиваем проект с GitHub:

```
git clone https://github.com/GwenB1ade/ArticleAPI
```

После этого запускаем Docker-контейнеры с помощью следующей команды:

```
docker-compose up --build
```

Затем создаём виртуальное окружение и устанавливаем все необходимые зависимости:

```
python -m venv .venv
. .venv/bin/activate
pip3 install -r req.txt
```

После загрузки проекта, запуска контейнеров и установки зависимостей можно запустить REST/GraphQL-приложение, используя следующую команду:

```
cd src
python3 main.py run
```

Если требуется запустить gRPC-приложение, используем эту команду:

```
python3 main.py grpc
```

# API Testing
URLs for testing and verifying REST/GraphQL handles:
- REST: http://127.0.0.1:8000/docs (or http://127.0.0.1:8000/redoc)
- GraphQL: http://127.0.0.1:8000/graphql

Use Postman to test gRPC. But if you want, you can install a UI for testing gRPC.
Installing the UI:

```
go install github.com/fullstorydev/grpcui/cmd/grpcui@latest
```

Launching the UI:
```
grpcui -proto src/api/gRPC/article.proto -plaintext localhost:50051
```

Learn more about installing grpcui [here](https://github.com/fullstorydev/grpcui)

# In the future
In the future, I would like to change/add the following:
- Secure work with user data. Working with the access token correctly
- Asynchronous work with the database
- Optimized database queries. Optimized article search in ElasticSearch

                
                """
    )


home()
