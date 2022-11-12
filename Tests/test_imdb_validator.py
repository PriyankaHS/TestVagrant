import pytest

from POM.page_imdb import PageIMDB
from POM.page_wiki import PageWIKI


@pytest.mark.usefixtures("set_up")
class Test_Imdb_Wiki:

    @pytest.fixture(autouse=True)
    def SetUp(self, set_up):
        self.driver = set_up
        self.page_imdb = PageIMDB(self.driver)
        self.page_wiki = PageWIKI(self.driver)

    def test_validate_imdb(self, movie_name="Pushpa: The Rise"):
        self.page_imdb.enter_movie_name(movie_name)
        imdb_country = self.page_imdb.get_country_of_origin()
        imdb_dd, imdb_mm, imdb_yyyy = self.page_imdb.get_release_date()

        self.page_wiki.enter_movie_name(movie_name)
        wiki_country = self.page_wiki.get_country_of_origin()
        wiki_dd, wiki_mm, wiki_yyyy = self.page_wiki.get_release_date()
        
        assert imdb_country.lower() == wiki_country.lower()
        assert imdb_dd.lower() == wiki_dd.lower()
        assert imdb_mm.lower() == wiki_mm.lower()
        assert imdb_yyyy.lower() == wiki_yyyy.lower()

