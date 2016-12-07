from distutils.core import setup

setup(
    name = "Localization.SqlLocalizer ",
    version = "1.0",
    packages = [
        "sqllocalizer",
        "sqllocalizer.management",
        "sqllocalizer.management.commands",
        "sqllocalizer.templatetags",
        "sqllocalizer.tests",
    ],
    author = "Damien Bowden",
    author_email = "damien_bod@hotmail.com",
    description = "SQL localization for ASP.NET Core",
    url = "https://github.com/damienbod/AspNet5Localization",
    package_data = {
        'sqllocalizer': [
            'templates/*.html',
            'templates/sqllocalizer/*.html',
            'templates/sqllocalizer/*.txt',
            'fixtures/*.json',

        ],
    },
)
