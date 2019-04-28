import movie
import fresh_tomatoes

Moana = movie.Movie('Moana')
Moana.storyline('On the Polynesian island of Motunui, the inhabitants worship the goddess Te Fiti, who brought life to the ocean, using a pounamu stone as her heart and the source of her power')
Moana.poster('https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg')
Moana.trailer('https://www.youtube.com/watch?v=Dadu2KLjMVM')

tarzan = movie.Movie('Tarzan')
tarzan.storyline('Tarzan jungel man')
tarzan.poster('https://upload.wikimedia.org/wikipedia/en/4/4f/Tarzan_%281999_film%29_-_theatrical_poster.jpg')
tarzan.trailer('https://www.youtube.com/watch?v=lfciC33t3M0')

deadpool = movie.Movie('DeadPool')
deadpool.storyline('Wade Wilson is a dishonorably discharged special forces operative working as a mercenary when he meets prostitute Vanessa.')
deadpool.poster('https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg')
deadpool.trailer('https://www.youtube.com/watch?v=20bpjtCbCz0')

suicide_squad = movie.Movie('Suicide Squad')
suicide_squad.storyline("In the aftermath of Superman's death, intelligence officer Amanda Waller reaches Washington D.C for assembling Task Force X, and shows them to everyone in the White House a team of dangerous criminals imprisoned at Belle Reve Prison consisting of elite hitman Deadshot, former psychiatrist Harley Quinn, pyrokinetic ex-gangster El Diablo, opportunistic thief Captain Boomerang, genetic mutation Killer Croc, and specialized assassin Slipknot.")
suicide_squad.poster('https://upload.wikimedia.org/wikipedia/en/5/50/Suicide_Squad_%28film%29_Poster.png')
suicide_squad.trailer('https://www.youtube.com/watch?v=CmRih_VtVAs')

star_wars = movie.Movie('Star Wars')
star_wars.storyline("Shortly after the battle of Starkiller Base, Resistance forces, led by General Leia Organa, flee D'Qar when a First Order fleet arrives. Poe Dameron leads a costly counterattack that destroys a First Order dreadnought, but after the Resistance escapes to hyperspace, the First Order tracks them and attacks the Resistance convoy.")
star_wars.poster('https://upload.wikimedia.org/wikipedia/en/7/7f/Star_Wars_The_Last_Jedi.jpg')
star_wars.trailer('https://www.youtube.com/watch?v=Q0CbN8sfihY')

tomb_raider = movie.Movie('Tomb Raider')
tomb_raider.storyline("Following the disappearance of her father, Richard Croft, Lara Croft makes a living as a bike courier")
tomb_raider.poster('https://upload.wikimedia.org/wikipedia/en/b/bd/Tomb_Raider_%282018_film%29.png')
tomb_raider.trailer('https://www.youtube.com/watch?v=8ndhidEmUbI')

print (movie.Movie.__doc__)
movies = [deadpool, tarzan, Moana, suicide_squad, star_wars, tomb_raider]
fresh_tomatoes.open_movies_page(movies)