import requests
import logging

# ============================================================
# Задание 1. Настройка логирования
# ============================================================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def run_integration_test():
    # ПРАВИЛЬНЫЙ URL для успешного сценария
    base_url = "https://jsonplaceholder.typicode.com/posts"
    
    # НЕПРАВИЛЬНЫЙ URL для демонстрации сбоя (Шаг А)
    # Раскомментируйте строку ниже, чтобы показать красный лог ошибки:
    # base_url = "https://jsonplaceholder.typicode.com/postsss"

    payload = {
        "title": "Мой тестовый заказ",
        "body": "Описание заказа",
        "userId": 1
    }

    try:
        # --- Шаг 1: POST (создание) ---
        logger.info("Шаг 1: Отправляем POST-запрос для создания записи...")
        response_create = requests.post(base_url, json=payload, timeout=10)
        response_create.raise_for_status()

        data = response_create.json()
        logger.info(f"Сервер ответил: {data}")
        
        # ⚠️ ВАЖНО: jsonplaceholder не сохраняет данные реально. 
        # В реальном проекте здесь было бы: post_id = data["id"]
        # Но для успешной демо-проверки GET-запроса используем существующий ID (например, 1)
        post_id = 1  

        # --- Шаг 2: GET (получение по ID) ---
        logger.info(f"Шаг 2: Запрашиваем запись с ID={post_id} через GET...")
        response_get = requests.get(f"{base_url}/{post_id}", timeout=10)
        response_get.raise_for_status()

        get_data = response_get.json()
        logger.info(f"✅ Запись успешно получена: {get_data.get('title')}")
        logger.info("✅ Интеграционный тест пройден успешно!")

    except requests.exceptions.RequestException as e:
        logger.error(f"ОШИБКА СЕТИ: Не удалось связаться с сервером — {e}")
    except KeyError as e:
        logger.error(f"ОШИБКА СТРУКТУРЫ JSON: отсутствует ключ {e}")
    except ValueError as e:
        logger.error(f"ОШИБКА JSON: некорректный формат ответа — {e}")
    except Exception as e:
        logger.error(f"НЕИЗВЕСТНАЯ ОШИБКА: {e}")

if __name__ == "__main__":
    run_integration_test()
