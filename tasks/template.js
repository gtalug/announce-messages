module.exports = function (grunt) {
    var config = {
        meeting_tpl: {
            files: {
                "meetings/#{grunt.template.today('yyyy-mm')}.txt":
                    ['_templates/meeting.txt.tpl']
            }
        }
    };
    
    grunt.config.set('template', config);
};
