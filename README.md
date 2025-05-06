# WLang - The programming language for the web
## Why?
In February 2023 to January 2024 I was learning web development, from basics to advanced topics. To be honest, almost everything was kind of "easy" to learn and practice.

But I knew several people trying to learn web development but it's too difficult, and I can understand them because the web languages are divided into several sintaxis.

For example, here is a list of web languages with different sintaxis or concepts:
- HTML
- CSS
- JavaScript
- PHP
- TypeScript (slight)
- Angular
- React.js
- Next.js

You get it, if you want to become a web developer you have to learn at least 3 or 4 different sintaxis.

But here is WLang (as a prototype for the moment). THE language that will centralize all those sintaxis in only one to simplify the web development but with the same features.
## Installation guide
1. Download the installer from [here](https://github.com/Zen-kun04/WLang/releases/tag/Prototype)
2. Open the installer. This will installer the compiler

## Code example
File: index.wl
```wl
main() {
    h1("This is a level-1 heading tag");
    p("This is a paragraph");
}
```
will return (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<body>
<h1>This is a level-1 heading tag</h1>
<p>This is a paragraph</p>
</body>

</html>
<!-- Made with <3 using WLang -->
```

## Complete example
File: index.wl
```wl
head() {
    page.setLang("fr");
    page.setTitle("WLang Website");
}

main() {
    heading1("WLang");
    paragraph("The programming language for the web");
}

footer() {
    url("https://github.com/Zen-kun04/WLang", "GitHub");
}
```

File: index.html
```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>WLang Website</title>
</head>
<body>
<h1>WLang</h1>
<p>The programming language for the web</p>
</body>
<footer>
<a href="https://github.com/Zen-kun04/WLang">GitHub</a>
</footer>
</html>
<!-- Made with <3 using WLang -->
```

## Reusable Components
File: index.wl
```wl
head() {
    page.setLang("fr");
    page.setTitle("WLang Website with Components");
}

comp MyComponent {
    paragraph("This is a paragraph used in a reusable component");
    p("Another paragraph but using the p() function!");
    paragraph("WLang components are very cool!!!");
}

main() {
    heading1("WLang");
    paragraph("Using Components!");
    MyComponent;
    MyComponent;
}

footer() {
    url("https://github.com/Zen-kun04/WLang", "GitHub");
}
```

File: index.html
```html
<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WLang Website with Components</title>
</head>

<body>
    <main>
        <h1>WLang</h1>
        <p>Using Components!</p>
        <p>This is a paragraph used in a reusable component</p>
        <p>Another paragraph but using the p() function!</p>
        <p>WLang components are very cool!!!</p>
        <p>This is a paragraph used in a reusable component</p>
        <p>Another paragraph but using the p() function!</p>
        <p>WLang components are very cool!!!</p>
    </main>
</body>
<footer>
    <a href="https://github.com/Zen-kun04/WLang">GitHub</a>
</footer>

</html><!-- Made with <3 using WLang -->
```