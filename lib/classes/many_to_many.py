class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str):#To ensure the name is a string
            raise TypeError("The name must be a string")
        if len(name) == 0:#To check characters of the name 
            raise ValueError("Type the auther's name")
        self.name = name

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise TypeError("Magazine name must be a string")
        if not (2 <= len(name) <= 16):
            raise ValueError("The name should be between 2 and 16 characters long")
        if not isinstance(category, str):
            raise TypeError("Magazine category must be a string")
        if len(category) == 0:
            raise ValueError("Magazine category must not be empty")
        self.name = name
        self.category = category


    @property
    def category(self):
        return self._category
    

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Magazine category must be a string")
        if len(value) == 0:
            raise ValueError("Magazine category must not be empty")
        self._category = value

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass