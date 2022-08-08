class Singleton(type):
    """
    Singleton namunasi bitta yaratish mexanizmini taqdim etadi
    va faqat bitta sinf ob'ekti,
    va unga global kirish nuqtasini taqdim etish.
    """
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class DBManager(metaclass=Singleton):
    """ 
    Ma'lumotlar bazasi bilan ishlash uchun sinf menejeri
    """

    def __init__(self):
        pass
