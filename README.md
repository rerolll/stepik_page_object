## Как запустить тесты:
- Клонировать репозиторий:
```
https://github.com/rerolll/stepik_page_object.git
```
- Перейти в папку тестов
```
cd/stepik_page_object
```
- Установить виртуальное окружение
```
python -m venv venv
```
- Активировать виртуальное окружение
```
source venv/Scripts/activate
```
- Установить зависимости
```
pip install -r requirements.txt
```
- Запустить тесты
```
pytest -v --tb=line --language=en -m need_review
pytest -v --tb=line
```
