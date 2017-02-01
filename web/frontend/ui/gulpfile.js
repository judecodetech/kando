var gulp = require('gulp');
var uglify = require('gulp-uglify');
var concat = require('gulp-concat');
var sass = require('gulp-sass');
var sourcemaps = require('gulp-sourcemaps');
var jscs = require('gulp-jscs');

var externalJSPaths = [
    'jquery/dist/jquery.js',
    'materialize/dist/js/materialize.js',
    ].map(function (g) { return 'bower_components/' + g; });

var externalCSSPaths = [

    /**
     * Same for CSS. If we use SCSS, we can import it directly from our stylesheets.
     */

    ].map(function (g) { return 'bower_components/' + g; });

var externalFontPaths = [
    'materialize/dist/fonts/**/*',
    ].map(function (g) { return 'bower_components/' + g; });

var paths = {
    fonts: externalFontPaths,
    images: 'img/**/*',
    js: {
        internal: ['app/**/*.js'],
        external: externalJSPaths,
    },
    scss: {
        internal: ['scss/style.scss'],
        external: externalCSSPaths,
    },
    scss_watch: ['scss/*.scss'],
    static: '../static/generated/',
};
console.log(externalJSPaths, externalFontPaths, paths.static + 'fonts/');

gulp.task('fonts', function () {
    gulp.src(paths.fonts)
        .pipe(gulp.dest(paths.static + 'fonts/'));
});

gulp.task('images', function () {
    gulp.src(paths.images)
        .pipe(gulp.dest(paths.static + 'img/'));
});

gulp.task('jscs', function () {
    return gulp.src(paths.js.internal)
        .pipe(jscs({ fix: true }))
        .pipe(jscs.reporter())
        .pipe(gulp.dest('app'));
});

gulp.task('scss:internal', ['scss:external'], function () {
    gulp.src(paths.scss.internal)
        .pipe(sourcemaps.init())
        .pipe(sass({
            outputStyle: 'compressed'
        }))
        .pipe(sourcemaps.write())
        .pipe(gulp.dest(paths.static + 'css/'));
});

gulp.task('scss:external', function (syncCallback) {
    var stream = gulp.src(paths.scss.external)
        .pipe(concat('_external.scss'))
        .pipe(gulp.dest('scss/generated/'));
    return stream;
});

gulp.task('js:internal', function () {
    gulp.src(paths.js.internal)
        .pipe(sourcemaps.init())
        .pipe(concat('internal.js'))

        // .pipe(uglify())
        .pipe(sourcemaps.write())
        .pipe(gulp.dest(paths.static + 'js/'));
});

gulp.task('js:external', function () {
    gulp.src(paths.js.external)
        .pipe(concat('external.js'))

        // .pipe(uglify())
        .pipe(gulp.dest(paths.static + 'js/'));
});

gulp.task('watch', function () {
    gulp.watch(paths.js.internal, ['js:internal']);
    gulp.watch(paths.scss_watch, ['scss:internal']);
});

gulp.task('default', [
    'watch',
    'fonts',
    'images',
    'js:internal',
    'js:external',
    'scss:external',
    'scss:internal']);

gulp.task('production', [
    'fonts',
    'images',
    'js:internal',
    'js:external',
    'scss:external',
    'scss:internal']);
