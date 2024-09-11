import argparse
import os
from dotenv import load_dotenv
from storage_csv import StorageCsv
from storage_json import StorageJson
from movie_app import MovieApp

load_dotenv()


def main():
    """Main Function"""
    parser = argparse.ArgumentParser(description='Movie App with custom storage file')

    parser.add_argument('storage_file', type=str, help='The storage file for movie data (CSV or JSON)')

    args = parser.parse_args()

    _, file_extension = os.path.splitext(args.storage_file)

    if file_extension == '.json':
        storage = StorageJson(args.storage_file)
    elif file_extension == '.csv':
        storage = StorageCsv(args.storage_file)
    else:
        raise ValueError("Unsupported file format. Use either a JSON or CSV file.")

    api_key = os.getenv('OMDB_API_KEY')

    movie_app = MovieApp(storage, api_key)
    movie_app.run()


if __name__ == '__main__':
    main()
