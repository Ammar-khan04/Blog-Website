from myApp.models import Post
from django.contrib.auth.models import User
from django.utils.text import slugify

# Change this to your actual username
username = 'ammar'  # or your superuser's username
user = User.objects.get(username=username)

posts = [
    {
        'title': 'Walter White: Breaking Bad',
        'content': 'Walter White, a chemistry teacher turned meth kingpin, navigates the criminal underworld in Breaking Bad.',
        'slug': 'walter-white-breaking-bad',
    },
    {
        'title': 'Jesse Pinkman: Breaking Bad',
        'content': "Jesse Pinkman, Walter White's former student and partner, faces moral dilemmas and personal struggles.",
        'slug': 'jesse-pinkman-breaking-bad',
    },
    {
        'title': 'Geralt of Rivia: The Witcher',
        'content': 'Geralt, a monster hunter known as a Witcher, travels the Continent facing beasts and destiny.',
        'slug': 'geralt-of-rivia-the-witcher',
    },
    {
        'title': 'Yennefer of Vengerberg: The Witcher',
        'content': 'Yennefer, a powerful sorceress, seeks power, love, and her own identity in a world of magic and war.',
        'slug': 'yennefer-of-vengerberg-the-witcher',
    },
    {
        'title': "Heisenberg's Legacy: Breaking Bad",
        'content': "The legend of Heisenberg grows as Walter White's actions ripple through Albuquerque's criminal world.",
        'slug': 'heisenbergs-legacy-breaking-bad',
    },
    {
        'title': 'Ciri: The Witcher',
        'content': 'Ciri, the Lion Cub of Cintra, is pursued for her Elder Blood and her connection to Geralt and Yennefer.',
        'slug': 'ciri-the-witcher',
    },
    # More Breaking Bad
    {
        'title': 'Saul Goodman: Breaking Bad',
        'content': 'Saul Goodman, the colorful lawyer, helps Walter and Jesse navigate legal and illegal troubles.',
        'slug': 'saul-goodman-breaking-bad',
    },
    {
        'title': 'Skyler White: Breaking Bad',
        'content': "Skyler White, Walter's wife, struggles with the truth and her own moral boundaries.",
        'slug': 'skyler-white-breaking-bad',
    },
    {
        'title': 'Mike Ehrmantraut: Breaking Bad',
        'content': 'Mike, a fixer and enforcer, is known for his calm demeanor and efficiency.',
        'slug': 'mike-ehrmantraut-breaking-bad',
    },
    # More Witcher
    {
        'title': 'Triss Merigold: The Witcher',
        'content': 'Triss, a skilled sorceress and friend to Geralt, plays a key role in the politics of the Continent.',
        'slug': 'triss-merigold-the-witcher',
    },
    {
        'title': 'Vesemir: The Witcher',
        'content': 'Vesemir, the oldest Witcher at Kaer Morhen, is a mentor and father figure to Geralt.',
        'slug': 'vesemir-the-witcher',
    },
    # General pop culture
    {
        'title': 'Jon Snow: Game of Thrones',
        'content': 'Jon Snow, the King in the North, faces the threat of the White Walkers and his own heritage.',
        'slug': 'jon-snow-game-of-thrones',
    },
    {
        'title': 'Tony Stark: Iron Man',
        'content': 'Tony Stark, a genius billionaire, becomes Iron Man and leads the Avengers against global threats.',
        'slug': 'tony-stark-iron-man',
    },
    {
        'title': 'Darth Vader: Star Wars',
        'content': 'Darth Vader, once Anakin Skywalker, is a powerful Sith Lord and tragic figure in the Star Wars saga.',
        'slug': 'darth-vader-star-wars',
    },
    {
        'title': 'Hermione Granger: Harry Potter',
        'content': 'Hermione Granger, the brightest witch of her age, is a loyal friend and key to defeating Voldemort.',
        'slug': 'hermione-granger-harry-potter',
    },
]

for post in posts:
    obj, created = Post.objects.get_or_create(
        slug=post['slug'],
        defaults={
            'title': post['title'],
            'content': post['content'],
            'author': user,
            'status': 1,  # Published
        }
    )
    if created:
        print(f"Created: {post['title']}")
    else:
        print(f"Already exists: {post['title']}") 