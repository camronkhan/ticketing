import os

if os.getenv('ENV', default='local') == 'local':
    from dotenv import load_dotenv
    dotenv_path = os.path.abspath(os.path.join('..', '.env-local'))
    load_dotenv(dotenv_path=dotenv_path)

db = {
    'env': os.getenv('ENV'),
    'user': os.getenv('POSTGRES_USER'),
    'password': os.getenv('POSTGRES_PASSWORD'),
    'db': os.getenv('POSTGRES_DB'),
    'host': os.getenv('POSTGRES_HOST'),
    'port': os.getenv('POSTGRES_PORT')
}
