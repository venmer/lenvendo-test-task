class JsTestTask:
    def __init__(self, name, image, price):
        self.name = name
        self.image = image
        self.price = price

    @classmethod
    def from_dict(cls, js_test_task_dict):
        return cls(js_test_task_dict['name'],
                   js_test_task_dict['image'],
                   js_test_task_dict['price'])

    def __repr__(self):
        return f"name: {self.name}, image: {self.image}, price: {self.price}"
