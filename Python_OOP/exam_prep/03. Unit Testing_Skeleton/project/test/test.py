from project.library import Library
from unittest import TestCase, main


class LibraryTests(TestCase):

    def test_init__when_valid__expect_to_be_initialized_correctly(self):
        library = Library("library")

        self.assertEqual("library", library.name)
        self.assertEqual({}, library.books_by_authors)
        self.assertEqual({}, library.readers)

    def test_init__when_name_is_empty_str__expect_to_raise_an_exception(self):
        with self.assertRaises(ValueError) as context:
            library = Library("")

        self.assertEqual("Name cannot be empty string!", str(context.exception))

    def test_add_book__when_author_not_in_books_by_authors__expect_to_add_author_and_title(self):
        author = "Vlado"
        title = "New Book"
        library = Library("library")
        library.add_book(author, title)

        self.assertTrue(author in library.books_by_authors)
        self.assertEqual([title], library.books_by_authors[author])

    def test_add_book__when_author_is_in_books_by_authors_but_tittle_is_not__expect_to_add_new_tittle(self):
        author = "Vlado"
        title = "New Book"
        new_title = "Book 2"
        library = Library("library")
        library.add_book(author, title)
        library.add_book(author, new_title)

        self.assertEqual([title, new_title], library.books_by_authors[author])

    def test_add_reader__when_reader_not_registered__expect_to_add_reader_to_readers(self):
        library = Library("library")
        library.add_reader("Pesho")

        self.assertEqual(1, len(library.readers))
        self.assertEqual({"Pesho": []}, library.readers)

    def test_add_reader__when_reader_not_registered__expect_to_return_str(self):
        name = "Pesho"
        library = Library("library")
        library.add_reader(name)
        result = library.add_reader(name)

        self.assertEqual(f"{name} is already registered in the {library.name} library.", result)

    def test_rent_book__when_reader_not_registered__expect_to_return_str(self):
        author = "Gosho"
        title = "Book"
        name = "Vlado"
        library = Library("library")
        library.add_book(author, title)
        result = library.rent_book(name, author, title)

        self.assertTrue(name not in library.readers)
        self.assertEqual(f"{name} is not registered in the {library.name} Library.", result)

    def test_rent_book__when_author_not_in_books_by_authors__expect_to_return_str(self):
        author = "Gosho"
        title = "Book"
        name = "Vlado"
        library = Library("library")
        library.add_reader(name)
        result = library.rent_book(name, author, title)

        self.assertTrue(author not in library.books_by_authors)
        self.assertEqual(f"{library.name} Library does not have any {author}'s books.", result)

    def test_rent_book__when_author_dont_have_book_with_that_title_expect_to_return_str(self):
        author = "Gosho"
        title = "Book"
        searched_title = "Book 2"
        name = "Vlado"
        library = Library("library")
        library.add_reader(name)
        library.add_book(author, title)
        result = library.rent_book(name, author, searched_title)

        self.assertTrue(searched_title not in library.books_by_authors[author])
        self.assertEqual(f"""{library.name} Library does not have {author}'s "{searched_title}".""", result)

    def test_ret_book__when_we_have_correct_reader_author_title__expect_to_rent_a_book(self):
        author = "Gosho"
        title = "Book"
        title_2 = "Book 2"
        name = "Vlado"
        library = Library("library")
        library.add_reader(name)
        library.add_book(author, title)
        library.add_book(author, title_2)
        library.rent_book(name, author, title)

        self.assertEqual([{author: title}], library.readers[name])
        self.assertEqual([title_2], library.books_by_authors[author])


if __name__ == '__main__':
    main()
