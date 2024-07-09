class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self._author.add_articles(self)
        self._magazine.add_articles(self)
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        if not 5 <= len(title) <= 50:
            raise ValueError("Title must be between 5 and 50 characters.")
        if hasattr(self, '_title'):
            raise AttributeError("Title cannot be changed after instantiation.")
        self._title = title
    
    @property 
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author")
        self._author = author
    
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine")
        self._magazine = magazine
    

        
class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        if hasattr(self, '_name'):
            raise AttributeError("Name cannot be changed after instantiation.")
        self._name = name

    def articles(self):
        return self._articles
    
    def add_articles(self, article):
        if isinstance(article, Article):
            self._articles.append(article)
        else:
            raise TypeError("Must be of type Article")

    def magazines(self):
        unique_magazines = {article.magazine for article in self._articles}
        return list(unique_magazines)

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self._articles:
            return None
        unique_categories_set = {article.magazine.category for article in self._articles}
        return list(unique_categories_set)

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not 2 <= len(name) <= 16:
            raise ValueError("Name must be between 2 and 16 characters.")
        self._name = name
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if not isinstance(category, str):
            raise TypeError("Category must be a string.")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters.")
        self._category = category
    
    def add_articles(self, article):
        if isinstance(article, Article):
            self._articles.append(article)
        else:
            raise TypeError("Must be of type Article")
    
    def articles(self):
        return self._articles

    def contributors(self):
        unique_authors = {article.author for article in self._articles}
        return list(unique_authors) if unique_authors else None

    def article_titles(self):
        if not self._articles:
            return None
        unique_categories = list()
        for article in self._articles:
            if article.magazine: 
                unique_categories.append(article.title)
        return list(unique_categories)

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author = article.author
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1
        
        double_authors = [author for author, count in author_counts.items() if count > 2]

        if double_authors:
            return double_authors
        else:
            return None