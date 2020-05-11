from django.test import TestCase

from catalog.models import Author, Book, Genre, BookInstance, Language


class BaseModelTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super(BaseModelTestCase, cls).setUpClass()
        cls.author = Author.objects.create(
            first_name='Omar', last_name='Munchaev')
        cls.author.save()
        cls.genre = Genre.objects.create(name='Ahuennaya')
        cls.genre.save()
        cls.language = Language.objects.create(name="Russian")
        cls.language.save()
        cls.book = Book.objects.create(
            language=cls.language, author=cls.author, title='Kniga ebanaya', summary='Da bla bilo takoe', isbn='1234567891')
        cls.book.save()
        genre_objects_for_book = Genre.objects.all()
        cls.book.genre.set(genre_objects_for_book)
        cls.book.save()
        cls.bookinstance = BookInstance(imprint='eto imprint ya hui ego')
        cls.bookinstance.save()
        cls.bookinstance.book = cls.book
        cls.bookinstance.save()


class BookModelTest(BaseModelTestCase):

    def test_title_label(self):
        field_label = self.book._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_author_label(self):
        field_label = self.book._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_summary_label(self):
        field_label = self.book._meta.get_field('summary').verbose_name
        self.assertEquals(field_label, 'summary')

    def test_isbn_label(self):
        field_label = self.book._meta.get_field('isbn').verbose_name
        self.assertEquals(field_label, 'isbn')

    def test_language_label(self):
        field_label = self.book._meta.get_field('language').verbose_name
        self.assertEquals(field_label, 'language')

    def test_title_max_length(self):
        max_length = self.book._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    def test_object_name_title(self):
        expected_object_name = f'{self.book.title}'
        self.assertEquals(expected_object_name, str(self.book.title))


class AuthorModelTest(BaseModelTestCase):

    def test_first_name_label(self):
        field_label = self.author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_date_of_death_label(self):
        field_label = self.author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label, 'died')

    def test_first_name_max_length(self):
        max_length = self.author._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        expected_object_name = f'{self.author.last_name}, {self.author.first_name}'
        self.assertEquals(expected_object_name, str(self.author))

    def test_get_absolute_url(self):
        # This will also fail if the urlconf is not defined.
        self.assertEquals(self.author.get_absolute_url(), '/catalog/author/1')

    def test_last_name_label(self):
        field_label = self.author._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_date_of_birth_label(self):
        field_label = self.author._meta.get_field('date_of_birth').verbose_name
        self.assertEquals(field_label, 'date of birth')

    def test_last_name_max_length(self):
        max_length = self.author._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 100)

    """

class BookModelTest(BaseModelTestCase):

    def test_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_author_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_summary_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('summary').verbose_name
        self.assertEquals(field_label, 'summary')

    def test_isbn_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('isbn').verbose_name
        self.assertEquals(field_label, 'isbn')

    def genre """
