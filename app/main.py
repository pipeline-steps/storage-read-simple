import argparse
from google.cloud import storage
from config import create_config


def main(config_path: str, output_path: str):
    # read configuration
    config = create_config(config_path)
    storage_client = storage.Client()
    bucket = storage_client.bucket(config.bucket)
    blob = bucket.blob(config.path)
    blob.download_to_filename(output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config_path", required=True)
    parser.add_argument("--output_path", required=True)
    args = vars(parser.parse_args())
    main(
        config_path=args["config_path"],
        output_path=args["output_path"]
    )
