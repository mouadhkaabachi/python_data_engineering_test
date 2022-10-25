def get_config():
    """
    Get config from config file
    """
    import yaml

    with open("config/config.yml", "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
