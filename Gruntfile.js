module.exports = function (grunt) {
    'use strict';
    
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        // mandrill: grunt.file.readJSON('mandrill.json'),
    });
    
    grunt.loadNpmTasks('grunt-template');
    grunt.loadNpmTasks('grunt-nodemailer');
    
    grunt.task.loadTasks('./tasks/');
}