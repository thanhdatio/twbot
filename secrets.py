import yaml


def read_secrets():
    """
    With this function we can read secrets
    from the configuration file.
    """
    with open("config.yaml", "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            exit()