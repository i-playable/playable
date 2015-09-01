module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    // Task configuration goes here.
    uglify: {
      app: {
        options:{
          compress: true
        },
        files: [{
          expand: true,
          cwd: 'assets/src/js/app',
          src: '**/*.js',
          dest: 'assets/build/js',
          ext : '.min.js'
        }]
      },

      vendor: {
        options:{
          compress: true
        },
        files: [{
          expand: true,
          cwd: 'assets/src/js/vendor',
          src: '**.js',
          dest: 'assets/build/js/vendor',
          ext : '.min.js'
        }]
      },
    },

    less: {
      dev: {
        options:{
          compress: true,
        },
        files: [{
          expand: true,
          cwd: 'assets/src/less',
          src: ['*.less'],
          dest: 'assets/src/css',
          ext: '.min.css'
        }]
      }
    },

    cssmin: {
      target: {
        files: [{
          expand: true,
          cwd: 'assets/src/css',
          src: ['*.css', '!*.min.css'],
          dest: 'assets/build/css',
          ext: '.min.css'
        }]
      }
    },

    copy: {
      images: {
        files: [
          {
            expand: true,
            cwd: 'assets/src/img/',
            src: ['**/*.{png,jpg,svg,gif,ico}'],
            dest:'assets/build/img/'
          }
        ]
      },

      css: {
        files: [
          {
            expand: true,
            cwd: 'assets/src/css/',
            src: ['**/*.min.css', '**/*.min.css.map'],
            dest:'assets/build/css/'
          }
        ]
      },

      font: {
        files: [
          {
            expand: true,
            cwd: 'assets/src/fonts/',
            src: ['**/*'],
            dest:'assets/build/fonts/'
          }
        ]
      }
    },



    watch: {
      options: {livereload: true},
      javascript: {
          files: ['assets/src/js/**/*.js'],
          tasks: ['uglify']
      },
      css: {
          files: 'assets/src/css/**/*.css',
          tasks: ['cssmin', 'copy:css']
          // tasks: ['copy:css']
      },

      less: {
          files: 'assets/src/less/**/*.less',
          tasks: ['less:dev', 'copy:css']
      },

      img_font: {
          files: ['assets/src/img/*','assets/src/fonts/*'],
          tasks: ['copy:font','copy:images']
      },
    }
  });

  // Load plugins here.
  grunt.loadNpmTasks('grunt-concat-css');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-watch');

  grunt.registerTask('default', ['uglify', 'less', 'copy', 'watch']);
};
