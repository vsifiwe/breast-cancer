let mix = require('laravel-mix');

mix.options({
    processCssUrls: false
});

mix.js('breast/frontend/Javascript/breast.js',
    'breast/static/breast/breast.js').setPublicPath('breast');

mix.sass('breast/frontend/SCSS/breast.scss',
    'breast/static/breast').setPublicPath('breast');
