from flask import request, views, render_template, redirect, url_for
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd


class Index(views.MethodView):
    """- главная страница, авторизация пользователя """

    df = pd.DataFrame({'Слово': [], 'tf': [], 'idf': []})
    is_table = False

    def get(self):
        """- GET запрос"""
        return render_template('index.html', is_table=self.is_table, table=self.df.to_html())

    def post(self):
        """- POST запрос """
        # Получение и проверка загруженного файла
        if 'file' not in request.files:
            return redirect('/')

        file = request.files['file']

        if file.filename == '':
            return redirect('/')
        if not file:
            return redirect('/')

        # получить объект файла
        text = file.read().decode('utf-8')
        self.get_tf_idf(text)
        return redirect(url_for('index'))

    @classmethod
    def get_tf_idf(cls, text):
        """- Обрабатывает текстовый файл и возвращает DataFrame с результатами TF-IDF."""
        # Создание экземпляра TfidfVectorizer
        vectorizer = TfidfVectorizer()
        # Преобразование текста в матрицу TF-IDF
        tfidf_matrix = vectorizer.fit_transform([text])
        # Получение названий слов
        word_names = vectorizer.get_feature_names_out()
        # Вычисление TF и IDF
        tf = tfidf_matrix.toarray()[0]
        idf = vectorizer.idf_
        # Создание DataFrame
        # df = pd.DataFrame({'Слово': word_names, 'tf': tf, 'idf': idf})
        cls.df = pd.concat(
            [cls.df, pd.DataFrame.from_records({'Слово': word_names, 'tf': tf, 'idf': idf})], ignore_index=True)
        # Сортировка по idf в убывающем порядке
        cls.df.sort_values(by='idf', ascending=False)
        cls.is_table = True



