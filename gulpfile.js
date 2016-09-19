var gulp = require('gulp'),
    autoprefix = require('gulp-autoprefixer'),
    sass = require('gulp-sass'),
    notify = require('gulp-notify');

gulp.task('styles', function () {
    gulp.src('./collection/static/scss/*.scss')
        .pipe(sass({
            sourcemap: true,
            outputStyle: 'compressed'
        }))
        .on('error', notify.onError(function (error) {
            return 'Couldn\'t compile styles: ' + error.message;
        }))
        .on('error', function(err) {this.emit('end');})
        .pipe(autoprefix({browsers: [
            'Android 2.3',
            'Android >= 4',
            'Chrome >= 20',
            'Firefox >= 24',
            'Explorer >= 8',
            'iOS >= 6',
            'Opera >= 12',
            'Safari >= 6'
        ]}))
        .pipe(gulp.dest('./collection/static/css/'))
        .pipe(notify('Styles Built Successfully!'));
});

gulp.task('default', ['styles'], function(){
    gulp.watch('./collection/static/scss/*.scss', ['styles']);
});