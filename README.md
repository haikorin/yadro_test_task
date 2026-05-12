# yadro_test_task
### Тестовое задание для команды разработки внутренней инфраструктуры и платформ продуктов
---
#### Раздел 1
В связи с недоступностью сервиса httpstat.us использован альтернативный — tools-httpstatus.pickup-services.com. Актуальной информации о поддержке httpstat.us не нашлось
Публичные API не поддерживают корректный возврат 1xx статусов, полагаю ввиду ограничений протокола HTTP. Локальный mock-сервер не реализовывался как избыточный для данного раздела.

#### Раздел 2

Сборка образа:
```bash
docker build -t http-checker -f section_2/Dockerfile section_1/
```

Запуск и проверка:
```bash
docker run --name http-checker http-checker
docker logs http-checker
```

#### Раздел 3

Сборка и запуск:
```bash
cd ./section_3
ansible-playbook playbook.yml --ask-become-pass
```

#### Структура проекта
```
yadro_test_task/
│
├── README.md
├── section_1/                         # Раздел 1: Скрипт
│   ├── check_status.py
│   └── requirements.txt
│
├── section_2/                         # Раздел 2: Docker
│   └── Dockerfile
│
└── section_3/                         # Раздел 3: Ansible
    ├── ansible.cfg
    ├── inventory.ini
    └── playbook.yml
```
