from flask import request, jsonify
from flask.views import MethodView
from app import app, db
from validator import validate
from models import User, Article
from schema import USER_CREATE, ARTICLE_CREATE


class UserView(MethodView):

    def get(self, user_id):
        user = User.by_id(user_id)
        return jsonify(user.to_dict())

    @validate('json', USER_CREATE)
    def post(self):
        user = User(**request.json)
        user.set_password(request.json['password'])
        user.add()
        return jsonify(user.to_dict())


class ArticleView(MethodView):

    def get(self, article_id):
        article = Article.by_id(article_id)
        return jsonify(article.to_dict())

    @validate('json', ARTICLE_CREATE)
    def post(self):
        st = request.json
        user_id = st.pop('user')
        user = User.by_id(user_id)
        article = Article(**st)
        article.set_user(user)
        article.add()
        return jsonify(article.to_dict())

    # @validate('json', ARTICLE_CREATE)
    def put(self, article_id):
        article = Article.by_id(article_id)
        st = request.json
        for key, val in st.items():
            setattr(article, key, val)
        article.add()
        return jsonify(article.to_dict())

    def delete(self, article_id):
        article = Article.by_id(article_id)
        db.session.delete(article)
        db.session.commit()
        return jsonify(article.to_dict())

class ArticleViewAll(MethodView):
    def get(self):
        article = Article.query.all()
        serial_list = []
        for art in article:
            serial_list.append(art.to_dict())
        return jsonify(serial_list)


app.add_url_rule('/users/<int:user_id>', view_func=UserView.as_view('users_get'), methods=['GET', ])      # получить конкретного пользователя
app.add_url_rule('/users/', view_func=UserView.as_view('users_create'), methods=['POST', ])               # создает нового пользователя
app.add_url_rule('/articles/<int:article_id>', view_func=ArticleView.as_view('articles_get'), methods=['GET', ])  # получить конкретное объявление
app.add_url_rule('/articles/<int:article_id>', view_func=ArticleView.as_view('articles_put'), methods=['PUT', ])  #изменить конкретное объявление
app.add_url_rule('/articles/<int:article_id>', view_func=ArticleView.as_view('articles_delete'), methods=['DELETE', ]) #удаляет конкретное объявление
app.add_url_rule('/articles/', view_func=ArticleView.as_view('articles_create'), methods=['POST', ])      # создает новое объявление
app.add_url_rule('/articles/', view_func=ArticleViewAll.as_view('articles'), methods=['GET', ])           # получить все объявления
