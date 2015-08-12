//包装函数
module.exports = function(grunt){

	//任务配置，所有插件的配置信息
	grunt.initConfig({


		//获取package.json 的信息
		pkg: grunt.file.readJSON('package.json'),

		//uglify插件的配置信息
		uglify: {
			options: {
				stripBanners: true,
				banner: '/*! <%=pkg.name%>-<%=pkg.version%>.js <%= grunt.template.today("yyyy-mm-dd") %> */\n'
			},

			build: {
				src: 'src/Common.js',
				dest: 'build/<%=pkg.name%>-<%=pkg.version%>.js.min.js'
			}
		},

		//jshint插件的配置信息
		jshint: {

			options: { jshint: '.jshintrc'	},

			build: { 'Gruntfile.js': 'src/*.js' }
		},

		//csslint插件的配置信息
		csslint: {

			options: { csslint: '.csslintrc' },

			lax: {
				options: { import: false },
				src: ['src/*.css']
			},
		},
		
		//watch插件的配置
		watch: {
			build: {
				files: ['src/*js', 'src/*.css'],
				tasks: ['jshint', 'uglify'],
				options: { spawn: false }
			}
		}

	});

	//告诉我们grunt我们将使用插件
	grunt.loadNpmTasks('grunt-contrib-uglify');
	//告诉我们grunt我们将使用插件
	grunt.loadNpmTasks('grunt-contrib-jshint');
	//告诉我们grunt我们将使用插件
	grunt.loadNpmTasks('grunt-contrib-csslint');
	//告诉grunt需要安装的插件
	grunt.loadNpmTasks('grunt-contrib-watch');



	//告诉grunt当我们在终端输入grunt时需要做些什么(注意先后顺序)

	grunt.registerTask('default', ['jshint', 'uglify', 'watch']);

};



















