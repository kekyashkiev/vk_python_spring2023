"""Реализовать функцию predict_message_mood,
 которая приниамает на вход строку,
 экземпляр модели SomeModel и пороги хорошести."""


class SomeModel:
    def predict(self, message: str) -> float:
        pass


def predict_message_mood(message: str, model: SomeModel,
                         bad_thresholds: float = 0.3,
                         good_thresholds: float = 0.8) -> str:
    var = model.predict(message)
    if var < bad_thresholds:
        return 'неуд'
    return 'отл' if var > good_thresholds else 'норм'
