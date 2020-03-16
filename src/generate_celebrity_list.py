import actors
import dancers
import youtubers
import inventors
import comedians
import male_boxers
import bullfighters
import female_boxers
import tattoo_artists
import social_thinkers
import news_presenters
import fashion_designers
import singer_songwriters
import dance_personalities
import forbes_celebrity_100
import television_presenters
import avenue_of_stars_london
import league_of_legends_players
import guest_stars_of_the_simpsons
import guest_stars_of_sesame_street
import film_and_television_directors
import stars_on_hollywood_walk_of_fame
import celebrities_with_advanced_degrees

from pprint import pprint


def get_celebrities_data():
    ...


def main2():
    data = actors.get_specific_roles_or_genres_links()
    data = actors.get_nationality_links()
    data = actors.get_other_links()

    data = guest_stars_of_the_simpsons.get_guest_star_links()
    data = guest_stars_of_the_simpsons.get_guest_star_animators_links()

    data = guest_stars_of_sesame_street.get_guest_star_links()

    data = inventors.get_inventors_links()

    data = celebrities_with_advanced_degrees.get_celebrity_links()

    data = comedians.get_comedians_links()

    data = dance_personalities.get_dance_personalities_links()
    data = dance_personalities.get_ballet_dance_personalities_links()

    data = dancers.get_dance_personalities_links()

    data = fashion_designers.get_fashion_designers_links()
    data = fashion_designers.get_fashion_designers_links2()

    data = female_boxers.get_female_boxers_links()

    data = film_and_television_directors.get_film_and_television_directors_links()

    data = forbes_celebrity_100.get_forbes_celebrity_100_links()

    data = league_of_legends_players.get_league_of_legends_players_links()

    data = male_boxers.get_male_boxers_links()

    data = news_presenters.get_news_presenters_links()
    data = news_presenters.get_news_presenters_links2()

    data = singer_songwriters.get_singer_songwriters_links()
    data = singer_songwriters.get_singer_songwriters_links2()

    data = social_thinkers.get_social_thinkers_links()

    data = stars_on_hollywood_walk_of_fame.get_stars_on_hollywood_walk_of_fame_links()

    data = bullfighters.get_bullfighters_links()

    data = avenue_of_stars_london.get_avenue_of_stars_london_links()

    data = tattoo_artists.get_tattoo_artists_links()

    data = television_presenters.get_television_presenters_links()

    data = television_presenters.get_television_presenters_links2()

    data = youtubers.get_youtubers_links()

    # pprint(data)
    ...


# Driver Function
if __name__ == '__main__':
    import cProfile
    cProfile.run('main2()', 'restats')
    import pstats
    p = pstats.Stats('restats')
    # p.strip_dirs().sort_stats(-1).print_stats()
    p.sort_stats('cumulative').print_stats("Celeb_Data_Analytics/wiki_scrap_master*", 10)

