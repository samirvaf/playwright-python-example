from faker import Faker

fake = Faker()


def make_order(**overrides) -> dict:
    order = {
        "name": fake.catch_phrase(),
        "lab_id": fake.unique.bothify("LAB-#####"),
        "client": fake.company(),
    }
    order.update(overrides)
    return order


def make_sample(**overrides) -> dict:
    sample = {
        "name": fake.bothify("Sample-#####"),
        "lab_id": fake.unique.bothify("S-#####"),
    }
    sample.update(overrides)
    return sample


def make_test(**overrides) -> dict:
    test = {
        "name": fake.bs().title() + " Test",
        "code": fake.bothify("TST-###"),
    }
    test.update(overrides)
    return test
