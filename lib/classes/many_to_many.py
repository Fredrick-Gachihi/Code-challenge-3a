class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name should be a string.")
        if len(name) == 0:
            raise ValueError("The name should have at least one character.")    
        self.name = name
        self.articles_list = []

    def articles(self):
        return self.articles_list

    def magazines(self):
        return [article.magazine for article in self.articles_list]

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self.articles_list.append(article)

    def topic_areas(self):
        return [article.magazine.category for article in self.articles_list]

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.articles_list = []

    def articles(self):
        return self.articles_list

    def contributors(self):
        return [article.author for article in self.articles_list]

    def article_titles(self):
        return [article.title for article in self.articles_list]

    def contributing_authors(self):
        author_count = {}
        for article in self.articles_list:
            author = article.author
            if author not in author_count:
                author_count[author] = 1
            else:
                author_count[author] += 1

        return [author for author, count in author_count.items() if count > 2]

